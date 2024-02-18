from typing import TYPE_CHECKING, Set, Dict

from NetUtils import ClientStatus
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient
from worlds.tloz_oos import LOCATIONS_DATA, ITEMS_DATA
from .Data import build_item_id_to_name_dict, build_location_name_to_id_dict

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

ROM_ADDRS = {
    "game_identifier": (0x0134, 9, "ROM"),
    "slot_name": (0x0000, 64, "ROM"),  # TODO: Inject using patcher and put addr here
}

RAM_ADDRS = {
    "game_state": (0xC2EE, 1, "System Bus"),
    "received_item_index": (0xC6A0, 2, "System Bus"),
    "received_item": (0xCBFB, 1, "System Bus"),
    "location_flags": (0xC600, 0x500, "System Bus"),  # TODO: Find and set the real address
    "game_clear_byte": (0x0000, 1, "System Bus"),  # TODO: Find and set the real address
}

class OracleOfSeasonsClient(BizHawkClient):
    game = "The Legend of Zelda: Oracle of Seasons"
    system = "GBC"
    patch_suffix = ".apseasons"
    local_checked_locations: Set[int]
    item_id_to_name: Dict[int, str]
    location_name_to_id: Dict[str, int]

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.item_id_to_name = build_item_id_to_name_dict()
        self.location_name_to_id = build_location_name_to_id_dict()

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            # Check ROM name/patch version
            rom_name_bytes = (await bizhawk.read(ctx.bizhawk_ctx, [ROM_ADDRS["game_identifier"]]))[0]
            rom_name = bytes([byte for byte in rom_name_bytes if byte != 0]).decode("ascii")
            if rom_name != "ZELDA DIN":
                return False
        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False

        ctx.game = self.game
        ctx.items_handling = 0b001
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.5

        return True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        # slot_name_bytes = (await bizhawk.read(ctx.bizhawk_ctx, [ROM_ADDRS["slot_name"]]))[0]
        # ctx.auth = bytes([byte for byte in slot_name_bytes if byte != 0]).decode("utf-8")
        pass

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        # if ctx.slot_data is not None:
        #    if ctx.slot_data["goal"] == Goal.option_beat_onox:
        #        self.goal_flag = BEAT_ONOX_FLAG

        try:
            # Handle giving the player items
            read_result = await bizhawk.read(ctx.bizhawk_ctx, [
                RAM_ADDRS["game_state"],  # Current state of game (is the player actually in-game?)
                RAM_ADDRS["received_item_index"],  # Number of received items
                RAM_ADDRS["received_item"],  # Received item still pending?
                RAM_ADDRS["location_flags"],  # Location flags
                RAM_ADDRS["game_clear_byte"],  # Has goal been completed?
            ])
            if read_result is None:
                return

            # Player is not in-game, don't do anything else
            if read_result[0][0] != 2:
                return

            num_received_items = int.from_bytes(read_result[1], "little")
            received_item_is_empty = (read_result[2][0] == 0)
            flag_bytes = read_result[3]
            game_clear = (read_result[4] == 1)  # TODO: Might be a different value

            # If the game hasn't received all items yet and the received item struct doesn't contain an item, then
            # fill it with the next item
            if num_received_items < len(ctx.items_received) and received_item_is_empty:
                received_item = list(RAM_ADDRS["received_item"])
                next_item_name = self.item_id_to_name[ctx.items_received[num_received_items].item]
                received_item[1] = [
                    ITEMS_DATA[next_item_name]["id"],
                    ITEMS_DATA[next_item_name]["subid"] if "subid" in ITEMS_DATA[next_item_name] else 0
                ]

                received_item_index = list(RAM_ADDRS["received_item_index"])
                received_item_index[1] = (num_received_items + 1).to_bytes(2, "little")

                await bizhawk.write(ctx.bizhawk_ctx, [
                    tuple(received_item),
                    tuple(received_item_index)
                ])

            # Read location flags from RAM
            local_checked_locations = set()
            for name, location in LOCATIONS_DATA.items():
                if "local" in location and location["local"] is True:
                    continue
                if "randomized" in location and location["randomized"] is False:
                    continue
                byte_offset = location["flag_byte"] - RAM_ADDRS["location_flags"][0]
                bit_mask = location["bit_mask"] if "bit_mask" in location else 0x20
                if flag_bytes[byte_offset] & bit_mask == bit_mask:
                    location_id = self.location_name_to_id[name]
                    local_checked_locations.add(location_id)

            # Send locations
            if local_checked_locations != ctx.locations_checked:
                self.local_checked_locations = local_checked_locations
                if local_checked_locations is not None:
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(local_checked_locations)
                    }])

            # Send game clear
            if not ctx.finished_game and game_clear:
                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])

        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass
