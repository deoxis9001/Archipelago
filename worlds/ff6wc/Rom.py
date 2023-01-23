import hashlib
import os

import Utils
from Patch import APDeltaPatch

NA10HASH = 'e986575b98300f721ce27c180264d890'
ROM_PLAYER_LIMIT = 65535
ROM_NAME = 0x00FFC0
event_flag_base_address = 0xF51e80
bit_positions = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
esper_bit_base_address = 0xF51A69
character_intialized_bit_base_address = 0xF51EDC
character_recruited_bit_base_address = 0xf51EDE
item_types_base_address = 0xF51869
item_quantities_base_address = 0xF51969
items_received_address = 0xF511E5
map_index_address = 0xF50082
espers = [  # This is the internal order of the Espers in the game. Editing this will break things.
    "Ramuh", "Ifrit", "Shiva",
    "Siren", "Terrato", "Shoat",
    "Maduin", "Bismark", "Stray",
    "Palidor", "Tritoch", "Odin",
    "Raiden", "Bahamut", "Alexandr",
    "Crusader", "Ragnarok Esper", "Kirin",
    "ZoneSeek", "Carbunkl", "Phantom",
    "Sraphim", "Golem", "Unicorn",
    "Fenrir", "Starlet", "Phoenix"
]

characters = [  # Same here.
    "TERRA", "LOCKE", "CYAN", "SHADOW", "EDGAR", "SABIN", "CELES", "STRAGO",
    "RELM", "SETZER", "MOG", "GAU", "GOGO", "UMARO"
]

event_flag_location_names = {
    'Whelk': 0x135,
    'Lete River': 0x1a,
    'Sealed Gate': 0x471,
    'Zozo': 0x52,
    'Mobliz': 0x0bf,
    'South Figaro Cave': 0x0b1,
    'Narshe Weapon Shop 1': 0x0b7,
    "Narshe Weapon Shop 2": 0x0b6,
    'Phoenix Cave': 0x0d7,
    'Red Dragon': 0x120,
    'Doma Castle Siege': 0x040,
    'Dream Stooges': 0x0d8,
    'Wrexsoul': 0x0da,
    'Doma Castle Throne': 0x0db,
    'Mt. Zozo': 0x0d2,
    'Storm Dragon': 0x11b,
    'Gau Father House': 0x162,
    'Imperial Air Force': 0x02a,
    'AtmaWeapon': 0x0a1,
    'Nerapa': 0x0a5,
    'Veldt Cave': 0x199,
    'Figaro Castle Throne': 0x004,
    'Figaro Castle Basement': 0x0c6,
    'Ancient Castle': 0x2dd,
    'Blue Dragon': 0x11f,
    'Mt. Kolts': 0x010,
    'Collapsing House': 0x28a,
    'Baren Falls': 0x03f,
    'Imperial Camp': 0x037,
    'Phantom Train': 0x192,
    'South Figaro': 0x01d,
    'Ifrit and Shiva': 0x061,
    'Number 024': 0x05f,
    'Cranes': 0x06b,
    'Opera House': 0x5b,
    'Burning House': 0x090,
    "Ebot's Rock": 0x19c,
    'MagiMaster': 0x2db,
    'Gem Box': 0x0ba,
    'Esper Mountain': 0x095,
    "Owzer Mansion": 0x253,
    'Kohlingen': 0x18e,
    "Daryl's Tomb": 0x2b2,
    'Lone Wolf 1': 0x29f,
    "Lone Wolf 2": 0x241,
    'Veldt': 0x1bc,
    'Serpent Trench': 0x050,
    "Gogo's Cave": 0x0d4,
    "Umaro's Cave": 0x07e,
    'Kefka at Narshe': 0x046,
    'Tzen Thief': 0x27c,
    'Doom Gaze': 0x2a1,
    'Tritoch': 0x29e,
    'Auction House 10kGP': 0x16c,
    'Auction House 20kGP': 0x16d,
    'Dirt Dragon': 0x11c,
    'White Dragon': 0x121,
    'Ice Dragon': 0x11a,
    'Atma': 0x0a2,
    "Skull Dragon": 0x11e,
    "Gold Dragon": 0x11d
}

