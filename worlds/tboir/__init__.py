import logging
import string

from .Items import TheBindingOfIsaacRepentanceItem, item_table, default_weights, default_junk_items_weights, \
    default_trap_items_weights
from .Locations import location_table, TheBindingOfIsaacRepentanceLocation, base_location_table
from .Rules import set_rules
from .Options import tobir_options

from BaseClasses import Region, Entrance, Item, MultiWorld, Tutorial, ItemClassification, CollectionState
from worlds.AutoWorld import World, WebWorld


class TheBindingOfIsaacRepentanceWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the The Binding Of Isaac Repentance integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Cyb3R"]
    )]


class TheBindingOfIsaacRepentanceWorld(World):
    """
    The Binding of Isaac: Rebirth is a randomly generated action RPG shooter with heavy Rogue-like elements.
    Following Isaac on his journey players will find bizarre treasures that change Isaac’s form giving him super
    human abilities and enabling him to fight off droves of mysterious creatures, discover secrets and fight his way
    to safety.
    """
    game: str = "The Binding of Isaac Repentance"
    option_definitions = tobir_options
    topology_present = False

    item_name_to_id = {name: data.id for name, data in item_table.items()}
    location_name_to_id = location_table
    item_name_groups = {'Any Progression': [name for name, data in item_table.items() if data.is_progression()]}

    data_version = 5
    web = TheBindingOfIsaacRepentanceWeb()

    def generate_early(self) -> None:
        if self.multiworld.required_locations[self.player].value > self.multiworld.total_locations[self.player].value:
            self.multiworld.total_locations[self.player].value = self.multiworld.required_locations[self.player].value

    def generate_basic(self):
        if not self.multiworld.player_name[self.player].isalnum():
            logging.warning(f"The name {self.multiworld.player_name[self.player]} for a TBoI world contains "
                            f"non-alphanumerical characters. You are not guaranteed to be able to enter the name "
                            f"ingame and may have to edit the games savefile to connect.")
        # Generate item pool
        itempool = []

        junk_item_count = round(
            self.multiworld.total_locations[self.player] * (self.multiworld.junk_percentage[self.player] / 100))
        collectable_item_count = self.multiworld.total_locations[self.player] - junk_item_count

        if self.multiworld.item_weights[self.player] == 99:
            item_weights = {name: val for name, val in self.multiworld.custom_item_weights[self.player].value.items()}
        else:
            item_weights = default_weights

        # Fill non-junk items
        itempool += self.multiworld.random.choices(list(item_weights.keys()), weights=list(item_weights.values()),
                                              k=collectable_item_count)

        trap_item_count = round(junk_item_count * (self.multiworld.trap_percentage[self.player] / 100))
        junk_item_count = junk_item_count - trap_item_count

        trap_weights = {name: val for name, val in self.multiworld.trap_item_weights[self.player].value.items()}
        junk_weights = {name: val for name, val in self.multiworld.custom_junk_item_weights[self.player].value.items()}

        # Fill traps
        itempool += self.multiworld.random.choices(list(trap_weights.keys()), weights=list(trap_weights.values()),
                                              k=trap_item_count)

        # Fill remaining items with randomly generated junk
        itempool += self.multiworld.random.choices(list(junk_weights.keys()), weights=list(junk_weights.values()),
                                              k=junk_item_count)

        assert len(itempool) == self.multiworld.total_locations[self.player]

        # Convert itempool into real items
        itempool = list(map(lambda name: self.create_item(name), itempool))

        self.multiworld.itempool += itempool

    def set_rules(self):
        set_rules(self.multiworld, self.player)
    #     self.enforce_early_items_before_first_event()
    #
    # def enforce_early_items_before_first_event(self):
    #     early_items = []
    #     for player, item_count in self.multiworld.early_items.items():
    #         for item, count in item_count.items():
    #             if self.multiworld.worlds[player].create_item(item).advancement:
    #                 early_items.append((player, item, count))
    #
    #     for item, count in self.multiworld.local_early_items[self.player].items():
    #         if self.create_item(item).advancement:
    #             early_items.append((self.player, item, count))
    #
    #     def first_event_require_all_early_items(state: CollectionState) -> bool:
    #         for player, item, count in early_items:
    #             if not state.has(item, player, count):
    #                 return False
    #
    #         return True
    #
    #     locations_per_event = 25
    #     first_event = self.multiworld.get_location(f"Pickup{locations_per_event}", self.player)
    #     set_rule(first_event, first_event_require_all_early_items)

    def create_regions(self):
        create_regions(self.multiworld, self.player)
        create_events(self.multiworld, self.player, int(self.multiworld.total_locations[self.player].value))

    def fill_slot_data(self):
        return {
            "itemPickupStep": self.multiworld.item_pickup_step[self.player].value,
            "seed": ''.join(self.multiworld.per_slot_randoms[self.player].choice(string.digits) for _ in range(16)),
            "totalLocations": self.multiworld.total_locations[self.player].value,
            "requiredLocations": self.multiworld.required_locations[self.player].value,
            "goal": self.multiworld.goal[self.player].value,
            "additionalBossRewards": self.multiworld.additional_boss_rewards[self.player].value,
            "deathLink": self.multiworld.death_link[self.player].value,
            "teleportTrapCanError": self.multiworld.teleport_trap_can_error[self.player].value,
            "fullNoteAmount": self.multiworld.full_note_amount[self.player].value,
            "noteMarksAmount": self.multiworld.note_marks_amount[self.player].value,
            "noteMarkRequireHardMode": self.multiworld.note_marks_require_hard_mode[self.player].value,
            "splitStartItems": self.multiworld.split_start_items[self.player].value
        }

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = TheBindingOfIsaacRepentanceItem(name, item_data.classification, item_data.id, self.player)
        return item

    def collect_item(self, state: "CollectionState", item: "Item", remove: bool = False):
        if item.advancement:
            return "Progression Item"

        return super(TheBindingOfIsaacRepentanceWorld, self).collect_item(state, item, remove)


