
BASE_LOCATION_ID = 27022001000

LOCATIONS_DATA = {
    "eyeglass lake, across bridge": {
        "region_id": "eyeglass lake, across bridge",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC7B8
    },
    "maku tree": {
        "region_id": "maku tree",
        "vanilla_item": "Gnarled Key",
        "flag_byte": [0xC80B, 0xC80C, 0xC82B, 0xC82C, 0xC82D, 0xC85B, 0xC85C, 0xC85D, 0xC87B]
        # Maku Tree has several rooms depending on the amount of essences owned
    },
    "horon village SW chest": {
        "region_id": "horon village SW chest",
        "vanilla_item": "Rupees (20)",
        "flag_byte": 0xC7F5
    },
    "horon village SE chest": {
        "region_id": "horon village SE chest",
        "vanilla_item": "Rupees (20)",
        "flag_byte": 0xC7F9
    },
    "holly's house": {
        "region_id": "holly's house",
        "vanilla_item": "Shovel",
        "flag_byte": 0xC8A3
    },
    "chest on top of D2": {
        "region_id": "d2 roof",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC78E
    },
    "blaino prize": {
        "region_id": "blaino prize",
        "vanilla_item": "Ricky's Gloves",
        "flag_byte": 0xC8B4
    },
    "underwater item below natzu bridge": {
        "region_id": "underwater item below natzu bridge",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC766
    },
    "spool swamp digging spot": {
        "region_id": "spool swamp digging spot",
        "vanilla_item": "Rupees (50)",  # Random ring in vanilla, but this doesn't exist in rando
        "flag_byte": 0xC782
    },
    "floodgate keeper's house": {
        "region_id": "floodgate keeper's house",
        "vanilla_item": "Floodgate Key",
        "flag_byte": 0xC8B5
    },
    "spool swamp cave": {
        "region_id": "spool swamp cave",
        "vanilla_item": "Square Jewel",
        "flag_byte": 0xC9FA
    },
    "moblin keep": {
        "region_id": "moblin keep",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC75B
    },
    "master diver's challenge": {
        "region_id": "master diver's challenge",
        "vanilla_item": "Master's Plaque",
        "flag_byte": 0xCABC
    },
    "master diver's reward": {
        "region_id": "master diver's reward",
        "vanilla_item": "Flippers",
        "flag_byte": 0xCABD,
        "bit_mask": 0x80
    },
    "chest in master diver's cave": {
        "region_id": "chest in master diver's cave",
        "vanilla_item": "Rupees (50)",
        "flag_byte": 0xCABD
    },
    "spring banana tree": {
        "region_id": "spring banana tree",
        "vanilla_item": "Spring Banana",
        "flag_byte": 0xC70F
    },
    "goron mountain, across pits": {
        "region_id": "goron mountain, across pits",
        "vanilla_item": "Dragon Key",
        "flag_byte": 0xC71A
    },
    "mt. cucco, platform cave": {
        "region_id": "mt. cucco, platform cave",
        "vanilla_item": "Green Joy Ring",
        "flag_byte": 0xCABB
    },
    "diving spot outside D4": {
        "region_id": "diving spot outside D4",
        "vanilla_item": "Pyramid Jewel",
        "flag_byte": 0xCAE5,
    },
    "black beast's chest": {
        "region_id": "black beast's chest",
        "vanilla_item": "X-Shaped Jewel",
        "flag_byte": 0xC7F4
    },
    "old man in treehouse": {
        "region_id": "old man in treehouse",
        "vanilla_item": "Round Jewel",
        "flag_byte": 0xC894
    },
    "lost woods": {
        "region_id": "lost woods",
        "vanilla_item": "Progressive Sword",
        "flag_byte": 0xC7C9,
    },
    "samasa desert pit": {
        "region_id": "samasa desert pit",
        "vanilla_item": "Rusty Bell",
        "flag_byte": 0xCAD2
    },
    "samasa desert chest": {
        "region_id": "samasa desert chest",
        "vanilla_item": "Rang Ring L-1",
        "flag_byte": 0xC7FF
    },
    "western coast, beach chest": {
        "region_id": "western coast after ship",
        "vanilla_item": "Blast Ring",
        "flag_byte": 0xC7E3
    },
    "western coast, in house": {
        "region_id": "western coast after ship",
        "vanilla_item": "Bombs (10)",
        "flag_byte": 0xC888
    },
    "cave south of mrs. ruul": {
        "region_id": "cave south of mrs. ruul",
        "vanilla_item": "Octo Ring",
        "flag_byte": 0xC9E0
    },
    "cave north of D1": {
        "region_id": "cave north of D1",
        "vanilla_item": "Quicksand Ring",
        "flag_byte": 0xC9E1
    },
    "cave outside D2": {
        "region_id": "cave outside D2",
        "vanilla_item": "Moblin Ring",
        "flag_byte": 0xCAB3
    },
    "woods of winter, 1st cave": {
        "region_id": "woods of winter, 1st cave",
        "vanilla_item": "Rupees (30)",
        "flag_byte": 0xCAB4
    },
    "sunken city, summer cave": {
        "region_id": "sunken city, summer cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xCAB5
    },
    "dry eyeglass lake, east cave": {
        "region_id": "dry eyeglass lake, east cave",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xCAC0
    },
    "chest in goron mountain": {
        "region_id": "chest in goron mountain",
        "vanilla_item": "Armor Ring L-2",
        "flag_byte": 0xCAC8
    },
    "natzu region, across water": {
        "region_id": "natzu region, across water",
        "vanilla_item": "Rupees (50)",
        "flag_byte": 0xCA0E
    },
    "mt. cucco, talon's cave": {
        "region_id": "mt. cucco, talon's cave",
        "vanilla_item": "Subrosian Ring",
        "flag_byte": 0xCAB6,
        "bit_mask": 0x60  # 0x60 is needed here to ensure we're not sending Talon's wakeup item as a false positive
    },
    "tarm ruins, under tree": {
        "region_id": "tarm ruins, under tree",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC89B
    },
    "eastern suburbs spring cave": {
        "region_id": "eastern suburbs spring cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC9F7
    },
    "dry eyeglass lake, west cave": {
        "region_id": "dry eyeglass lake, west cave",
        "vanilla_item": "Rupees (100)",
        "flag_byte": 0xC9FB
    },
    "woods of winter, 2nd cave": {
        "region_id": "woods of winter, 2nd cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xCA12
    },
    "shop, 20 rupees": {
        "region_id": "shop, 20 rupees",
        "vanilla_item": "Bombs (10)",
        "randomized": False
    },
    "shop, 30 rupees": {
        "region_id": "shop, 30 rupees",
        "vanilla_item": "Progressive Shield",
        "randomized": False
    },
    "shop, 150 rupees": {
        "region_id": "shop, 150 rupees",
        "vanilla_item": "Flute",
        "flag_byte": 0xC693,
        "bit_mask": 0x80
    },
    "member's shop 1": {
        "region_id": "member's shop",
        "vanilla_item": "Seed Satchel",
        "flag_byte": 0xC63F,
        "bit_mask": 0x01,
    },
    "member's shop 2": {
        "region_id": "member's shop",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC63F,
        "bit_mask": 0x02,
    },
    "member's shop 3": {
        "region_id": "member's shop",
        "vanilla_item": "Treasure Map",
        "flag_byte": 0xC63F,
        "bit_mask": 0x08,
    },

    "tower of winter": {
        "region_id": "tower of winter",
        "vanilla_item": "Rod of Seasons (Winter)",
        "flag_byte": 0xCAF2
    },
    "tower of summer": {
        "region_id": "tower of summer",
        "vanilla_item": "Rod of Seasons (Summer)",
        "flag_byte": 0xCAF8
    },
    "tower of spring": {
        "region_id": "tower of spring",
        "vanilla_item": "Rod of Seasons (Spring)",
        "flag_byte": 0xCAF5
    },
    "tower of autumn": {
        "region_id": "tower of autumn",
        "vanilla_item": "Rod of Seasons (Autumn)",
        "flag_byte": 0xCAFB
    },
    "subrosian dance hall": {
        "region_id": "subrosian dance hall",
        "vanilla_item": "Progressive Boomerang",
        "flag_byte": 0xC895
    },
    "temple of seasons": {
        "region_id": "temple of seasons",
        "vanilla_item": "Rod of Seasons",
        "flag_byte": 0xC8AC
    },
    "subrosia seaside": {
        "region_id": "subrosia seaside",
        "vanilla_item": "Star Ore",
        "flag_byte": [0xC865, 0xC866, 0xC875, 0xC876]
    },
    "subrosian wilds chest": {
        "region_id": "subrosian wilds chest",
        "vanilla_item": "Blue Ore",
        "flag_byte": 0xC841
    },
    "subrosian wilds digging spot": {
        "region_id": "subrosian wilds digging spot",
        "vanilla_item": "Rupees (50)",  # Random ring in vanilla, but this doesn't exist in rando
        "flag_byte": 0xC840
    },
    "subrosia village chest": {
        "region_id": "subrosia village chest",
        "vanilla_item": "Red Ore",
        "flag_byte": 0xC858
    },
    "subrosia, open cave": {
        "region_id": "subrosia, open cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC9F1
    },
    "subrosia, locked cave": {
        "region_id": "subrosia, locked cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xCAC6
    },
    "subrosia market, 1st item": {
        "region_id": "subrosia market, 1st item",
        "vanilla_item": "Ribbon",
        "flag_byte": 0xC642,
        "bit_mask": 0x01,
    },
    "subrosia market, 2nd item": {
        "region_id": "subrosia market, 2nd item",
        "vanilla_item": "Rare Peach Stone",
        "flag_byte": 0xC642,
        "bit_mask": 0x02,
    },
    "subrosia market, 5th item": {
        "region_id": "subrosia market, 5th item",
        "vanilla_item": "Member's Card",
        "flag_byte": 0xC694,
        "bit_mask": 0x01
    },
    "great furnace": {
        "region_id": "great furnace",
        "vanilla_item": "Hard Ore",
        "flag_byte": 0xC88E
    },
    "subrosian smithy ore": {
        "region_id": "subrosian smithy ore",
        "vanilla_item": "Progressive Shield",
        "flag_byte": 0xC897,
        "bit_mask": 0x40
    },
    # "subrosian smithy bell": {
    #     "region_id": "subrosian smithy bell",
    #     "vanilla_item": "pirate's bell",
    #     "randomized": False,
    #     "flag_byte": 0xC897,
    #     "local": True
    # },

    "d0 key chest": {
        "region_id": "d0 key chest",
        "vanilla_item": "Small Key (Hero's Cave)",
        "dungeon": 0,
        "flag_byte": 0xC903
    },
    "d0 sword chest": {
        "region_id": "d0 sword chest",
        "vanilla_item": "Progressive Sword",
        "dungeon": 0,
        "flag_byte": 0xC906
    },
    "d0 hidden 2d section": {
        "region_id": "d0 hidden 2d section",
        "vanilla_item": "Gasha Seed",
        "dungeon": 0,
        "flag_byte": 0xC901
    },
    "d0 rupee chest": {
        "region_id": "d0 rupee chest",
        "vanilla_item": "Rupees (30)",
        "dungeon": 0,
        "flag_byte": 0xC905
    },

    "d1 stalfos drop": {
        "region_id": "d1 stalfos drop",
        "vanilla_item": "Small Key (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC91B
    },
    "d1 basement": {
        "region_id": "d1 basement",
        "vanilla_item": "Seed Satchel",
        "dungeon": 1,
        "flag_byte": 0xC909
    },
    "d1 block-pushing room": {
        "region_id": "d1 block-pushing room",
        "vanilla_item": "Gasha Seed",
        "dungeon": 1,
        "flag_byte": 0xC90D
    },
    "d1 railway chest": {
        "region_id": "d1 railway chest",
        "vanilla_item": "Bombs (10)",
        "dungeon": 1,
        "flag_byte": 0xC910
    },
    "d1 floormaster room": {
        "region_id": "d1 floormaster room",
        "vanilla_item": "Discovery Ring",
        "dungeon": 1,
        "flag_byte": 0xC917
    },
    "d1 lever room": {
        "region_id": "d1 lever room",
        "vanilla_item": "Compass (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC90F
    },
    "d1 stalfos chest": {
        "region_id": "d1 stalfos chest",
        "vanilla_item": "Dungeon Map (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC919
    },
    "d1 button chest": {
        "region_id": "d1 button chest",
        "vanilla_item": "Small Key (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC911
    },
    "d1 goriya chest": {
        "region_id": "d1 goriya chest",
        "vanilla_item": "Boss Key (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC914
    },
    "d1 boss": {
        "region_id": "d1 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 1,
        "flag_byte": 0xC912
    },
    # Essence is 0xC913

    "d2 rope drop": {
        "region_id": "d2 rope drop",
        "vanilla_item": "Small Key (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC934
    },
    "d2 moblin chest": {
        "region_id": "d2 moblin chest",
        "vanilla_item": "Bracelet",
        "dungeon": 2,
        "flag_byte": 0xC92A
    },
    "d2 roller chest": {
        "region_id": "d2 roller chest",
        "vanilla_item": "Rupees (10)",
        "dungeon": 2,
        "flag_byte": 0xC91F
    },
    "d2 left from entrance": {
        "region_id": "d2 left from entrance",
        "vanilla_item": "Rupees (5)",
        "dungeon": 2,
        "flag_byte": 0xC938
    },
    "d2 pot chest": {
        "region_id": "d2 pot chest",
        "vanilla_item": "Dungeon Map (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC92B
    },
    "d2 rope chest": {
        "region_id": "d2 rope chest",
        "vanilla_item": "Compass (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC936
    },
    "d2 blade chest": {
        "region_id": "d2 blade chest",
        "vanilla_item": "Small Key (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC931
    },
    "d2 spiral chest": {
        "region_id": "d2 spiral chest",
        "vanilla_item": "Small Key (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC92D
    },
    "d2 terrace chest": {
        "region_id": "d2 terrace chest",
        "vanilla_item": "Boss Key (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC924
    },
    "d2 boss": {
        "region_id": "d2 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 2,
        "flag_byte": 0xC929
    },
    # Essence is 0xC92C

    "d3 roller chest": {
        "region_id": "d3 roller chest",
        "vanilla_item": "Small Key (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC94C
    },
    "d3 mimic chest": {
        "region_id": "d3 mimic chest",
        "vanilla_item": "Progressive Feather",
        "dungeon": 3,
        "flag_byte": 0xC950
    },
    "d3 zol chest": {
        "region_id": "d3 zol chest",
        "vanilla_item": "Small Key (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC94F
    },
    "d3 water room": {
        "region_id": "d3 water room",
        "vanilla_item": "Rupees (30)",
        "dungeon": 3,
        "flag_byte": 0xC941
    },
    "d3 quicksand terrace": {
        "region_id": "d3 quicksand terrace",
        "vanilla_item": "Gasha Seed",
        "dungeon": 3,
        "flag_byte": 0xC944
    },
    "d3 moldorm chest": {
        "region_id": "d3 moldorm chest",
        "vanilla_item": "Bombs (10)",
        "dungeon": 3,
        "flag_byte": 0xC954
    },
    "d3 trampoline chest": {
        "region_id": "d3 trampoline chest",
        "vanilla_item": "Compass (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC94D
    },
    "d3 bombed wall chest": {
        "region_id": "d3 bombed wall chest",
        "vanilla_item": "Dungeon Map (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC951
    },
    "d3 giant blade room": {
        "region_id": "d3 giant blade room",
        "vanilla_item": "Boss Key (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC946
    },
    "d3 boss": {
        "region_id": "d3 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 3,
        "flag_byte": 0xC953
    },
    # Essence is 0xC940

    "d4 pot puzzle": {
        "region_id": "d4 pot puzzle",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC97B
    },
    "d4 north of entrance": {
        "region_id": "d4 north of entrance",
        "vanilla_item": "Bombs (10)",
        "dungeon": 4,
        "flag_byte": 0xC97F
    },
    "d4 maze chest": {
        "region_id": "d4 maze chest",
        "vanilla_item": "Dungeon Map (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC969
    },
    "d4 dark room": {
        "region_id": "d4 dark room",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC96D
    },
    "d4 water ring room": {
        "region_id": "d4 water ring room",
        "vanilla_item": "Compass (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC983
    },
    "d4 pool": {
        "region_id": "d4 pool",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC975
    },
    "d4 terrace": {
        "region_id": "d4 terrace",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC963
    },
    "d4 torch chest": {
        "region_id": "d4 torch chest",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC964
    },
    "d4 cracked floor room": {
        "region_id": "d4 cracked floor room",
        "vanilla_item": "Progressive Slingshot",
        "dungeon": 4,
        "flag_byte": 0xC973
    },
    "d4 dive spot": {
        "region_id": "d4 dive spot",
        "vanilla_item": "Boss Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC96C
    },
    "d4 boss": {
        "region_id": "d4 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 4,
        "flag_byte": 0xC95F
    },
    # Essence is 0xC960

    "d5 cart chest": {
        "region_id": "d5 cart chest",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC999
    },
    "d5 left chest": {
        "region_id": "d5 left chest",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC9A3
    },
    "d5 magnet ball chest": {
        "region_id": "d5 magnet ball chest",
        "vanilla_item": "Magnet Gloves",
        "dungeon": 5,
        "flag_byte": 0xC989
    },
    "d5 terrace chest": {
        "region_id": "d5 terrace chest",
        "vanilla_item": "Rupees (100)",
        "dungeon": 5,
        "flag_byte": 0xC997
    },
    "d5 armos chest": {
        "region_id": "d5 armos chest",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC991
    },
    "d5 gibdo/zol chest": {
        "region_id": "d5 gibdo/zol chest",
        "vanilla_item": "Dungeon Map (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC98F
    },
    "d5 spiral chest": {
        "region_id": "d5 spiral chest",
        "vanilla_item": "Compass (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC99D
    },
    "d5 spinner chest": {
        "region_id": "d5 spinner chest",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC99F
    },
    "d5 stalfos room": {
        "region_id": "d5 stalfos room",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC9A5
    },
    "d5 basement": {
        "region_id": "d5 basement",
        "vanilla_item": "Boss Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC98B
    },
    "d5 boss": {
        "region_id": "d5 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 5,
        "flag_byte": 0xC98C
    },
    # Essence is 0xC988

    "d6 magnet ball drop": {
        "region_id": "d6 magnet ball drop",
        "vanilla_item": "Small Key (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9AB
    },
    "d6 spinner north": {
        "region_id": "d6 spinner north",
        "vanilla_item": "Small Key (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9C2
    },
    "d6 armos hall": {
        "region_id": "d6 armos hall",
        "vanilla_item": "Progressive Boomerang",
        "dungeon": 6,
        "flag_byte": 0xC9D0
    },
    "d6 crystal trap room": {
        "region_id": "d6 crystal trap room",
        "vanilla_item": "Rupees (10)",
        "dungeon": 6,
        "flag_byte": 0xC9AF
    },
    "d6 1F east": {
        "region_id": "d6 1F east",
        "vanilla_item": "Rupees (5)",
        "dungeon": 6,
        "flag_byte": 0xC9B3
    },
    "d6 2F gibdo chest": {
        "region_id": "d6 2F gibdo chest",
        "vanilla_item": "Bombs (10)",
        "dungeon": 6,
        "flag_byte": 0xC9BF
    },
    "d6 2F armos chest": {
        "region_id": "d6 2F armos chest",
        "vanilla_item": "Rupees (5)",
        "dungeon": 6,
        "flag_byte": 0xC9C3
    },
    "d6 beamos room": {
        "region_id": "d6 beamos room",
        "vanilla_item": "Compass (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9AD
    },
    "d6 1F terrace": {
        "region_id": "d6 1F terrace",
        "vanilla_item": "Dungeon Map (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9B0
    },
    "d6 escape room": {
        "region_id": "d6 escape room",
        "vanilla_item": "Boss Key (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9C4
    },
    "d6 vire chest": {
        "region_id": "d6 vire chest",
        "vanilla_item": "Small Key (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9C1
    },
    "d6 boss": {
        "region_id": "d6 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 6,
        "flag_byte": 0xC9D5
    },
    # Essence is 0xC898

    "d7 wizzrobe chest": {
        "region_id": "d7 wizzrobe chest",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA54
    },
    "d7 spike chest": {
        "region_id": "d7 spike chest",
        "vanilla_item": "Progressive Feather",
        "dungeon": 7,
        "flag_byte": 0xCA44
    },
    "d7 maze chest": {
        "region_id": "d7 maze chest",
        "vanilla_item": "Rupees (1)",
        "dungeon": 7,
        "flag_byte": 0xCA43
    },
    "d7 right of entrance": {
        "region_id": "d7 right of entrance",
        "vanilla_item": "Power Ring L-1",
        "dungeon": 7,
        "flag_byte": 0xCA5A
    },
    "d7 bombed wall chest": {
        "region_id": "d7 bombed wall chest",
        "vanilla_item": "Compass (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA52
    },
    "d7 zol button": {
        "region_id": "d7 zol button",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA45
    },
    "d7 armos puzzle": {
        "region_id": "d7 armos puzzle",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA35
    },
    "d7 magunesu chest": {
        "region_id": "d7 magunesu chest",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA47
    },
    "d7 quicksand chest": {
        "region_id": "d7 quicksand chest",
        "vanilla_item": "Dungeon Map (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA58
    },
    "d7 B2F drop": {
        "region_id": "d7 B2F drop",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA3D
    },
    "d7 stalfos chest": {
        "region_id": "d7 stalfos chest",
        "vanilla_item": "Boss Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA48
    },
    "d7 boss": {
        "region_id": "d7 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 7,
        "flag_byte": 0xCA50
    },
    # Essence is 0xCA4F

    "d8 eye drop": {
        "region_id": "d8 eye drop",
        "vanilla_item": "Small Key (Sword & Shield Maze)",
        "dungeon": 8,
        "flag_byte": 0xCA82
    },
    "d8 three eyes chest": {
        "region_id": "d8 three eyes chest",
        "vanilla_item": "Steadfast Ring",
        "dungeon": 8,
        "flag_byte": 0xCA7D
    },
    "d8 hardhat drop": {
        "region_id": "d8 hardhat drop",
        "vanilla_item": "Small Key (Sword & Shield Maze)",
        "dungeon": 8,
        "flag_byte": 0xCA75
    },
    "d8 spike room": {
        "region_id": "d8 spike room",
        "vanilla_item": "Compass (Sword & Shield Maze)",
        "dungeon": 8,
        "flag_byte": 0xCA8B
    },
    "d8 spinner chest": {
        "region_id": "d8 spinner chest",
        "vanilla_item": "Small Key (Sword & Shield Maze)",
        "dungeon": 8,
        "flag_byte": 0xCA70
    },
    "d8 armos chest": {
        "region_id": "d8 armos chest",
        "vanilla_item": "Progressive Slingshot",
        "dungeon": 8,
        "flag_byte": 0xCA8D
    },
    "d8 magnet ball room": {
        "region_id": "d8 magnet ball room",
        "vanilla_item": "Dungeon Map (Sword & Shield Maze)",
        "dungeon": 8,
        "flag_byte": 0xCA8E
    },
    "d8 darknut chest": {
        "region_id": "d8 darknut chest",
        "vanilla_item": "Small Key (Sword & Shield Maze)",
        "dungeon": 8,
        "flag_byte": 0xCA8C
    },
    "d8 pols voice chest": {
        "region_id": "d8 pols voice chest",
        "vanilla_item": "Boss Key (Sword & Shield Maze)",
        "dungeon": 8,
        "flag_byte": 0xCA80
    },
    "d8 ghost armos drop": {
        "region_id": "d8 ghost armos drop",
        "vanilla_item": "Small Key (Sword & Shield Maze)",
        "dungeon": 8,
        "flag_byte": 0xCA7F
    },
    "d8 SE lava chest": {
        "region_id": "d8 SE lava chest",
        "vanilla_item": "Small Key (Sword & Shield Maze)",
        "dungeon": 8,
        "flag_byte": 0xCA6B
    },
    "d8 SW lava chest": {
        "region_id": "d8 SW lava chest",
        "vanilla_item": "Bombs (10)",
        "dungeon": 8,
        "flag_byte": 0xCA6A
    },
    "d8 spark chest": {
        "region_id": "d8 spark chest",
        "vanilla_item": "Small Key (Sword & Shield Maze)",
        "dungeon": 8,
        "flag_byte": 0xCA8A
    },
    "d8 boss": {
        "region_id": "d8 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 8,
        "flag_byte": 0xCA64
    },
    # Essence is 0xCA5F

    "horon heart piece": {
        "region_id": "horon heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC7D8
    },
    "woods of winter heart piece": {
        "region_id": "woods of winter heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC7AF
    },
    "mt. cucco heart piece": {
        "region_id": "mt. cucco heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC72D
    },
    "windmill heart piece": {
        "region_id": "windmill heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xCAB2
    },
    "graveyard heart piece": {
        "region_id": "graveyard heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC7D1
    },
    "spool swamp heart piece": {
        "region_id": "spool swamp heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC7B1
    },
    "temple remains heart piece": {
        "region_id": "temple remains heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xCAC7
    },
    "mayor's house secret room": {
        "region_id": "mayor's house secret room",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC887
    },
    "subrosian house": {
        "region_id": "subrosian house",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC8A1
    },
    "subrosian 2d cave": {
        "region_id": "subrosian 2d cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xCAE3
    },

    "mayor's gift": {
        "region_id": "mayor's gift",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC886
    },
    "vasu's gift": {
        "region_id": "vasu's gift",
        "vanilla_item": "Friendship Ring",
        "flag_byte": 0xC891
    },
    "goron's gift": {
        "region_id": "goron's gift",
        "vanilla_item": "Biggoron's Sword",  # Ring Box doesn't really exist anymore
        "flag_byte": 0xCAC5
    },

    "dr. left reward": {
        "region_id": "dr. left reward",
        "vanilla_item": "Cuccodex",
        "flag_byte": 0xC8A4
    },
    "malon trade": {
        "region_id": "malon trade",
        "vanilla_item": "Lon Lon Egg",
        "flag_byte": 0xC880
    },
#    "maple trade": {
#        "region_id": "maple trade",
#        "vanilla_item": "Ghastly Doll",
#        "flag_byte": 0x
#    },
    "mrs. ruul trade": {
        "region_id": "mrs. ruul trade",
        "vanilla_item": "Iron Pot",
        "flag_byte": 0xC8B3
    },
    "subrosian chef trade": {
        "region_id": "subrosian chef trade",
        "vanilla_item": "Lava Soup",
        "flag_byte": 0xC88F
    },
    "biggoron trade": {
        "region_id": "biggoron trade",
        "vanilla_item": "Goron Vase",
        "flag_byte": 0xC708
    },
    "ingo trade": {
        "region_id": "ingo trade",
        "vanilla_item": "Fish",
        "flag_byte": 0xC899
    },
    "old man trade": {
        "region_id": "old man trade",
        "vanilla_item": "Megaphone",
        "flag_byte": 0xC7B7
    },
    "talon trade": {
        "region_id": "talon trade",
        "vanilla_item": "Mushroom",
        "flag_byte": 0xCAB6,
        "bit_mask": 0x40
    },
    "syrup trade": {
        "region_id": "syrup trade",
        "vanilla_item": "Wooden Bird",
        "flag_byte": 0xC89C
    },
    "tick tock trade": {
        "region_id": "tick tock trade",
        "vanilla_item": "Engine Grease",
        "flag_byte": 0xC883
    },
    "guru-guru trade": {
        "region_id": "guru-guru trade",
        "vanilla_item": "Phonograph",
        "flag_byte": 0xC7DA
    },

#    "subrosian buried bomb flower": {
#        "region_id": "subrosian buried bomb flower",
#        "vanilla_item": "bomb flower",
#        "randomized": False,
#        "flag_byte": 0xC869
#    },
#    "subrosian sign guy": {
#        "region_id": "subrosian sign guy",
#        "vanilla_item": "sign ring",
#        "randomized": False,
#        "flag_byte": 0xC8A9
#    },
    # Maku seed is 0xC85D

    "old man in horon": {
        "region_id": "old man in horon",
        "flag_byte": 0xCA05,
        "bit_mask": 0x40,
        "conditional": True
    },
    "old man near d1": {
        "region_id": "old man near d1",
        "flag_byte": 0xCA03,
        "bit_mask": 0x40,
        "conditional": True
    },
    "old man near blaino": {
        "region_id": "old man near blaino",
        "flag_byte": 0xCA02,
        "bit_mask": 0x40,
        "conditional": True
    },
    "old man in goron mountain": {
        "region_id": "old man in goron mountain",
        "flag_byte": 0xCA01,
        "bit_mask": 0x40,
        "conditional": True
    },
    "old man near western coast house": {
        "region_id": "old man near western coast house",
        "flag_byte": 0xCA04,
        "bit_mask": 0x40,
        "conditional": True
    },
    "old man near holly's house": {
        "region_id": "old man near holly's house",
        "flag_byte": 0xCA07,
        "bit_mask": 0x40,
        "conditional": True
    },
    "old man near mrs. ruul": {
        "region_id": "old man near mrs. ruul",
        "flag_byte": 0xCA08,
        "bit_mask": 0x40,
        "conditional": True
    },
    "old man near d6": {
        "region_id": "old man near d6",
        "flag_byte": 0xCA06,
        "bit_mask": 0x40,
        "conditional": True
    },

    "horon village tree": {
        "region_id": "horon village tree",
        "local": True
    },
    "woods of winter tree": {
        "region_id": "woods of winter tree",
        "local": True
    },
    "north horon tree": {
        "region_id": "north horon tree",
        "local": True
    },
    "spool swamp tree": {
        "region_id": "spool swamp tree",
        "local": True
    },
    "sunken city tree": {
        "region_id": "sunken city tree",
        "local": True
    },
    "tarm ruins tree": {
        "region_id": "tarm ruins tree",
        "local": True
    },

    "golden beasts old man": {
        "region_id": "golden beasts old man",
        "vanilla_item": "Red Ring",
        "flag_byte": 0xCA11,
    }
}
