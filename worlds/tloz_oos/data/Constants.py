VERSION = "0.9e"

COMPANIONS = [
    "Ricky",
    "Moosh",
    "Dimitri"
]

SEASONS = [
    "spring",
    "summer",
    "autumn",
    "winter"
]

DIRECTIONS = [
    "up",
    "right",
    "down",
    "left"
]

SEASON_ITEMS = {
    "winter": "Rod of Seasons (Winter)",
    "summer": "Rod of Seasons (Summer)",
    "spring": "Rod of Seasons (Spring)",
    "autumn": "Rod of Seasons (Autumn)",
}

SEED_ITEMS = [
    "Ember Seeds",
    "Scent Seeds",
    "Pegasus Seeds",
    "Mystery Seeds",
    "Gale Seeds"
]

DUNGEON_NAMES = [
    "Hero's Cave",
    "Gnarled Root Dungeon",
    "Snake's Remains",
    "Poison Moth's Lair",
    "Dancing Dragon Dungeon",
    "Unicorn's Cave",
    "Ancient Ruins",
    "Explorer's Crypt",
    "Sword & Shield Dungeon"
]

REGIONS_CONVERSION_TABLE = {
    "EYEGLASS_LAKE": "north horon",
    "NORTH_HORON": "holodrum plain",
    "EASTERN_SUBURBS": "eastern suburbs",
    "WOODS_OF_WINTER": "woods of winter",
    "SUNKEN_CITY": "sunken city",
    "WESTERN_COAST": "western coast",
    "SPOOL_SWAMP": "spool swamp",
    "TEMPLE_REMAINS": "temple remains",
    "LOST_WOODS": "lost woods",
    "TARM_RUINS": "tarm ruins",
    "HORON_VILLAGE": "horon village"
}

PORTALS_CONVERSION_TABLE = {
    "eastern suburbs portal": "eastern suburbs",
    "eyeglass lake portal": "eyeglass lake",
    "horon village portal": "horon village",
    "mt. cucco portal": "mt. cucco",
    "spool swamp portal": "spool swamp",
    "temple remains lower portal": "temple remains lower",
    "temple remains upper portal": "temple remains upper",

    "subrosia portal 1": "volcanoes east",
    "subrosia portal 2": "subrosia market",
    "subrosia portal 3": "strange brothers",
    "subrosia portal 4": "house of pirates",
    "subrosia portal 5": "great furnace",
    "subrosia portal 6": "volcanoes west",
    "subrosia portal 7": "d8 entrance",
}

ESSENCES = [
    "Fertile Soil",
    "Gift of Time",
    "Bright Sun",
    "Soothing Rain",
    "Nurturing Warmth",
    "Blowing Wind",
    "Seed of Life",
    "Changing Seasons",
]

DUNGEON_ITEMS = [
    "Small Key",
    "Boss Key",
    "Compass",
    "Dungeon Map"
]

VALID_RUPEE_VALUES = [
    0, 1, 2, 5, 10, 20, 25, 30, 40, 50, 60, 70, 80, 100, 200, 300, 400, 500, 900, 999
]

ITEM_GROUPS = {
    "Dungeon Items": [
        "Small Key (Hero's Cave)",
        "Small Key (Gnarled Root Dungeon)",
        "Small Key (Snake's Remains)",
        "Small Key (Poison Moth's Lair)",
        "Small Key (Dancing Dragon Dungeon)",
        "Small Key (Unicorn's Cave)",
        "Small Key (Ancient Ruins)",
        "Small Key (Explorer's Crypt)",
        "Small Key (Sword & Shield Dungeon)",

        "Boss Key (Gnarled Root Dungeon)",
        "Boss Key (Snake's Remains)",
        "Boss Key (Poison Moth's Lair)",
        "Boss Key (Dancing Dragon Dungeon)",
        "Boss Key (Unicorn's Cave)",
        "Boss Key (Ancient Ruins)",
        "Boss Key (Explorer's Crypt)",
        "Boss Key (Sword & Shield Dungeon)",

        "Compass (Gnarled Root Dungeon)",
        "Compass (Snake's Remains)",
        "Compass (Poison Moth's Lair)",
        "Compass (Dancing Dragon Dungeon)",
        "Compass (Unicorn's Cave)",
        "Compass (Ancient Ruins)",
        "Compass (Explorer's Crypt)",
        "Compass (Sword & Shield Dungeon)",

        "Dungeon Map (Gnarled Root Dungeon)",
        "Dungeon Map (Snake's Remains)",
        "Dungeon Map (Poison Moth's Lair)",
        "Dungeon Map (Dancing Dragon Dungeon)",
        "Dungeon Map (Unicorn's Cave)",
        "Dungeon Map (Ancient Ruins)",
        "Dungeon Map (Explorer's Crypt)",
        "Dungeon Map (Sword & Shield Dungeon)"
    ],
}

