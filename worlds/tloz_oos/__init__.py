import os
import logging

import yaml

from BaseClasses import Tutorial, Region, Location, LocationProgressType
from Fill import fill_restrictive, FillError
from worlds.AutoWorld import WebWorld, World
from .Data import *
from worlds.tloz_oos.data.Items import *
from .Logic import create_connections
from .Options import *
from .data import LOCATIONS_DATA
from .data.Constants import SEED_ITEMS, REGIONS_CONVERSION_TABLE, PORTALS_CONVERSION_TABLE, DUNGEON_NAMES, \
    SEASONS, COMPANIONS, DIRECTIONS, DUNGEON_ITEMS, LOCATION_GROUPS, ITEM_GROUPS, VERSION, VALID_RUPEE_VALUES
from .data.Regions import REGIONS
from .Client import OracleOfSeasonsClient  # Unused, but required to register with BizHawkClient


class OracleOfSeasonsWeb(WebWorld):
    theme = "grass"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Oracle of Seasons for Archipelago on your computer.",
        "English",
        "oos_setup_en.md",
        "oos_setup/en",
        ["Dinopony"]
    )]


class OracleOfSeasonsWorld(World):
    """
    The Legend of Zelda: Oracles of Seasons is one of the rare Capcom entries to the series.
    The seasons in the world of Holodrum have been a mess since Onox captured Din, the Oracle of Seasons.
    Gather the Essences of Nature, confront Onox and rescue Din to give nature some rest in Holodrum.
    """
    game = "The Legend of Zelda - Oracle of Seasons"
    options_dataclass = OracleOfSeasonsOptions
    options: OracleOfSeasonsOptions
    required_client_version = (0, 4, 4)
    web = OracleOfSeasonsWeb()

    location_name_to_id = build_location_name_to_id_dict()
    item_name_to_id = build_item_name_to_id_dict()
    item_name_groups = ITEM_GROUPS
    location_name_groups = LOCATION_GROUPS

    pre_fill_items: List[Item]
    dungeon_items: List[Item]
    default_seasons: Dict[str, str]
    dungeon_entrances: Dict[str, str]
    portal_connections: Dict[str, str]
    lost_woods_item_sequence: List[str]
    old_man_rupee_values: Dict[str, int]
    shop_prices: Dict[str, int]
    samasa_gate_code: List[int]

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.pre_fill_items = []
        self.dungeon_items = []
        self.default_seasons = {
            "EYEGLASS_LAKE": "winter",
            "NORTH_HORON": "spring",
            "EASTERN_SUBURBS": "autumn",
            "WOODS_OF_WINTER": "summer",
            "SUNKEN_CITY": "summer",
            "WESTERN_COAST": "winter",
            "SPOOL_SWAMP": "autumn",
            "TEMPLE_REMAINS": "winter",
            "LOST_WOODS": "autumn",
            "TARM_RUINS": "spring",
            "HORON_VILLAGE": "spring"
        }
        self.dungeon_entrances = {
            "d1 entrance": "enter d1",
            "d2 entrance": "enter d2",
            "d3 entrance": "enter d3",
            "d4 entrance": "enter d4",
            "d5 entrance": "enter d5",
            "d6 entrance": "enter d6",
            "d7 entrance": "enter d7",
            "d8 entrance": "enter d8",
        }
        self.portal_connections = {
            "eastern suburbs portal": "subrosia portal 1",
            "spool swamp portal": "subrosia portal 2",
            "mt. cucco portal": "subrosia portal 3",
            "horon village portal": "subrosia portal 4",
            "eyeglass lake portal": "subrosia portal 5",
            "temple remains lower portal": "subrosia portal 6",
            "temple remains upper portal": "subrosia portal 7",
        }
        self.lost_woods_item_sequence = [
            "winter", "left",
            "autumn", "left",
            "spring", "left",
            "summer", "left"
        ]
        self.old_man_rupee_values = {
            "old man in horon": 100,
            "old man near d1": 100,
            "old man near blaino": 200,
            "old man in goron mountain": 300,
            "old man near western coast house": 300,
            "old man near holly's house": -50,
            "old man near mrs. ruul": -100,
            "old man near d6": -200
        }

        self.samasa_gate_code = [2, 2, 1, 0, 0, 3, 3, 3]

        self.shop_prices = {
            "horon shop 1": 1,
            "horon shop 2": 1,
            "horon shop 3": 1,
            "member shop 1": 1,
            "member shop 2": 1,
            "member shop 3": 1,
            "advance shop 1": 1,
            "advance shop 2": 1,
            "advance shop 3": 1,
            "syrup shop 1": 1,
            "syrup shop 2": 1,
            "syrup shop 3": 1,
            "subrosian market 2": 2,
            "subrosian market 3": 2,
            "subrosian market 4": 2,
            "subrosian market 5": 2,
        }

    def fill_slot_data(self) -> dict:
        # Put options that are useful to the tracker inside slot data
        options = ["goal", "logic_difficulty", "required_essences", "horon_village_season",
                   "shuffle_dungeons", "shuffle_portals", "shuffle_old_men", "treehouse_old_man_requirement",
                   "golden_beasts_requirement", "lost_woods_item_sequence", "advance_shop", "warp_to_start"]

        slot_data = self.options.as_dict(*options)
        slot_data["animal_companion"] = COMPANIONS[self.options.animal_companion.value]
        slot_data["default_seed"] = SEED_ITEMS[self.options.default_seed.value]

        slot_data["default_seasons"] = {}
        for region_name, season in self.default_seasons.items():
            slot_data["default_seasons"][REGIONS_CONVERSION_TABLE[region_name]] = season
        if self.options.horon_village_season == "chaotic":
            slot_data["default_seasons"][REGIONS_CONVERSION_TABLE["HORON_VILLAGE"]] = "chaotic"

        slot_data["dungeon_entrances"] = self.dungeon_entrances
        slot_data["portal_connections"] = self.portal_connections

        return slot_data

    def generate_early(self):
        self.options.non_local_items.value -= self.item_name_groups["Dungeon Items"]

        if self.options.default_seasons == "randomized":
            for region in self.default_seasons:
                self.default_seasons[region] = self.random.choice(SEASONS)
        elif self.options.default_seasons.current_key.endswith("singularity"):
            singularities = {
                "random_singularity": self.random.choice(SEASONS),
                "spring_singularity": "spring",
                "summer_singularity": "summer",
                "winter_singularity": "winter",
                "autumn_singularity": "autumn",
            }
            single_season = singularities[self.options.default_seasons.current_key]
            for region in self.default_seasons:
                self.default_seasons[region] = single_season

        if self.options.shuffle_dungeons == "shuffle":
            shuffled_entrances = list(self.dungeon_entrances.values())
            self.random.shuffle(shuffled_entrances)
            self.dungeon_entrances = dict(zip(self.dungeon_entrances, shuffled_entrances))

        if self.options.shuffle_portals == "shuffle":
            def shuffle_portals():
                shuffled_portals = list(self.portal_connections.values())
                self.random.shuffle(shuffled_portals)
                self.portal_connections = dict(zip(self.portal_connections, shuffled_portals))
            shuffle_portals()
            while self.portal_connections["temple remains upper portal"] == "subrosia portal 6":
                shuffle_portals()

        if self.options.lost_woods_item_sequence == "randomized":
            authorized_directions = [direction for direction in DIRECTIONS if direction != "right"]
            self.lost_woods_item_sequence = [
                self.random.choice(SEASONS), self.random.choice(authorized_directions),
                self.random.choice(SEASONS), self.random.choice(authorized_directions),
                self.random.choice(SEASONS), self.random.choice(authorized_directions),
                self.random.choice(SEASONS), "left"
            ]

        if self.options.shuffle_old_men == "shuffled_values":
            shuffled_rupees = list(self.old_man_rupee_values.values())
            self.random.shuffle(shuffled_rupees)
            self.old_man_rupee_values = dict(zip(self.old_man_rupee_values, shuffled_rupees))

        if self.options.samasa_gate_code == "randomized":
            self.samasa_gate_code = []
            for i in range(self.options.samasa_gate_code_length.value):
                self.samasa_gate_code.append(self.random.randint(0, 3))

        self.randomize_shop_prices()

    def randomize_shop_prices(self):
        prices_pool = get_prices_pool()
        self.random.shuffle(prices_pool)
        global_prices_factor = self.options.shop_prices_factor.value / 100.0
        for key, divider in self.shop_prices.items():
            floating_price = prices_pool.pop() * global_prices_factor / divider
            for i, value in enumerate(VALID_RUPEE_VALUES):
                if value > floating_price:
                    self.shop_prices[key] = VALID_RUPEE_VALUES[i-1]
                    break

    def location_is_active(self, location_data):
        if "conditional" not in location_data or location_data["conditional"] is False:
            return True

        region_id = location_data["region_id"]
        if region_id == "advance shop":
            return self.options.advance_shop.value
        if region_id.startswith("subrosia") and region_id.endswith("digging spot"):
            return self.options.shuffle_golden_ore_spots != "vanilla"
        return False

    def create_location(self, region_name: str, location_name: str, local: bool):
        region = self.multiworld.get_region(region_name, self.player)
        location = Location(self.player, location_name, self.location_name_to_id[location_name], region)
        region.locations.append(location)
        if local:
            location.item_rule = lambda item: item.player == self.player

    def create_regions(self):
        # Create regions
        for region_name in REGIONS:
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations
        for location_name, location_data in LOCATIONS_DATA.items():
            if not self.location_is_active(location_data):
                continue

            is_local = "local" in location_data and location_data["local"] is True
            self.create_location(location_data['region_id'], location_name, is_local)

        self.create_events()
        self.exclude_problematic_locations()

    def create_event(self, region_name, event_item_name):
        region = self.multiworld.get_region(region_name, self.player)
        location = Location(self.player, region_name + ".event", None, region)
        region.locations.append(location)
        location.place_locked_item(Item(event_item_name, ItemClassification.progression, None, self.player))

    def create_events(self):
        self.create_event("subrosian smithy bell", "Pirate's Bell")
        self.create_event("maku seed", "Maku Seed")

        if self.options.goal == OracleOfSeasonsGoal.option_beat_onox:
            self.create_event("onox beaten", "_beaten_game")
        elif self.options.goal == OracleOfSeasonsGoal.option_beat_ganon:
            self.create_event("ganon beaten", "_beaten_game")

        self.create_event("maple trade", "Ghastly Doll")
        self.create_event("spool stump", "_reached_spool_stump")
        self.create_event("bomb temple remains", "_triggered_volcano")
        self.create_event("temple remains lower stump", "_reached_remains_stump")
        self.create_event("temple remains upper stump", "_reached_remains_stump")
        self.create_event("d1 stump", "_reached_eyeglass_stump")
        self.create_event("d2 stump", "_reached_d2_stump")
        self.create_event("d5 stump", "_reached_eyeglass_stump")
        self.create_event("sunken city dimitri", "_saved_dimitri_in_sunken_city")
        self.create_event("ghastly stump", "_reached_ghastly_stump")
        self.create_event("coast stump", "_reached_coast_stump")
        self.create_event("subrosia market sector", "_reached_rosa")
        self.create_event("subrosian dance hall", "_reached_subrosian_dance_hall")
        self.create_event("subrosia pirates sector", "_met_pirates")
        self.create_event("tower of autumn", "_opened_tower_of_autumn")
        self.create_event("d2 moblin chest", "_reached_d2_bracelet_room")
        self.create_event("d5 drop ball", "_dropped_d5_magnet_ball")
        self.create_event("d8 SE crystal", "_dropped_d8_SE_crystal")
        self.create_event("d8 NE crystal", "_dropped_d8_NE_crystal")
        self.create_event("d2 rupee room", "_reached_d2_rupee_room")
        self.create_event("d6 rupee room", "_reached_d6_rupee_room")

        self.create_event("golden darknut", "_beat_golden_darknut")
        self.create_event("golden lynel", "_beat_golden_lynel")
        self.create_event("golden octorok", "_beat_golden_octorok")
        self.create_event("golden moblin", "_beat_golden_moblin")

        self.create_event("d4 miniboss room hard embers", "_hard_ember_seeds")
        self.create_event("d5 armos chest", "_hard_ember_seeds")
        self.create_event("d7 entrance hard embers", "_hard_ember_seeds")

        for region_name in self.old_man_rupee_values:
            self.create_event(region_name, "rupees from " + region_name)

    def exclude_problematic_locations(self):
        locations_to_exclude = []
        # If goal essence requirement is set to a specific value, prevent essence-bound checks which require more
        # essences than this goal to hold anything of value
        if self.options.required_essences < 7:
            locations_to_exclude.append("Horon Village: Item Inside Maku Tree (7+ Essences)")
            if self.options.required_essences < 5:
                locations_to_exclude.append("Horon Village: Item Inside Maku Tree (5+ Essences)")
                if self.options.required_essences < 3:
                    locations_to_exclude.append("Horon Village: Item Inside Maku Tree (3+ Essences)")
        if self.options.required_essences < self.options.treehouse_old_man_requirement:
            locations_to_exclude.append("Holodrum Plain: Old Man in Treehouse")

        for name in locations_to_exclude:
            self.multiworld.get_location(name, self.player).progress_type = LocationProgressType.EXCLUDED

    def set_rules(self):
        create_connections(self.multiworld, self.player)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("_beaten_game", self.player)

    def create_item(self, name: str) -> Item:
        ap_code = self.item_name_to_id[name]
        classification = ITEMS_DATA[name]["classification"]

        # A few items become progression only in hard logic
        progression_items_in_hard_logic = ["Expert's Ring", "Fist Ring", "Swimmer's Ring"]
        if self.options.logic_difficulty == "hard" and name in progression_items_in_hard_logic:
            classification = ItemClassification.progression

        return Item(name, classification, ap_code, self.player)

    def create_items(self):
        item_pool_adjustements = [
            ["Gasha Seed", "Seed Satchel"],  # Add a third satchel that is usually obtained in linked games (99 seeds)
            ["Gasha Seed", "Bombs (10)"],    # Add one more bomb compared to vanilla to reach 99 max bombs
            ["Gasha Seed", "Rupees (50)"],   # Too many Gasha Seeds in vanilla pool, add more rupees instead
            ["Gasha Seed", "Rupees (50)"],   # ^
            ["Gasha Seed", "Rupees (50)"],   # ^
            ["Gasha Seed", "Rupees (50)"],   # ^
        ]

        ring_count = 0
        for loc_name, loc_data in LOCATIONS_DATA.items():
            if "randomized" in loc_data and loc_data["randomized"] is False:
                item = self.create_item(loc_data['vanilla_item'])
                location = self.multiworld.get_location(loc_name, self.player)
                location.place_locked_item(item)
                continue
            if not self.location_is_active(loc_data):
                continue
            if "vanilla_item" not in loc_data:
                continue

            item_name = loc_data['vanilla_item']
            if item_name == "Ricky's Gloves":  # Ricky's gloves are useless in current logic
                item_name = "Progressive Sword"
            elif item_name == "Rod of Seasons":  # No lone rod of seasons supported for now
                item_name = "Fool's Ore" if self.options.fools_ore != "excluded" else "Gasha Seed"
            elif item_name == "Flute":
                item_name = COMPANIONS[self.options.animal_companion.value] + "'s Flute"

            for i, pair in enumerate(item_pool_adjustements):
                if item_name == pair[0]:
                    item_name = pair[1]
                    del item_pool_adjustements[i]
                    break

            if "Ring" in item_name:
                ring_count += 1
            elif any([(string in item_name) for string in DUNGEON_ITEMS]):
                self.dungeon_items.append(self.create_item(item_name))
            else:
                self.multiworld.itempool.append(self.create_item(item_name))

        self.create_rings(ring_count)

    def create_rings(self, amount):
        # Get a subset of as many rings as needed, with a potential filter on quality depending on chosen options
        ring_names = [name for name, idata in ITEMS_DATA.items() if "ring" in idata and idata["ring"] is True]
        if self.options.ring_quality == "only_useful":
            ring_names = [name for name in ring_names if ITEMS_DATA[name]["classification"] == ItemClassification.useful]

        self.random.shuffle(ring_names)
        del ring_names[amount:]
        for ring_name in ring_names:
            self.multiworld.itempool.append(self.create_item(ring_name))

    def get_pre_fill_items(self):
        return self.pre_fill_items

    def pre_fill(self) -> None:
        self.pre_fill_seeds()
        self.pre_fill_dungeon_items()

    def pre_fill_dungeon_items(self):
        # If keysanity is off, dungeon items can only be put inside local dungeon locations,
        # and there are not so many of those which makes them pretty crowded.
        # This usually ends up with generator not having anywhere to place a few small keys, making the seed unbeatable.
        # To circumvent this, we perform a restricted pre fill here, placing only those dungeon items
        # before anything else.
        collection_state = self.multiworld.get_all_state(False)

        for i in range(0, 9):
            dungeon_location_names = [name for name, data in LOCATIONS_DATA.items() if "dungeon" in data and data["dungeon"] == i]
            dungeon_locations = [loc for loc in self.multiworld.get_locations(self.player) if loc.name in dungeon_location_names]
            dungeon_items = [item for item in self.dungeon_items if item.name.endswith(f"({DUNGEON_NAMES[i]})")]
            for item in dungeon_items:
                collection_state.remove(item)

            for attempts_remaining in range(2, -1, -1):
                self.random.shuffle(dungeon_locations)
                try:
                    fill_restrictive(self.multiworld, collection_state, dungeon_locations, dungeon_items,
                                     single_player_placement=True, lock=True, allow_excluded=True)
                    break
                except FillError as exc:
                    if attempts_remaining == 0:
                        raise exc
                    logging.debug(f"Failed to shuffle dungeon items for player {self.player}. Retrying...")

    def pre_fill_seeds(self) -> None:
        # The prefill algorithm for seeds has a few constraints:
        #   - it needs to place the "default seed" into Horon Village seed tree
        #   - it needs to place a random seed on the "duplicate tree" (can be Horon's tree)
        #   - it needs to place one of each seed on the 5 remaining trees
        # This has a few implications:
        #   - if Horon is the duplicate tree, this is the simplest case: we just place a random seed in Horon's tree
        #     and scatter the 5 seed types on the 5 other trees
        #   - if Horon is NOT the duplicate tree, we need to remove Horon's seed from the pool of 5 seeds to scatter
        #     and put a random seed inside the duplicate tree. Then, we place the 4 remaining seeds on the 4 remaining
        #     trees
        TREES_TABLE = {
            OracleOfSeasonsDuplicateSeedTree.option_horon_village: "Horon Village: Seed Tree",
            OracleOfSeasonsDuplicateSeedTree.option_woods_of_winter: "Woods of Winter: Seed Tree",
            OracleOfSeasonsDuplicateSeedTree.option_north_horon: "Holodrum Plain: Seed Tree",
            OracleOfSeasonsDuplicateSeedTree.option_spool_swamp: "Spool Swamp: Seed Tree",
            OracleOfSeasonsDuplicateSeedTree.option_sunken_city: "Sunken City: Seed Tree",
            OracleOfSeasonsDuplicateSeedTree.option_tarm_ruins: "Tarm Ruins: Seed Tree",
        }
        duplicate_tree_name = TREES_TABLE[self.options.duplicate_seed_tree.value]

        def place_seed(seed_name: str, location_name: str):
            seed_item = self.create_item(seed_name)
            self.multiworld.get_location(location_name, self.player).place_locked_item(seed_item)
            self.pre_fill_items.append(seed_item)

        seeds_to_place = set([name for name in SEED_ITEMS])

        manually_placed_trees = ["Horon Village: Seed Tree", duplicate_tree_name]
        trees_to_process = [name for name in TREES_TABLE.values() if name not in manually_placed_trees]

        # Place default seed type in Horon Village tree
        place_seed(SEED_ITEMS[self.options.default_seed.value], "Horon Village: Seed Tree")

        # If duplicate tree is not Horon's, remove Horon seed from the pool of placeable seeds
        if duplicate_tree_name != "Horon Village: Seed Tree":
            seeds_to_place.remove(SEED_ITEMS[self.options.default_seed.value])
            place_seed(self.random.choice(SEED_ITEMS), duplicate_tree_name)

        # Place remaining seeds on remaining trees
        self.random.shuffle(trees_to_process)
        for seed in seeds_to_place:
            place_seed(seed, trees_to_process.pop())

    def get_filler_item_name(self) -> str:
        return "Rupees (1)"

    def generate_output(self, output_directory: str):
        yamlObj = {
            "settings": {
                "game": "seasons",
                "version": VERSION,
                "goal": self.options.goal.current_key,
                "companion": COMPANIONS[self.options.animal_companion.value],
                "warp_to_start": self.options.warp_to_start.current_key,
                "required_essences": self.options.required_essences.value,
                "fools_ore_damage": 3 if self.options.fools_ore == "balanced" else 12,
                "heart_beep_interval": self.options.heart_beep_interval.current_key,
                "lost_woods_item_sequence": ' '.join(self.lost_woods_item_sequence),
                "samasa_gate_sequence": ' '.join([str(x) for x in self.samasa_gate_code]),
                "golden_beasts_requirement": self.options.golden_beasts_requirement.value,
                "treehouse_old_man_requirement": self.options.treehouse_old_man_requirement.value,
                "sign_guy_requirement": self.options.sign_guy_requirement.value,
                "tarm_gate_required_jewels": self.options.tarm_gate_required_jewels.value,
                "reveal_golden_ore_tiles": self.options.shuffle_golden_ore_spots == "shuffled_visible",
                "quick_flute": self.options.quick_flute.current_key,
                "open_advance_shop": self.options.advance_shop.current_key,
                "character_sprite": self.options.character_sprite.current_key,
                "character_palette": self.options.character_palette.current_key,
                "slot_name": self.multiworld.get_player_name(self.player)
             },
            "default seasons": {},
            "old man rupee values": {},
            "locations": {},
            "shop prices": self.shop_prices
        }

        for region_name, season in self.default_seasons.items():
            yamlObj["default seasons"][REGIONS_CONVERSION_TABLE[region_name]] = season
        if self.options.horon_village_season == "chaotic":
            yamlObj["default seasons"][REGIONS_CONVERSION_TABLE["HORON_VILLAGE"]] = "chaotic"

        for region_name, value in self.old_man_rupee_values.items():
            yamlObj["old man rupee values"][region_name] = value

        if self.options.shuffle_dungeons != "vanilla":
            yamlObj["dungeon entrances"] = {}
            for entrance, dungeon in self.dungeon_entrances.items():
                yamlObj["dungeon entrances"][entrance] = dungeon.replace("enter ", "")

        if self.options.shuffle_portals != "vanilla":
            yamlObj["subrosia portals"] = {}
            for portal_holo, portal_sub in self.portal_connections.items():
                yamlObj["subrosia portals"][PORTALS_CONVERSION_TABLE[portal_holo]] = PORTALS_CONVERSION_TABLE[portal_sub]

        for loc in self.multiworld.get_locations(self.player):
            if loc.address is None:
                continue
            item_name = loc.item.name if loc.item.player == loc.player else "Archipelago Item"
            loc_patcher_name = find_patcher_name_for_location(loc.name)
            if loc_patcher_name != "":
                yamlObj["locations"][loc_patcher_name] = item_name

        filename = f"{self.multiworld.get_out_file_name_base(self.player)}.patcherdata"
        with open(os.path.join(output_directory, filename), 'w') as f:
            yaml.dump(yamlObj, f)

    def write_spoiler(self, spoiler_handle):
        spoiler_handle.write(f"\n\nDefault Seasons ({self.multiworld.player_name[self.player]}):\n")
        for region_name, season in self.default_seasons.items():
            spoiler_handle.write(f"\t- {REGIONS_CONVERSION_TABLE[region_name]} --> {season}\n")

        if self.options.shuffle_dungeons != "vanilla":
            spoiler_handle.write(f"\nDungeon Entrances ({self.multiworld.player_name[self.player]}):\n")
            for entrance, dungeon in self.dungeon_entrances.items():
                spoiler_handle.write(f"\t- {entrance} --> {dungeon.replace('enter ', '')}\n")

        if self.options.shuffle_portals != "vanilla":
            spoiler_handle.write(f"\nSubrosia Portals ({self.multiworld.player_name[self.player]}):\n")
            for portal_holo, portal_sub in self.portal_connections.items():
                spoiler_handle.write(f"\t- {PORTALS_CONVERSION_TABLE[portal_holo]} --> {PORTALS_CONVERSION_TABLE[portal_sub]}\n")
