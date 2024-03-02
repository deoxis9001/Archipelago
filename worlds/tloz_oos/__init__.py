import os
import logging
from typing import List, Dict

import yaml

from BaseClasses import Tutorial, Item, Region, Location, LocationProgressType
from Fill import fill_restrictive, FillError
from worlds.AutoWorld import WebWorld, World
from .Data import build_location_name_to_id_dict, build_item_name_to_id_dict
from worlds.tloz_oos.data.Items import *
from .Logic import create_connections
from .Options import *
from .data import LOCATIONS_DATA
from .data.Constants import SEED_ITEMS, REGIONS_CONVERSION_TABLE, PORTALS_CONVERSION_TABLE, DUNGEON_NAMES, \
    SEASONS, COMPANIONS, ESSENCES, DIRECTIONS, DUNGEON_ITEMS, LOCATION_GROUPS
from .data.Regions import REGIONS
from .Client import OracleOfSeasonsClient  # Unused, but required to register with BizHawkClient
from .data.logic.LogicPredicates import oos_can_reach_d2_stump


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
    The seasons in the world of Holodrum have been a mess since Onox captured Din, the oracle of seasons.
    Gather the Essences of Nature, confront Onox and rescue Din to give nature some rest in Holodrum.
    """
    game = "The Legend of Zelda - Oracle of Seasons"
    options_dataclass = OracleOfSeasonsOptions
    options: OracleOfSeasonsOptions
    required_client_version = (0, 4, 4)
    web = OracleOfSeasonsWeb()

    location_name_to_id = build_location_name_to_id_dict()
    item_name_to_id = build_item_name_to_id_dict()
    location_name_groups = LOCATION_GROUPS

    pre_fill_items: List[Item]
    dungeon_items: List[Item]
    default_seed: str
    default_seasons: Dict[str, str]
    dungeon_entrances: Dict[str, str]
    portal_connections: Dict[str, str]
    lost_woods_item_sequence: List[str]
    old_man_rupee_values: Dict[str, int]

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.pre_fill_items = []
        self.dungeon_items = []
        self.default_seed = SEED_ITEMS[0]
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
            "TARM_RUINS": "spring"
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

    def fill_slot_data(self) -> dict:
        options = ["goal", "logic_difficulty"]
        slot_data = self.options.as_dict(*options)
        return slot_data

    def generate_early(self):
        self.default_seed = self.random.choice(SEED_ITEMS)

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
            if "conditional" in location_data and location_data["conditional"] is True:
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
        self.create_event("bomb flower", "Bomb Flower")
        for i in range(8):
            self.create_event(f"d{i+1} boss", ESSENCES[i])
        self.create_event("maku seed", "Maku Seed")

        self.create_event("onox beaten", "_beaten_onox")

        self.create_event("maple trade", "Ghastly Doll")
        self.create_event("spool stump", "_reached_spool_stump")
        self.create_event("bomb temple remains", "_triggered_volcano")
        self.create_event("temple remains lower stump", "_reached_remains_stump")
        self.create_event("temple remains upper stump", "_reached_remains_stump")
        self.create_event("d1 stump", "_reached_eyeglass_stump")
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

        # Only create progression events related to D2 stump if it's actually reachable
        if oos_can_reach_d2_stump(self):
            self.create_event("d2 stump", "_reached_d2_stump")
        if oos_can_reach_d2_stump(self) or self.default_seasons["WOODS_OF_WINTER"] == "autumn":
            self.create_event("golden moblin", "_beat_golden_moblin")

        for region_name in self.old_man_rupee_values:
            self.create_event(region_name, "rupees from " + region_name)

    def exclude_problematic_locations(self):
        # Some locations become unreachable with specific options, exclude them to prevent any harm from happening
        if not oos_can_reach_d2_stump(self):
            locations_to_exclude = ["chest on top of D2"]
            if self.default_seasons["WOODS_OF_WINTER"] != "autumn":
                locations_to_exclude.append("cave outside D2")
                if self.options.golden_beasts_requirement == 4:
                    locations_to_exclude.append("golden beasts old man")
            for name in locations_to_exclude:
                self.multiworld.get_location(name, self.player).progress_type = LocationProgressType.EXCLUDED

    def set_rules(self):
        create_connections(self.multiworld, self.player)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("_beaten_onox", self.player)

    def create_item(self, name: str) -> Item:
        ap_code = self.item_name_to_id[name]
        classification = ITEMS_DATA[name]["classification"]
        return Item(name, classification, ap_code, self.player)

    def create_items(self):
        ring_count = 0
        for loc_data in LOCATIONS_DATA.values():
            if "randomized" in loc_data and loc_data["randomized"] is False:
                continue
            if "vanilla_item" not in loc_data:
                continue

            item_name = loc_data['vanilla_item']
            if item_name == "Ricky's Gloves":  # Ricky's gloves are useless in current logic
                item_name = "Progressive Sword"
            elif item_name == "Rod of Seasons":  # No lone rod of seasons supported for now
                item_name = "Fool's Ore" if self.options.fools_ore != "excluded" else "Gasha Seed"
            elif item_name == "Flute":
                item_name = str(self.options.animal_companion.value) + "'s Flute"

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

        self.multiworld.random.shuffle(ring_names)
        del ring_names[amount:]
        for ring_name in ring_names:
            self.multiworld.itempool.append(self.create_item(ring_name))

    def get_pre_fill_items(self):
        return self.pre_fill_items

    def pre_fill(self) -> None:
        self.pre_fill_fixed_items()
        self.pre_fill_seeds()
        self.pre_fill_dungeon_items()

    def pre_fill_fixed_items(self):
        # Fill some shop items with their fixed contents
        bomb_item = self.create_item("Bombs (10)")
        self.multiworld.get_location("shop, 20 rupees", self.player).place_locked_item(bomb_item)
        self.pre_fill_items.append(bomb_item)

        shield_item = self.create_item("Wooden Shield")
        self.multiworld.get_location("shop, 30 rupees", self.player).place_locked_item(shield_item)
        self.pre_fill_items.append(shield_item)

        # TODO: Force fixed Subrosian shop items

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
        def place_seed(seed_name: str, location_name: str):
            seed_item = self.create_item(seed_name)
            self.multiworld.get_location(location_name, self.player).place_locked_item(seed_item)
            self.pre_fill_items.append(seed_item)

        # Fill Horon tree with default seed
        place_seed(self.default_seed, "horon village tree")

        # Fill all other trees randomly
        trees = ["woods of winter tree", "north horon tree", "spool swamp tree", "sunken city tree", "tarm ruins tree"]
        seeds = [s for s in SEED_ITEMS]
        self.random.shuffle(seeds)
        while seeds and trees:
            place_seed(seeds.pop(), trees.pop())

    def get_filler_item_name(self) -> str:
        return "Rupees (1)"

    def generate_output(self, output_directory: str):
        yamlObj = {
            "settings": {
                "game": "seasons",
                "companion": self.options.animal_companion.value,
                "warp_to_start": self.options.warp_to_start.current_key,
                "required_essences": self.options.required_essences.value,
                "fools_ore_damage": 3 if self.options.fools_ore == "balanced" else 12,
                "heart_beep_interval": self.options.heart_beep_interval.current_key,
                "lost_woods_item_sequence": ' '.join(self.lost_woods_item_sequence),
                "golden_beasts_requirement": self.options.golden_beasts_requirement.value,
                "slot_name": self.multiworld.get_player_name(self.player)
             },
            "default seasons": {},
            "old man rupee values": {},
            "locations": {}
        }

        for region_name, season in self.default_seasons.items():
            yamlObj["default seasons"][REGIONS_CONVERSION_TABLE[region_name]] = season

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
            yamlObj["locations"][loc.name] = item_name

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