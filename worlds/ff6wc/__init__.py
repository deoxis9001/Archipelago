import json
import os
import random
import shutil
import subprocess
import threading
from typing import NamedTuple, Union
import logging

from BaseClasses import Item, Location, Region, Entrance, MultiWorld, ItemClassification
from . import Logic
from .Rom import FF6WCDeltaPatch
from .Client import FF6WCClient
from ..generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from ..AutoWorld import World, LogicMixin, WebWorld
from NetUtils import SlotType
from .Locations import location_table
from .Items import item_table
from .Options import ff6wc_options, generate_flagstring
import Utils

from .WorldsCollide import wc


class FF6WCWeb(WebWorld):
    theme = "dirt"

class FF6WCWorld(World):
    option_definitions = ff6wc_options
    game = "Final Fantasy 6 Worlds Collide"
    topology_present = False
    data_version = 1
    base_id = 6000
    web = FF6WCWeb()

    item_name_to_id = {name: index for index, name in enumerate(item_table)}
    location_name_to_id = {name: index for index, name in enumerate(location_table)}

    all_characters = [
            'Terra', 'Locke', 'Cyan', 'Shadow', 'Edgar',
            'Sabin', 'Celes', 'Strago', 'Relm', 'Setzer',
            'Mog', 'Gau', 'Gogo', 'Umaro'
        ]

    all_espers = [
            "Ramuh", "Ifrit", "Shiva", "Siren", "Terrato", "Shoat", "Maduin",
            "Bismark", "Stray", "Palidor", "Tritoch", "Odin", "Raiden", "Bahamut",
            "Alexandr", "Crusader", "Ragnarok Esper", "Kirin", "ZoneSeek", "Carbunkl",
            "Phantom", "Sraphim", "Golem", "Unicorn", "Fenrir", "Starlet", "Phoenix",
        ]

    all_dragon_clears = [
            "Removed!", "Stomped!",
            "Blasted!", "Ditched!",
            "Wiped!", "Incinerated!",
            "Skunked!", "Gone!"
        ]

    item_name_groups = {
        'characters': all_characters,
        'espers': all_espers,
        "dragons": all_dragon_clears
    }

    for k, v in item_name_to_id.items():
        item_name_to_id[k] = v + base_id

    for k, v in location_name_to_id.items():
        if v is not None:
            location_name_to_id[k] = v + base_id

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.starting_characters = None
        self.generator_in_use = threading.Event()
        self.wc = None
        self.rom_name_available_event = threading.Event()

    def create_item(self, name: str):
        return FF6WCItem(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    def create_good_filler_item(self, name: str):
        return FF6WCItem(name, ItemClassification.useful, self.item_name_to_id[name], self.player)

    def create_filler_item(self, name: str):
        return FF6WCItem(name, ItemClassification.filler, self.item_name_to_id[name], self.player)

    def create_event(self, event: str):
        return FF6WCItem(event, ItemClassification.progression, None, self.player)

    def create_location(self, name, id, parent, event=False):
        return_location = FF6WCLocation(self.player, name, id, parent)
        return_location.event = event
        return return_location

    def generate_early(self):
        starting_characters = [
            (self.multiworld.StartingCharacter1[self.player].current_key).capitalize(),
            (self.multiworld.StartingCharacter2[self.player].current_key).capitalize(),
            (self.multiworld.StartingCharacter3[self.player].current_key).capitalize(),
            (self.multiworld.StartingCharacter4[self.player].current_key).capitalize()
        ]
        starting_characters = starting_characters[0:self.multiworld.StartingCharacterCount[self.player]]
        starting_characters.sort(key=lambda character: character == "Random_with_no_gogo_or_umaro")

        filtered_starting_characters = []
        for character in starting_characters:
            if character == "Random_with_no_gogo_or_umaro":
                character = random.choice(Rom.characters[:12])
                while character in filtered_starting_characters:
                    character = random.choice(Rom.characters[:12])
            if character not in filtered_starting_characters:
                filtered_starting_characters.append(character)

        self.starting_characters = filtered_starting_characters

    def create_regions(self):
        menu = Region("Menu", None, "Menu", self.player, self.multiworld)
        world_map = Region("World Map", None, "World Map", self.player, self.multiworld)
        final_dungeon = Region("Kefka's Tower", None, "Kefka's Tower", self.player, self.multiworld)

        for name, id in self.location_name_to_id.items():
            if name in Locations.dragon_events:
                id = None
            if name in Locations.kefka_checks:
                final_dungeon.locations.append(self.create_location(name, id, final_dungeon))
            elif name in Locations.accomplishment_data:
                final_dungeon.locations.append(self.create_location(name, None, final_dungeon, True))
            else:
                world_map.locations.append(self.create_location(name, id, world_map))

        airship = Entrance(self.player, "Airship", menu)
        final_dungeon_entrance = Entrance(self.player, "Kefka's Tower Landing", world_map)
        # airship.connect(menu)
        airship.connect(world_map)
        menu.exits.append(airship)
        world_map.exits.append(airship)
        self.multiworld.regions.append(menu)
        final_dungeon_entrance.connect(world_map)
        final_dungeon_entrance.connect(final_dungeon)
        world_map.exits.append(final_dungeon_entrance)
        final_dungeon.exits.append(final_dungeon_entrance)
        self.multiworld.regions.append(world_map)
        self.multiworld.regions.append(final_dungeon)

    def create_items(self):
        for item in map(self.create_item, self.item_name_to_id):
            if item.name in self.starting_characters:
                self.multiworld.push_precollected(item)
            elif item.name in Rom.characters or item.name in Rom.espers:
                self.multiworld.itempool.append(item)

    def set_rules(self):
        check_list = {
            "Terra": Locations.terra_checks,
            "Locke": Locations.locke_checks,
            "Cyan": Locations.cyan_checks,
            "Shadow": Locations.shadow_checks,
            "Edgar": Locations.edgar_checks,
            "Sabin": Locations.sabin_checks,
            "Celes": Locations.celes_checks,
            "Strago": Locations.strago_checks,
            "Relm": Locations.relm_checks,
            "Setzer": Locations.setzer_checks,
            "Mog": Locations.mog_checks,
            "Gau": Locations.gau_checks,
            "Gogo": Locations.gogo_checks,
            "Umaro": Locations.umaro_checks,
        }
        # Set every character locked check to require that character.
        for check_name, checks in check_list.items():
            for check in checks:
                set_rule(self.multiworld.get_location(check, self.player),
                         lambda state, character=check_name: state.has(character, self.player))

        for check in Locations.major_checks:
            add_item_rule(self.multiworld.get_location(check, self.player),
                          lambda item: item.name not in Items.okay_items)

        for check in Locations.item_only_checks:
            add_item_rule(self.multiworld.get_location(check, self.player),
                          lambda item: item.name not in self.item_name_groups["characters"]
                                       and item.name not in self.item_name_groups['espers']
                                       or item.player != self.player)

        for check in Locations.no_character_checks:
            add_item_rule(self.multiworld.get_location(check, self.player),
                          lambda item: item.name not in self.item_name_groups["characters"]
                                       or item.player != self.player)

        for check in Locations.no_item_checks:
            add_item_rule(self.multiworld.get_location(check, self.player),
                          lambda item: item.name in self.item_name_groups["characters"]
                                       or item.name in self.item_name_groups['espers']
                                       or item.player != self.player)

        for dragon in Locations.dragons:
            dragon_event = Locations.dragon_events_link[dragon]
            add_item_rule(self.multiworld.get_location(dragon_event, self.player),
                          lambda state: state.can_reach(str(dragon), 'Location', self.player))

        for location in Locations.fanatics_tower_checks:
            add_rule(self.multiworld.get_location(location, self.player),
                          lambda state: state.has_group("espers", self.player, 4))

        set_rule(self.multiworld.get_entrance("Kefka's Tower Landing", self.player),
                 lambda state: state._ff6wc_has_enough_characters(self.multiworld, self.player)
                               and state._ff6wc_has_enough_espers(self.multiworld, self.player))
        set_rule(self.multiworld.get_location("Beat Final Kefka", self.player),
                 lambda state: state.can_reach("Kefka's Tower", 'Location', self.player)
                               and state._ff6wc_has_enough_dragons(self.multiworld, self.player))

    def generate_basic(self):
        self.multiworld.get_location("Kefka's Tower", self.player).place_locked_item(
            self.create_event("Kefka's Tower Access"))
        self.multiworld.get_location("Beat Final Kefka", self.player).place_locked_item(self.create_event("Victory"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

        for index, dragon in enumerate(Locations.dragons):
            dragon_event = Locations.dragon_events_link[dragon]
            self.multiworld.get_location(dragon_event, self.player).place_locked_item(
                self.create_event(self.all_dragon_clears[index]))

        #filler_item = self.create_item("Junk")
        filler_count = len(
            self.multiworld.get_unfilled_locations(self.player)) - len(
            [item for item in self.multiworld.itempool if item.player == self.player])
        filler_pool = []
        for item in Items.items:
            filler_pool.append(item)
        self.multiworld.itempool += [self.create_item(random.choice(filler_pool)) for _ in range(0, filler_count)]

    def post_fill(self) -> None:
        spheres = list(self.multiworld.get_spheres())
        sphere_count = len(spheres)
        upgrade_base = sphere_count * 2
        for current_sphere_count, sphere in enumerate(spheres):
            for location in sphere:
                if location.item.player == self.player:
                    if self.multiworld.random.randint(0, upgrade_base) < current_sphere_count:
                        self.upgrade_item(location.item)
        return

    def upgrade_item(self, item: Item):
        if item.name in Items.okay_items:
            new_item = self.multiworld.random.choice(Items.good_items)
            new_item_id = self.item_name_to_id[new_item]
            item.name = new_item
            item.code = new_item_id
            item.classification = ItemClassification.useful
        return

    def generate_output(self, output_directory: str):
        locations = dict()
        # get all locations
        for region in self.multiworld.regions:
            if region.player == self.player:
                for location in region.locations:
                    if location.name in Locations.minor_checks:
                        location_name = Rom.treasure_chest_data[location.name][2]
                    else:
                        location_name = location.name
                    locations[location_name] = "Archipelago Item"
                    if location.item.player == self.player:
                        locations[location_name] = location.item.name
        self.rom_name_text = f'6WC{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}'
        self.rom_name_text = self.rom_name_text[:20]
        self.romName = bytearray(self.rom_name_text, 'utf-8')
        self.romName.extend([0] * (20 - len(self.romName)))
        self.rom_name = self.romName
        locations["RomName"] = self.rom_name_text
        placement_file = os.path.join(output_directory,
                                      f'{self.multiworld.get_out_file_name_base(self.player)}' + '.txt')
        with open(placement_file, "w") as file:
            json.dump(locations, file, indent=2)
        output_file = os.path.join(output_directory,f"{self.multiworld.get_out_file_name_base(self.player)}.sfc")
        wc_args = ["-i", "Final Fantasy III (USA).sfc", "-o", f"{output_file}", "-ap", placement_file]
        wc_args.extend(generate_flagstring(self.multiworld, self.player, self.starting_characters))

        wc.main(wc_args)
        patch = FF6WCDeltaPatch(
            os.path.splitext(output_file)[0] + FF6WCDeltaPatch.patch_file_ending,
            player=self.player,
            player_name=self.multiworld.player_name[self.player],
            patched_path=output_file)
        self.rom_name_available_event.set()
        patch.write()
        os.remove(output_file)


    def modify_multidata(self, multidata: dict):
        import base64
        # wait for self.rom_name to be available.
        rom_name = getattr(self, "rom_name", None)
        # we skip in case of error, so that the original error in the output thread is the one that gets raised
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]


class FF6WCItem(Item):
    game = 'Final Fantasy 6 Worlds Collide'


class FF6WCLocation(Location):
    game = 'Final Fantasy 6 Worlds Collide'