def create_events(world: MultiWorld, player: int, total_locations: int):
    locations_per_event = 25
    num_of_events = total_locations // locations_per_event

    if total_locations / locations_per_event == num_of_events:
        num_of_events -= 1
    for i in range(num_of_events):
        event_loc = TheBindingOfIsaacRepentanceLocation(player, f"Pickup{(i + 1) * locations_per_event}", None,
                                                     world.get_region('In Run', player))
        event_loc.place_locked_item(
            TheBindingOfIsaacRepentanceItem(f"Pickup{(i + 1) * locations_per_event}", ItemClassification.progression, None,
                                         player))
        event_loc.access_rule(
            lambda state, i=i: state.can_reach(f"ItemPickup{((i + 1) * locations_per_event) - 1}", player) and state.has("Progression Item", player, i+1))
        world.get_region('In Run', player).locations.append(event_loc)


# generate locations based on player setting
def create_regions(world, player: int):
    world.regions += [
        create_region(world, player, 'Menu', None, ['New Run']),
        create_region(world, player, 'In Run',
                      [location for location in base_location_table] +
                      [f"ItemPickup{i}" for i in range(1, 1 + world.total_locations[player].value)])
    ]

    world.get_entrance("New Run", player).connect(world.get_region("In Run", player))
    world.get_location("Victory", player).place_locked_item(TheBindingOfIsaacRepentanceItem("Victory", ItemClassification.progression, None, player))


def create_region(world: MultiWorld, player: int, name: str, locations=None, exits=None):
    ret = Region(name, player, world)
    ret.world = world
    if locations:
        for location in locations:
            loc_id = location_table[location]
            location = TheBindingOfIsaacRepentanceLocation(player, location, loc_id, ret)
            ret.locations.append(location)
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, exit, ret))

    return ret