treasure_chest_data = {
    "Narshe Arvis's Clock": (0x1E40, 2),
    "Narshe Elder's Clock": (0x1E41, 2),
    "Narshe Adventuring School Advanced Battle Tactics Chest": (0x1E51, 4),
    "Narshe Adventuring School Battle Tactics Chest": (0x1E51, 3),
    "Narshe Adventuring School Environmental Science Chest": (0x1E51, 2),
    "Narshe Adventuring School Environmental Science Pot": (0x1E51, 5),
    "Narshe Treasure House South Chest": (0x1E41, 1),
    "Narshe Treasure House Middle Right": (0x1E41, 0),
    "Narshe Treasure House Middle Left": (0x1E40, 7),
    "Narshe Treasure House Top Right": (0x1E40, 6),
    "Narshe Treasure House Top Middle": (0x1E40, 5),
    "Narshe Treasure House Top Left": (0x1E40, 4),
    "Narshe Mines East Right WoB": (0x1E41, 3), #TODO: Fix this address
    "Narshe Mines East Left WoB": (0x1E41, 4), #TODO: Fix this address
    "Narshe Moogle Lair WoB": (0x1E41, 5), #TODO: Fix this address
    "Narshe Mines East Right WoR": (0x1E41, 3), #TODO: Fix this address
    "Narshe Mines East Left WoR": (0x1E41, 4), #TODO: Fix this address
    "Narshe Moogle Lair WoR": (0x1E41, 5), #TODO: Fix this address
    "Albrook Armor Shop Left": (0x1E4C, 5),
    "Albrook Armor Shop Right": (0x1E4C, 6),
    "Albrook Cafe Clock": (0x1E4C, 7),
    "Albrook Inn Barrel WoB": (0x1E4C, 2), # Fix this address
    "Albrook Inn Barrel WoR": (0x1E4C, 2), # Fix this address
    "Albrook Weapon Shop Pot": (0x1E4C, 4),
    "Albrook Docks Crate": (0x1E4C, 3),
    "Ancient Cave North Cavern Left": (0x1E58, 5),
    "Ancient Cave North Cavern Right": (0x1E58, 4),
    "Ancient Cave South Cavern Bottom": (0x1E58, 7),
    "Ancient Cave South Cavern Top": (0x1E58, 6),
    "Ancient Cave West Cavern Bottom": (0x1E59, 0),
    "Ancient Cave West Cavern Left": (0x1E59, 1),
    "Ancient Castle Treasure Room Left": (0x1E59, 2),
    "Ancient Castle Treasure Room Right": (0x1E59, 3),
    "Ancient Castle East Room": (0x1E59, 6),
    "Ancient Castle Library": (0x1E59, 4),
    "Ancient Castle Jail": (0x1E59, 5),
    "Sealed Gate Basement 1": (0x1E4F, 3),
    "Sealed Gate Basement 2 Bottom": (0x1E50, 5),
    "Sealed Gate Basement 2 Top": (0x1E50, 6),
    "Sealed Gate Basement 3 Bottom Left": (0x1E4F, 4),
    "Sealed Gate Basement 3 Island": (0x1E4F, 5),
    "Sealed Gate Basement 3 Plaza": (0x1E50, 0),
    "Sealed Gate Basement 3 Hidden Passage": (0x1E4F, 6),
    "Sealed Gate Basement 3 Bridge": (0x1E4F, 7),
    "Sealed Gate Entrance": (0x1E4F, 2),
    "Sealed Gate Save Point": (0x1E48, 4),
    "Sealed Gate Treasure Room Left": (0x1E50, 1),
    "Sealed Gate Treasure Room Upper Left": (0x1E50, 2),
    "Sealed Gate Treasure Room Upper Floor Left": (0x1E50, 3),
    "Sealed Gate Treasure Room Upper Floor Right": (0x1E50, 4),
    "Darill's Tomb Basement 2 Southeast": (0x1E53, 4),
    "Darill's Tomb Basement 2 Southwest": (0x1E53, 5),
    "Darill's Tomb Basement 3 Center": (0x1E53, 6),
    "Darill's Tomb Basement 3 Right": (0x1E53, 7),
    "Darill's Tomb Pre-Boss Room Left": (0x1E54, 1),
    "Darill's Tomb Pre-Boss Room Right": (0x1E54, 9),
    "Doma Castle Cyan's Bedroom": (0x1E4C, 0),
    "Doma Castle Lower Hall Pot": (0x1E46, 4),
    "Doma Castle Southeast Tower Left": (0x1E46, 5),
    "Doma Castle Southeast Tower Right": (0x1E46, 6),
    "Doma Castle West Sleeping Quarters Chest": (0x1E56, 3),
    "Doma Castle West Sleeping Quarters Clock": (0x1E46, 3),
    "Dragon's Neck Cabin Pot": (0x1E5C, 5),
    "Duncan's Cabin Bucket": (0x1E44, 4),
    "Cyan's Dream Phantom Train Fourth Car Upper Right": (0x1E57, 4),
    "Cyan's Dream Phantom Train Fourth Car Middle": (0x1E57, 5),
    "Cyan's Dream Phantom Train Third Car Bottom Right": (0x1E57, 2),
    "Cyan's Dream Phantom Train Third Car Middle": (0x1E57, 3),
    "Esper Mountain Entrance Cavern": (0x1E4D, 5),
    "Esper Mountain Outside Bridge": (0x1E4D, 2),
    "Esper Mountain Side Slope": (0x1E4D, 3),
    "Esper Mountain Treasure Slope": (0x1E4D, 4),
    "Fanatics' Tower Seventeenth Floor": (0x1E56, 5),
    "Fanatics' Tower Twenty-sixth Floor": (0x1E56, 6),
    "Fanatics' Tower Thirty-fifth Floor": (0x1E56, 7),
    "Fanatics' Tower Seventh Floor": (0x1E57, 1),
    "Fanatics' Tower Eighth Floor": (0x1E56, 4),
    "Figaro Castle East Shop Left": (0x1E41, 6),
    "Figaro Castle East Shop Right": (0x1E41, 7),
    "Figaro Castle Upper Hall": (0x1E42, 1),
    "Figaro Castle West Shop": (0x1E42, 0),
    "Figaro Castle Basement 2 Treasure Room": (0x1E53, 2),
    "Figaro Castle Basement 3 Treasure Room Far Left": (0x1E52, 6),
    "Figaro Castle Basement 3 Treasure Room Left": (0x1E52, 7),
    "Figaro Castle Basement 3 Treasure Room Right": (0x1E53, 0),
    "Figaro Castle Basement 3 Treasure Room Far Right": (0x1E53, 1),
    "Figaro Castle Basement 3 Treasure Room Statue": (0x1E53, 3),
    "Floating Continent North Path": (0x1E50, 7),
    "Floating Continent Lower Path": (0x1E4B, 7),
    "Floating Continent Northeast of Save": (0x1E51, 0),
    "Floating Continent Escape": (0x1E51, 1),
    "Imperial Base First Row Right": (0x1E4D, 7),
    "Imperial Base First Row Left": (0x1E4D, 6),
    "Imperial Base Stove": (0x1E4F, 1),
    "Imperial Base Second Row Far Right": (0x1E4E, 3),
    "Imperial Base Second Row Right": (0x1E4E, 2),
    "Imperial Base Second Row Left": (0x1E4E, 1),
    "Imperial Base Second Row Far Left": (0x1E4E, 0),
    "Imperial Base Third Row": (0x1E4E, 4),
    "Imperial Base Fourth Row Left": (0x1E4E, 5),
    "Imperial Base Fourth Row Right": (0x1E4E, 6),
    "Imperial Base Fifth Row Left": (0x1E4E, 7),
    "Imperial Base Fifth Row Right": (0x1E4F, 0),
    "Imperial Base Bottom Right Hidden Chest": (0x1E60, 1),
    "Imperial Camp Kick Chest": (0x1E46, 2),
    "Imperial Camp Central Tent Left": (0x1E5A, 4),
    "Imperial Camp Central Tent Right": (0x1E5A, 3),
    "Imperial Camp Central Tent Back": (0x1E5A, 2),
    "Owzer's House Pot": (0x1E48, 2),
    "Kefka's Tower Group 3 Balcony Left": (0x1E5C, 1),
    "Kefka's Tower Group 3 Balcony Right": (0x1E5C, 3),
    "Kefka's Tower Group 3 Entrance Stairs": (0x1E5C, 2),
    "Kefka's Tower Group 3 Hidden Room": (0x1E5E, 1),
    "Kefka's Tower Group 1 Metal Switchback": (0x1E5A, 7),
    "Kefka's Tower Group 1 Landing Area": (0x1E5A, 6),
    "Kefka's Tower Group 2 Left Area Top": (0x1E5B, 1),
    "Kefka's Tower Group 2 Left Area Bottom": (0x1E5B, 2),
    "Kefka's Tower Group 3 Right Path": (0x1E5B, 5),
    "Kefka's Tower Group 3 After Magitek Left": (0x1E5B, 3),
    "Kefka's Tower Group 3 After Magitek Right": (0x1E5B, 6),
    "Kefka's Tower Group 1 Winding Path": (0x1E5B, 4),
    "Kefka's Tower Poltergeist Hidden Chest": (0x1E5E, 2),
    "Kefka's Tower Group 2 Outside Switchback": (0x1E5B, 1),
    "Kefka's Tower Group 2 Pipe Output": (0x1E5B, 7),
    "Kefka's Tower Group 2 Switch Room": (0x1E5C, 0),
    "Kohlingen Old Man's House": (0x1E48, 1),
    "Kohlingen Rachel's House Clock": (0x1E48, 5),
    "Magitek Factory North Upper Left": (0x1E4A, 2),
    "Magitek Factory North Right Side Pipe": (0x1E4A, 3),
    "Magitek Factory North Lower Landing": (0x1E4A, 4),
    "Magitek Factory North Across Conveyor Belt": (0x1E4A, 7),
    "Magitek Factory North Near Crate": (0x1E4A, 5),
    "Magitek Factory North Lower Balcony": (0x1E4A, 6),
    "Magitek Factory South Secret Room Left": (0x1E4B, 2),
    "Magitek Factory South Secret Room Right": (0x1E4B, 3),
    "Magitek Factory South Lower Balcony": (0x1E4B, 4),
    "Magitek Factory South Hidden Chest": (0x1E4B, 5),
    "Magitek Factory South Lower Left": (0x1E4B, 1),
    "Magitek Factory South Bottom Left": (0x1E4B, 0),
    "Magitek Factory Specimen Room": (0x1E4B, 6),
    "Maranda Crate Left": (0x1E5E, 5),
    "Maranda Crate Bottom Right": (0x1E5E, 4),
    "Mobliz Shelter Pot": (0x1E54, 7),
    "Mobliz Post OFfice Clock": (0x1E47, 5),
    "Mobliz House Barrel": (0x1E5F, 3),
    "Mt. Kolts Exit": (0x1E45, 0),
    "Mt. Kolts Hidden Cavern": (0x1E44, 7),
    "Mt. Kolts West Face South": (0x1E44, 6),
    "Mt. Kolts West Face North": (0x1E44, 5),
    "Mt. Zozo East Cavern Middle": (0x1E54, 3),
    "Mt. Zozo East Cavern Right": (0x1E54, 2),
    "Mt. Zozo East Cavern Lower Left": (0x1E54, 5),
    "Mt. Zozo East Cavern Upper": (0x1E54, 4),
    "Mt. Zozo Treasure Slope": (0x1E54, 6),
    "Mt. Zozo Cyan's Room": (0x1E5D, 6),
    "Umaro's Cave Basement 1 Lower Left": (0x1E55, 2),
    "Umaro's Cave Basement 1 Left Central": (0x1E55, 0),
    "Umaro's Cave Basement 2 Lower Left": (0x1E55, 1),
    "Nikeah Inn Clock": (0x1E47, 6),
    "Phantom Train Dining Car": (0x1E46, 7),
    "Phantom Train Third Car Far Left Chest": (0x1E47, 2),
    "Phantom Train Third Car Left Chest": (0x1E5E, 3),
    "Phantom Train Third Car Right Chest": (0x1E47, 3),
    "Phantom Train Third Car Far Right Chest": (0x1E47, 4),
    "Phoenix Cave Lower Cavern East Pool Island": (0x1E56, 0),
    "Phoenix Cave Lower Cavern East Pool Bridge": (0x1E55, 6),
    "Phoenix Cave Lower Cavern Spikes": (0x1E55, 7),
    "Phoenix Cave Lower Cavern Rock Jumping": (0x1E57, 6),
    "Phoenix Cave Lower Cavern Cool Lava": (0x1E55, 3),
    "Phoenix Cave Upper Cavern Spikes": (0x1E55, 5),
    "Phoenix Cave Upper Cavern Hidden Room": (0x1E58, 3),
    "Phoenix Cave Upper Cavern Across Bridge": (0x1E55, 4),
    "Phoenix Cave Upper Cavern Near Red Dragon": (0x1E56, 1),
    "Returners' Hideout Banon's Room": (0x1E46, 0),
    "Returners' Hideout Bedroom": (0x1E45, 2),
    "Returners' Hideout Main Room Pot": (0x1E45, 1),
    "Returners' Hideout North Room Bottom Left": (0x1E45, 6),
    "Returners' Hideout North Room Bottom Right": (0x1E45, 7),
    "Returners' Hideout North Room Upper Left": (0x1E45, 5),
    "Returners' Hideout North Room Bucket": (0x1E45, 3),
    "Returners' Hideout North Room Pot": (0x1E45, 4),
    "Returners' Hideout North Room Secret Room": (0x1E46, 1),
    "Serpent Trench First Branch": (0X1E47, 7),
    "Serpent Trench Second Branch": (0x1E48, 0),
    "South Figaro Basements Hidden Path Entrance": (0x1E44, 0),
    "South Figaro Basements Hidden Path North Left": (0x1E44, 3),
    "South Figaro Basements Hidden Path North Right": (0x1E44, 2),
    "South Figaro Basements Hidden Path South": (0x1E44, 1),
    "South Figaro Basements 2 South": (0x1E5F, 7),
    "South Figaro Basements 2 Northeast": (0x1E5F, 5),
    "South Figaro Basements 2 Hidden Chest": (0x1E5F, 6),
    "South Figaro Old Man's Bucket": (0x1E43, 6),
    "South Figaro Secret Path Clock": (0x1E43, 7),
    "South Figaro Chocobo Stable Box WoB": (0x1E43, 1), #TODO: Fix this address
    "South Figaro Chocobo Stable Barrel WoB": (0x1E43, 0), #TODO: Fix this address
    "South Figaro Shoreline Box WoB": (0x1E5C, 6), #TODO: Fix this address
    "South Figaro Barrel Near Cafe WoB": (0x1E42, 6), #TODO: Fix this address
    "South Figaro Box Near Cafe WoB": (0x1E42, 7), #TODO: Fix this address
    "South Figaro Arsenal Barrel WoB": (0x1E42, 5), #TODO: Fix this address
    "South Figaro Wall Barrel WoB": (0x1E5C, 7), #TODO: Fix this address
    "South Figaro Mansion Exit Barrel WoB": (0x1E42, 4), #TODO: Fix this address
    "South Figaro Chocobo Stable Box WoR": (0x1E43, 1), #TODO: Fix this address
    "South Figaro Chocobo Stable Barrel WoR": (0x1E43, 0), #TODO: Fix this address
    "South Figaro Shoreline Box WoR": (0x1E5C, 6), #TODO: Fix this address
    "South Figaro Barrel Near Cafe WoR": (0x1E42, 6), #TODO: Fix this address
    "South Figaro Box Near Cafe WoR": (0x1E42, 7), #TODO: Fix this address
    "South Figaro Arsenal Barrel WoR": (0x1E42, 5), #TODO: Fix this address
    "South Figaro Wall Barrel WoR": (0x1E5C, 7), #TODO: Fix this address
    "South Figaro Mansion Exit Barrel": (0x1E42, 4), #TODO: Fix this address
    "South Figaro Mansion Basement West Cell": (0x1E5F, 4),
    "South Figaro Mansion Basement East Cell": (0x1E60, 0),
    "South Figaro Mansion Basement East Room Left": (0x1E43, 2),
    "South Figaro Mansion Basement East Room Below Clock": (0x1E43, 4),
    "South Figaro Mansion Basement East Room Right": (0x1E43, 3),
    "South Figaro Mansion Basement East Room Far Right": (0x1E43, 5),
    "South Figaro Cave Eastern Passage WoB": (0x1E4C, 1), #TODO: Fix this address
    "South Figaro Cave Southwest Passage WoB": (0x1E42, 2), #TODO: Fix this address
    "South Figaro Cave Eastern Bridge WoB": (0x1E42, 3), #TODO: Fix this address
    "South Figaro Cave Eastern Passage WoR": (0x1E4C, 1), #TODO: Fix this address
    "South Figaro Cave Southwest Passage WoR": (0x1E42, 2), #TODO: Fix this address
    "South Figaro Cave Eastern Bridge WoR": (0x1E42, 3), #TODO: Fix this address
    "Thamasa Strago's House Near Table": (0x1E5C, 3),
    "Thamasa Item Shop Barrel": (0x1E5F, 1),
    "Thamasa Relic Shop Barrel": (0x1E5F, 0),
    "Thamasa Inn Barrel": (0x1E5F, 2),
    "Thamasa Strago's House Barrel": (0x1E5E, 7),
    "Thamasa Elder's House Barrel": (0x1E5E, 6),
    "Burning House First Chest": (0x1E4D, 0),
    "Burning House Second Chest": (0x1E4D, 1),
    "Collapsing House First Floor Top Right": (0x1E51, 6),
    "Collapsing House First Floor Middle": (0x1E52, 1),
    "Collapsing House First Floor Top Left": (0x1E51, 7),
    "Collapsing House First Floor Left": (0x1E52, 0),
    "Collapsing House First Floor Bottom Left": (0x1E52, 2),
    "Collapsing House Basement Bottom": (0x1E52, 5),
    "Collapsing House Basement Left": (0x1E52, 4),
    "Collapsing House Basement Right": (0x1E52, 3),
    "Veldt Cave North Upper Left": (0x1E57, 7),
    "Veldt Cave North Hidden Room": (0x1E58, 0),
    "Veldt Cave South Lower Left": (0x1E58, 1),
    "Zone Eater Crusher Room Right": (0x1E5D, 0),
    "Zone Eater Crusher Room Middle": (0x1E5D, 1),
    "Zone Eater Crusher Room Left": (0x1E5D, 2),
    "Zone Eater Jumping Room": (0x1E5C, 4),
    "Zone Eater Lower Cavern Left": (0x1E58, 2),
    "Zone Eater Lower Cavern Right": (0x1E5A, 1),
    "Zone Eater Triple Bridge Right": (0x1E5D, 5),
    "Zone Eater Triple Bridge Middle": (0x1E5D, 4),
    "Zone Eater Triple Bridge Left": (0x1E5A, 0),
    "Zozo Armor Shop": (0x1E49, 0),
    "Zozo Cafe": (0x1E49, 2),
    "Zozo Clock Puzzle": (0x1E49, 1),
    "Zozo Relic Shop Seventh Floor": (0x1E49, 3),
    "Zozo West Tower North Left Pot": (0x1E5D, 7),
    "Zozo West Tower North Right Pot": (0x1E5E, 0),
    "Zozo Relic Shop Thirteenth Floor": (0x1E49, 4),
    "Zozo Esper Room Left": (0x1E48, 6),
    "Zozo Esper Room Right": (0x1E48, 7)
}

