from BaseClasses import ItemClassification

BASE_ITEM_ID = 1000000  # TODO: Change

ITEMS_DATA = {
    #   "No Item": {
    #   'classification': ItemClassification.filler,
    #   "",
    #    'id': 0x00,
    #    'subid': 0x00
    #    },
    "Wooden Shield": {
        'classification': ItemClassification.useful,
        'id': 0x01
    },
    "Iron Shield": {
        'classification': ItemClassification.useful,
        'id': 0x01,
        'subid': 0x01
    },
    "Bombs (10)": {
        'classification': ItemClassification.progression,
        'id': 0x03
    },
    "Progressive Sword": {
        'classification': ItemClassification.progression,
        'id': 0x05
    },
    "Progressive Boomerang": {
        'classification': ItemClassification.progression,
        'id': 0x06
    },
    "Rod of Seasons (Spring)": {
        'classification': ItemClassification.progression,
        'id': 0x07,
        'subid': 0x02
    },
    "Rod of Seasons (Summer)": {
        'classification': ItemClassification.progression,
        'id': 0x07,
        'subid': 0x03
    },
    "Rod of Seasons (Autumn)": {
        'classification': ItemClassification.progression,
        'id': 0x07,
        'subid': 0x04
    },
    "Rod of Seasons (Winter)": {
        'classification': ItemClassification.progression,
        'id': 0x07,
        'subid': 0x05
    },
    "Magnet Gloves": {
        'classification': ItemClassification.progression,
        'id': 0x08
    },
    "Biggoron's Sword": {
        'classification': ItemClassification.useful,
        'id': 0x0c
    },
    #   "Bombchus (10)": {
    #       'classification': ItemClassification.progression,
    #       'id': 0x0d
    #   },
    "Flute": {
        'classification': ItemClassification.progression,
        'id': 0x0e
    },
    "Progressive Slingshot": {
        'classification': ItemClassification.progression,
        'id': 0x13
    },
    "Shovel": {
        'classification': ItemClassification.progression,
        'id': 0x15
    },
    "Bracelet": {
        'classification': ItemClassification.progression,
        'id': 0x16
    },
    "Progressive Feather": {
        'classification': ItemClassification.progression,
        'id': 0x17
    },
    "Seed Satchel": {
        'classification': ItemClassification.progression,
        'id': 0x19
    },
    "Fool's Ore": {
        'classification': ItemClassification.useful,
        'id': 0x1e
    },
    "Ember Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x20
    },
    "Scent Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x21
    },
    "Pegasus Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x22
    },
    "Gale Seeds": {
        'classification': ItemClassification.useful,
        'id': 0x23
    },
    "Mystery Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x24
    },
    "Rupees (1)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x00
    },
    "Rupees (5)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x01
    },
    "Rupees (10)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x02
    },
    "Rupees (20)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x03
    },
    "Rupees (30)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x04
    },
    "Rupees (50)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x05
    },
    "Rupees (100)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x06
    },
    "Heart Container": {
        'classification': ItemClassification.useful,
        'id': 0x2a
    },
    "Piece of Heart": {
        'classification': ItemClassification.useful,
        'id': 0x2b,
        'subid': 0x01
    },
    "Rare Peach Stone": {
        'classification': ItemClassification.useful,
        'id': 0x2b,
        'subid': 0x02
    },

    # TODO: Handle rings
    "Discovery Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x04
    },
    "Power Ring L-1": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x0e
    },
    "Moblin Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x05
    },
    "Steadfast Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x06
    },
    "Blast Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x07
    },
    "Rang Ring L-1": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x08
    },
    "Octo Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x09
    },
    "Quicksand Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x0a
    },
    "Armor Ring L-2": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x0b
    },
    "Subrosian Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x10
    },
    "Green Joy Ring": {
        'classification': ItemClassification.useful,
        'id': 0x2d,
        'subid': 0x11
    },


    "Flippers": {
        'classification': ItemClassification.progression,
        'id': 0x2e
    },
    "Potion": {
        'classification': ItemClassification.useful,
        'id': 0x2f
    },

    "Small Key (Hero's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x00
    },
    "Small Key (Gnarled Root Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x01
    },
    "Small Key (Snake's Remains)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x02
    },
    "Small Key (Poison Moth's Lair)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x03
    },
    "Small Key (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x04
    },
    "Small Key (Unicorn's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x05
    },
    "Small Key (Ancient Ruins)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x06
    },
    "Small Key (Explorer's Crypt)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x07
    },
    "Small Key (Sword & Shield Maze)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x07
    },
    "Boss Key (Gnarled Root Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x01
    },
    "Boss Key (Snake's Remains)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x02
    },
    "Boss Key (Poison Moth's Lair)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x03
    },
    "Boss Key (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x04
    },
    "Boss Key (Unicorn's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x05
    },
    "Boss Key (Ancient Ruins)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x06
    },
    "Boss Key (Explorer's Crypt)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x07
    },
    "Boss Key (Sword & Shield Maze)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x08
    },
    "Compass (Gnarled Root Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x01
    },
    "Compass (Snake's Remains)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x02
    },
    "Compass (Poison Moth's Lair)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x03
    },
    "Compass (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x04
    },
    "Compass (Unicorn's Cave)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x05
    },
    "Compass (Ancient Ruins)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x06
    },
    "Compass (Explorer's Crypt)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x07
    },
    "Compass (Sword & Shield Maze)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x08
    },
    "Dungeon Map (Gnarled Root Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x01
    },
    "Dungeon Map (Snake's Remains)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x02
    },
    "Dungeon Map (Poison Moth's Lair)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x03
    },
    "Dungeon Map (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x04
    },
    "Dungeon Map (Unicorn's Cave)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x05
    },
    "Dungeon Map (Ancient Ruins)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x06
    },
    "Dungeon Map (Explorer's Crypt)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x07
    },
    "Dungeon Map (Sword & Shield Maze)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x08
    },

    "Gasha Seed": {
        'classification': ItemClassification.filler,
        'id': 0x34,
        'subid': 0x01
    },
    
    #     "Maku Seed": {
    #           'classification': ItemClassification.progression,
    #         'id': 0x36
    #     },
    #     "Ore Chunks": {
    #     'classification': ItemClassification.filler,
    #     "",
    #         'id': 0x37
    #     },
    #     "Essence": {
    #     'classification': ItemClassification.progression,
    #     "",
    #         'id': 0x40
    #     },

    "Cuccodex": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x00
    },
    "Lon Lon Egg": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x01
    },
    "Ghastly Doll": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x02
    },
    "Iron Pot": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x03
    },
    "Lava Soup": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x04
    },
    "Goron Vase": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x05
    },
    "Fish": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x06
    },
    "Megaphone": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x07
    },
    "Mushroom": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x08
    },
    "Wooden Bird": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x09
    },
    "Engine Grease": {
        'classification': ItemClassification.progression,
        'id': 0x41
    },
    "Phonograph": {
         'classification': ItemClassification.progression,
         'id': 0x41,
    },

    "Gnarled Key": {
        'classification': ItemClassification.progression,
        'id': 0x42
    },
    "Floodgate Key": {
        'classification': ItemClassification.progression,
        'id': 0x43
    },
    "Dragon Key": {
        'classification': ItemClassification.progression,
        'id': 0x44
    },
    "Star Ore": {
        'classification': ItemClassification.progression,
        'id': 0x45
    },
    "Ribbon": {
        'classification': ItemClassification.progression,
        'id': 0x46
    },
    "Spring Banana": {
        'classification': ItemClassification.progression,
        'id': 0x47
    },
    #   "ricky's gloves": {
    #       'classification': ItemClassification.progression,
    #       'pretty_name': "Ricky's Gloves",
    #       'id': 0x48
    #   },
    #   "Bomb Flower": {
    #   'classification': ItemClassification.progression,
    #   "",
    #        'id': 0x49
    #    },
    "Rusty Bell": {
        'classification': ItemClassification.progression,
        'id': 0x4a
    },
    "Treasure Map": {
        'classification': ItemClassification.useful,
        'id': 0x4b
    },
    "Round Jewel": {
        'classification': ItemClassification.progression,
        'id': 0x4c
    },
    "Pyramid Jewel": {
        'classification': ItemClassification.progression,
        'id': 0x4d
    },
    "Square Jewel": {
        'classification': ItemClassification.progression,
        'id': 0x4e
    },
    "X-Shaped Jewel": {
        'classification': ItemClassification.progression,
        'id': 0x4f
    },
    "Red Ore": {
        'classification': ItemClassification.progression,
        'id': 0x50
    },
    "Blue Ore": {
        'classification': ItemClassification.progression,
        'id': 0x51
    },
    "Hard Ore": {
        'classification': ItemClassification.progression,
        'id': 0x52
    },
    "Member's Card": {
        'classification': ItemClassification.progression,
        'id': 0x53
    },
    "Master's Plaque": {
        'classification': ItemClassification.progression,
        'id': 0x54
    },
    #   "Bomb Upgrade": {
    #   'classification': ItemClassification.progression,
    #   "",
    #        'id': 0x61
    #    },
    #   "Satchel Upgrade": {
    #   'classification': ItemClassification.progression,
    #   "",
    #        'id': 0x62)
}