LOCATION_GROUPS = {
    "D0": [
        "d0 key chest",
        "d0 sword chest",
        "d0 hidden 2d section",
        "d0 rupee chest"
    ],
    "D1": [
        "d1 stalfos drop",
        "d1 basement",
        "d1 block-pushing room",
        "d1 railway chest",
        "d1 floormaster room",
        "d1 lever room",
        "d1 stalfos chest",
        "d1 button chest",
        "d1 goriya chest",
        "d1 boss"
    ],
    "D2": [
        "d2 rope drop",
        "d2 moblin chest",
        "d2 roller chest",
        "d2 left from entrance",
        "d2 pot chest",
        "d2 rope chest",
        "d2 blade chest",
        "d2 spiral chest",
        "d2 terrace chest",
        "d2 boss"
    ],
    "D3": [
        "d3 roller chest",
        "d3 mimic chest",
        "d3 zol chest",
        "d3 water room",
        "d3 quicksand terrace",
        "d3 moldorm chest",
        "d3 trampoline chest",
        "d3 bombed wall chest",
        "d3 giant blade room",
        "d3 boss"
    ],
    "D4": [
        "d4 pot puzzle",
        "d4 north of entrance",
        "d4 maze chest",
        "d4 dark room",
        "d4 water ring room",
        "d4 pool",
        "d4 terrace",
        "d4 torch chest",
        "d4 cracked floor room",
        "d4 dive spot",
        "d4 boss"
    ],
    "D5": [
        "d5 cart chest",
        "d5 left chest",
        "d5 magnet ball chest",
        "d5 terrace chest",
        "d5 armos chest",
        "d5 gibdo/zol chest",
        "d5 spiral chest",
        "d5 spinner chest",
        "d5 stalfos room",
        "d5 basement",
        "d5 boss"
    ],
    "D6": [
        "d6 magnet ball drop",
        "d6 spinner north",
        "d6 armos hall",
        "d6 crystal trap room",
        "d6 1F east",
        "d6 2F gibdo chest",
        "d6 2F armos chest",
        "d6 beamos room",
        "d6 1F terrace",
        "d6 escape room",
        "d6 vire chest",
        "d6 boss"
    ],
    "D7": [
        "d7 wizzrobe chest",
        "d7 spike chest",
        "d7 maze chest",
        "d7 right of entrance",
        "d7 bombed wall chest",
        "d7 zol button",
        "d7 armos puzzle",
        "d7 magunesu chest",
        "d7 quicksand chest",
        "d7 B2F drop",
        "d7 stalfos chest",
        "d7 boss"
    ],
    "D8": [
        "d8 eye drop",
        "d8 three eyes chest",
        "d8 hardhat drop",
        "d8 spike room",
        "d8 spinner chest",
        "d8 armos chest",
        "d8 magnet ball room",
        "d8 darknut chest",
        "d8 pols voice chest",
        "d8 ghost armos drop",
        "d8 SE lava chest",
        "d8 SW lava chest",
        "d8 spark chest",
        "d8 boss"
    ],
    "Trade Sequence": [
        "dr. left reward",
        "malon trade",
        # "maple trade",
        "mrs. ruul trade",
        "subrosian chef trade",
        "biggoron trade",
        "ingo trade",
        "old man trade",
        "talon trade",
        "syrup trade",
        "tick tock trade",
        "guru-guru trade"
    ],
}