item_ingame_ids = {
    'ValiantKnife': 9,
    'Illumina': 26,
    'Ragnarok Sword': 27,
    'Pearl Lance': 33,
    'Aura Lance': 35,
    'Magus Rod': 60,
    'Fixed Dice': 82,
    'Aegis Shld': 94,
    'Flame Shld': 96,
    'Ice Shld': 97,
    'Thunder Shld': 98,
    'Genji Shld': 100,
    'Paladin Shld': 103,
    'Force Shld': 104,
    'Red Cap': 120,
    'Cat Hood': 128,
    'Genji Helmet': 129,
    'Force Armor': 148,
    'Genji Armor': 154,
    'Minerva': 156,
    'BehemothSuit': 161,
    'Snow Muffler': 162,
    'Economizer': 206,
    'Genji Glove': 209,
    'Offering': 211,
    'Gem Box': 216,
    'Dragon Horn': 217,
    'Marvel Shoes': 224,
    'Exp. Egg': 228,
    'ArchplgoItem': 231
}


class FF6WCDeltaPatch(APDeltaPatch):
    hash = NA10HASH
    game = "Final Fantasy 6 Worlds Collide"
    patch_file_ending = ".apff6wc"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()


def get_base_rom_bytes(file_name: str = "") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(open(file_name, "rb").read())

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        if NA10HASH != basemd5.hexdigest():
            raise Exception('Supplied Base Rom does not match known MD5 for NA (1.0) release. '
                            'Get the correct game and version, then dump it')
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes


