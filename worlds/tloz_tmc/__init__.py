import os
import logging
from typing import List, Dict

import yaml

from BaseClasses import Tutorial, Item, Region, Location, LocationProgressType
from Fill import fill_restrictive, FillError
from worlds.AutoWorld import WebWorld, World
from .Data import build_location_name_to_id_dict, build_item_name_to_id_dict
from worlds.tloz_tmc.data.Items import *
from .Logic import create_connections
from .Options import *
from .data import LOCATIONS_DATA
from .data.Constants import DUNGEONS_NAMES, ELEMENT
from .data.Regions import REGIONS
from .Client import TheMinishCapClient  # Unused, but required to register with BizHawkClient
from .data.logic.LogicPredicates import oos_can_reach_d2_stump


class TheMinishCapWeb(WebWorld):
    theme = "grass"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Minish cap for Archipelago on your computer.",
        "English",
        "tmc_setup_en.md",
        "tmc_setup/en",
        ["Deoxis9001"]
    )]


class TheMinishCapWorld(World):
    """
"""
    game = "The Legend of Zelda - The Minish Cap"
    options_dataclass = TheMinishCapOptions
    options: TheMinishCapOptions
    required_client_version = (0, 4, 4)
    web = TheMinishCapWeb()

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

    def generate_early(self):
        

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

  
    def set_rules(self):
        create_connections(self.multiworld, self.player)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("vaati", self.player)

    def create_item(self, name: str) -> Item:
        ap_code = self.item_name_to_id[name]
        classification = ITEMS_DATA[name]["classification"]
        return Item(name, classification, ap_code, self.player)

    def create_items(self):
        for loc_data in LOCATIONS_DATA.values():
           
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
                    

    def get_filler_item_name(self) -> str:

    def generate_output(self, output_directory: str):
        

    def write_spoiler(self, spoiler_handle):
        