def get_base_rom_path(file_name: str = "") -> str:
    options = Utils.get_options()
    if not file_name:
        file_name = options["ff6wc_options"]["rom_file"]
    if not os.path.exists(file_name):
        file_name = Utils.local_path(file_name)
    return file_name


def get_event_flag_value(event_id):
    event_byte = event_flag_base_address + (event_id // 8)
    event_bit = event_id % 8
    hbyte = hex(event_byte)
    bbyte = bin(event_byte)
    hbit = hex(bit_positions[event_bit])
    bbit = bin(bit_positions[event_bit])
    return event_byte, bit_positions[event_bit]


def get_obtained_esper_bit(esper_name):
    esper_index = esper_name
    esper_byte = esper_bit_base_address + (esper_index // 8)
    esper_bit = esper_index % 8
    return esper_byte, bit_positions[esper_bit]


def add_esper(initial, esper_name):
    byte, bit = get_obtained_esper_bit(esper_name)
    return initial | bit


def get_character_bit(character, address):
    character_index = character
    character_byte = address + character_index // 8
    character_bit = character_index % 8
    return character_byte, bit_positions[character_bit]


def get_character_initialized_bit(character_name):
    return get_character_bit(character_name, character_intialized_bit_base_address)


def get_character_recruited_bit(character_name):
    return get_character_bit(character_name, character_recruited_bit_base_address)
