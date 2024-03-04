
BASE_LOCATION_ID = 27022001000

LOCATIONS_DATA = {
    "Eyeglass Lake: chest across bridge": {
        "patcher_name": "eyeglass lake, across bridge",
        "region_id": "eyeglass lake, across bridge",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC7B8
    },
    "Horon Village: Maku Tree gift": {
        "patcher_name": "maku tree",
        "region_id": "maku tree",
        "vanilla_item": "Gnarled Key",
        "flag_byte": [0xC80B, 0xC80C, 0xC82B, 0xC82C, 0xC82D, 0xC85B, 0xC85C, 0xC85D, 0xC87B]
        # Maku Tree has several rooms depending on the amount of essences owned
    },
    "Horon Village: chest behind mushrooms": {
        "patcher_name": "horon village SW chest",
        "region_id": "horon village SW chest",
        "vanilla_item": "Rupees (20)",
        "flag_byte": 0xC7F5
    },
    "Horon Village: chest in Dr. Left's backyard": {
        "patcher_name": "horon village SE chest",
        "region_id": "horon village SE chest",
        "vanilla_item": "Rupees (20)",
        "flag_byte": 0xC7F9
    },
    "Woods of Winter: Holly's gift": {
        "patcher_name": "holly's house",
        "region_id": "holly's house",
        "vanilla_item": "Shovel",
        "flag_byte": 0xC8A3
    },
    "Woods of Winter: chest on D2 roof": {
        "patcher_name": "chest on top of D2",
        "region_id": "d2 roof",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC78E
    },
    "North Horon: Blaino's gym prize": {
        "patcher_name": "blaino prize",
        "region_id": "blaino prize",
        "vanilla_item": "Ricky's Gloves",
        "flag_byte": 0xC8B4
    },
    "Holodrum Plain: underwater item below Natzu bridge": {
        "patcher_name": "underwater item below natzu bridge",
        "region_id": "underwater item below natzu bridge",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC766
    },
    "Spool Swamp: digging spot": {
        "patcher_name": "spool swamp digging spot",
        "region_id": "spool swamp digging spot",
        "vanilla_item": "Rupees (50)",  # Random ring in vanilla, but this doesn't exist in rando
        "flag_byte": 0xC782
    },
    "Spool Swamp: floodgate keeper's house": {
        "patcher_name": "floodgate keeper's house",
        "region_id": "floodgate keeper's house",
        "vanilla_item": "Floodgate Key",
        "flag_byte": 0xC8B5
    },
    "Spool Swamp: winter cave": {
        "patcher_name": "spool swamp cave",
        "region_id": "spool swamp cave",
        "vanilla_item": "Square Jewel",
        "flag_byte": 0xC9FA
    },
    "Natzu: moblin keep": {
        "patcher_name": "moblin keep",
        "region_id": "moblin keep",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC75B
    },
    "Sunken City: Master Diver's challenge chest": {
        "patcher_name": "master diver's challenge",
        "region_id": "master diver's challenge",
        "vanilla_item": "Master's Plaque",
        "flag_byte": 0xCABC
    },
    "Sunken City: Master Diver's reward": {
        "patcher_name": "master diver's reward",
        "region_id": "master diver's reward",
        "vanilla_item": "Flippers",
        "flag_byte": 0xCABD,
        "bit_mask": 0x80
    },
    "Sunken City: chest in Master Diver's cave": {
        "patcher_name": "chest in master diver's cave",
        "region_id": "chest in master diver's cave",
        "vanilla_item": "Rupees (50)",
        "flag_byte": 0xCABD
    },
    "Mt. Cucco: Spring Banana tree": {
        "patcher_name": "spring banana tree",
        "region_id": "spring banana tree",
        "vanilla_item": "Spring Banana",
        "flag_byte": 0xC70F
    },
    "Goron Mountain: item across pits": {
        "patcher_name": "goron mountain, across pits",
        "region_id": "goron mountain, across pits",
        "vanilla_item": "Dragon Key",
        "flag_byte": 0xC71A
    },
    "Mt. Cucco: moving platform cave": {
        "patcher_name": "mt. cucco, platform cave",
        "region_id": "mt. cucco, platform cave",
        "vanilla_item": "Green Joy Ring",
        "flag_byte": 0xCABB
    },
    "Mt. Cucco: diving spot outside D4": {
        "patcher_name": "diving spot outside D4",
        "region_id": "diving spot outside D4",
        "vanilla_item": "Pyramid Jewel",
        "flag_byte": 0xCAE5,
    },
    "Western Coast: black beast's chest": {
        "patcher_name": "black beast's chest",
        "region_id": "black beast's chest",
        "vanilla_item": "X-Shaped Jewel",
        "flag_byte": 0xC7F4
    },
    "North Horon: old man in treehouse": {
        "patcher_name": "old man in treehouse",
        "region_id": "old man in treehouse",
        "vanilla_item": "Round Jewel",
        "flag_byte": 0xC894
    },
    "Lost Woods: pedestal item": {
        "patcher_name": "lost woods",
        "region_id": "lost woods",
        "vanilla_item": "Progressive Sword",
        "flag_byte": 0xC7C9,
    },
    "Samasa Desert: item in quicksand pit": {
        "patcher_name": "samasa desert pit",
        "region_id": "samasa desert pit",
        "vanilla_item": "Rusty Bell",
        "flag_byte": 0xCAD2
    },
    "Samasa Desert: elevated chest": {
        "patcher_name": "samasa desert chest",
        "region_id": "samasa desert chest",
        "vanilla_item": "Rang Ring L-1",
        "flag_byte": 0xC7FF
    },
    "Western Coast: beach chest": {
        "patcher_name": "western coast, beach chest",
        "region_id": "western coast after ship",
        "vanilla_item": "Blast Ring",
        "flag_byte": 0xC7E3
    },
    "Western Coast: house chest": {
        "patcher_name": "western coast, in house",
        "region_id": "western coast after ship",
        "vanilla_item": "Bombs (10)",
        "flag_byte": 0xC888
    },
    "Holodrum Plain: flooded cave south of Mrs. Ruul": {
        "patcher_name": "cave south of mrs. ruul",
        "region_id": "cave south of mrs. ruul",
        "vanilla_item": "Octo Ring",
        "flag_byte": 0xC9E0
    },
    "Holodrum Plain: autumn cave north of D1": {
        "patcher_name": "cave north of D1",
        "region_id": "cave north of D1",
        "vanilla_item": "Quicksand Ring",
        "flag_byte": 0xC9E1
    },
    "Woods of Winter: autumn cave outside D2": {
        "patcher_name": "cave outside D2",
        "region_id": "cave outside D2",
        "vanilla_item": "Moblin Ring",
        "flag_byte": 0xCAB3
    },
    "Woods of Winter: cave behind bombable rocks": {
        "patcher_name": "woods of winter, 1st cave",
        "region_id": "woods of winter, 1st cave",
        "vanilla_item": "Rupees (30)",
        "flag_byte": 0xCAB4
    },
    "Sunken City: summer cave": {
        "patcher_name": "sunken city, summer cave",
        "region_id": "sunken city, summer cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xCAB5
    },
    "Eyeglass Lake: dried lake east cave": {
        "patcher_name": "dry eyeglass lake, east cave",
        "region_id": "dry eyeglass lake, east cave",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xCAC0
    },
    "Goron Mountain: interior chest": {
        "patcher_name": "chest in goron mountain",
        "region_id": "chest in goron mountain",
        "vanilla_item": "Armor Ring L-2",
        "flag_byte": 0xCAC8
    },
    "Natzu Region: chest in cave across water": {
        "patcher_name": "natzu region, across water",
        "region_id": "natzu region, across water",
        "vanilla_item": "Rupees (50)",
        "flag_byte": 0xCA0E
    },
    "Mt. Cucco: Talon's cave chest": {
        "patcher_name": "mt. cucco, talon's cave",
        "region_id": "mt. cucco, talon's cave",
        "vanilla_item": "Subrosian Ring",
        "flag_byte": 0xCAB6,
        "bit_mask": 0x60  # 0x60 is needed here to ensure we're not sending Talon's wakeup item as a false positive
    },
    "Tarm Ruins: chest in rabbit hole under tree": {
        "patcher_name": "tarm ruins, under tree",
        "region_id": "tarm ruins, under tree",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC89B
    },
    "Eastern Suburbs: spring cave chest": {
        "patcher_name": "eastern suburbs spring cave",
        "region_id": "eastern suburbs spring cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC9F7
    },
    "Eyeglass Lake: dried lake west cave": {
        "patcher_name": "dry eyeglass lake, west cave",
        "region_id": "dry eyeglass lake, west cave",
        "vanilla_item": "Rupees (100)",
        "flag_byte": 0xC9FB
    },
    "Woods of Winter: waterfall cave chest": {
        "patcher_name": "woods of winter, 2nd cave",
        "region_id": "woods of winter, 2nd cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xCA12
    },
    "Horon Village: shop item #1": {
        "patcher_name": "shop, 20 rupees",
        "region_id": "shop, 20 rupees",
        "vanilla_item": "Bombs (10)",
        "randomized": False
    },
    "Horon Village: shop item #2": {
        "patcher_name": "shop, 30 rupees",
        "region_id": "shop, 30 rupees",
        "vanilla_item": "Progressive Shield",
        "randomized": False
    },
    "Horon Village: shop item #3": {
        "patcher_name": "shop, 150 rupees",
        "region_id": "shop, 150 rupees",
        "vanilla_item": "Flute",
        "flag_byte": 0xC693,
        "bit_mask": 0x80
    },
    "Horon Village: member's shop item #1": {
        "patcher_name": "member's shop 1",
        "region_id": "member's shop",
        "vanilla_item": "Seed Satchel",
        "flag_byte": 0xC63F,
        "bit_mask": 0x01,
    },
    "Horon Village: member's shop item #2": {
        "patcher_name": "member's shop 2",
        "region_id": "member's shop",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC63F,
        "bit_mask": 0x02,
    },
    "Horon Village: member's shop item #3": {
        "patcher_name": "member's shop 3",
        "region_id": "member's shop",
        "vanilla_item": "Treasure Map",
        "flag_byte": 0xC63F,
        "bit_mask": 0x08,
    },

    "Subrosia: tower of winter": {
        "patcher_name": "tower of winter",
        "region_id": "tower of winter",
        "vanilla_item": "Rod of Seasons (Winter)",
        "flag_byte": 0xCAF2
    },
    "Subrosia: tower of summer": {
        "patcher_name": "tower of summer",
        "region_id": "tower of summer",
        "vanilla_item": "Rod of Seasons (Summer)",
        "flag_byte": 0xCAF8
    },
    "Subrosia: tower of spring": {
        "patcher_name": "tower of spring",
        "region_id": "tower of spring",
        "vanilla_item": "Rod of Seasons (Spring)",
        "flag_byte": 0xCAF5
    },
    "Subrosia: tower of autumn": {
        "patcher_name": "tower of autumn",
        "region_id": "tower of autumn",
        "vanilla_item": "Rod of Seasons (Autumn)",
        "flag_byte": 0xCAFB
    },
    "Subrosia: dance hall reward": {
        "patcher_name": "subrosian dance hall",
        "region_id": "subrosian dance hall",
        "vanilla_item": "Progressive Boomerang",
        "flag_byte": 0xC895
    },
    "Subrosia: temple of seasons": {
        "patcher_name": "temple of seasons",
        "region_id": "temple of seasons",
        "vanilla_item": "Rod of Seasons",
        "flag_byte": 0xC8AC
    },
    "Subrosia: seaside digging spot": {
        "patcher_name": "subrosia seaside",
        "region_id": "subrosia seaside",
        "vanilla_item": "Star Ore",
        "flag_byte": [0xC865, 0xC866, 0xC875, 0xC876]
    },
    "Subrosia: wilds chest": {
        "patcher_name": "subrosian wilds chest",
        "region_id": "subrosian wilds chest",
        "vanilla_item": "Blue Ore",
        "flag_byte": 0xC841
    },
    "Subrosia: wilds digging spot": {
        "patcher_name": "subrosian wilds digging spot",
        "region_id": "subrosian wilds digging spot",
        "vanilla_item": "Rupees (50)",  # Random ring in vanilla, but this doesn't exist in rando
        "flag_byte": 0xC840
    },
    "Subrosia: chest above cave near great furnace": {
        "patcher_name": "subrosia village chest",
        "region_id": "subrosia village chest",
        "vanilla_item": "Red Ore",
        "flag_byte": 0xC858
    },
    "Subrosia: bridge sector open cave": {
        "patcher_name": "subrosia, open cave",
        "region_id": "subrosia, open cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC9F1
    },
    "Subrosia: bridge sector locked cave": {
        "patcher_name": "subrosia, locked cave",
        "region_id": "subrosia, locked cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xCAC6
    },
    "Subrosia: market item #1": {
        "patcher_name": "subrosia market, 1st item",
        "region_id": "subrosia market, 1st item",
        "vanilla_item": "Ribbon",
        "flag_byte": 0xC642,
        "bit_mask": 0x01,
    },
    "Subrosia: market item #2": {
        "patcher_name": "subrosia market, 2nd item",
        "region_id": "subrosia market, 2nd item",
        "vanilla_item": "Rare Peach Stone",
        "flag_byte": 0xC642,
        "bit_mask": 0x02,
    },
    "Subrosia: market item #3": {
        "patcher_name": "subrosia market, 3rd item",
        "region_id": "subrosia market, 3rd item",
        "vanilla_item": "Bomb Bag Upgrade",
        "conditional": True,  # Not yet implemented
        # "flag_byte": 0xC...,
    },
    "Subrosia: market item #4": {
        "patcher_name": "subrosia market, 4th item",
        "region_id": "subrosia market, 4th item",
        "vanilla_item": "Progressive Shield",
        "conditional": True,  # Not yet implemented
        # "flag_byte": 0xC...,
    },
    "Subrosia: market item #5": {
        "patcher_name": "subrosia market, 5th item",
        "region_id": "subrosia market, 5th item",
        "vanilla_item": "Member's Card",
        "flag_byte": 0xC694,
        "bit_mask": 0x01
    },
    "Subrosia: item smelted in Great Furnace": {
        "patcher_name": "great furnace",
        "region_id": "great furnace",
        "vanilla_item": "Hard Ore",
        "flag_byte": 0xC88E
    },
    "Subrosia: item forged by smithy from Hard Ore": {
        "patcher_name": "subrosian smithy ore",
        "region_id": "subrosian smithy ore",
        "vanilla_item": "Progressive Shield",
        "flag_byte": 0xC897,
        "bit_mask": 0x40
    },
    "Subrosia: item forged by smithy from Rusty Bell": {
        "patcher_name": "subrosian smithy bell",
        "region_id": "subrosian smithy bell",
        "vanilla_item": "pirate's bell",
        "conditional": True,
        "randomized": False,
        "flag_byte": 0xC897,
        "local": True
    },

    "Hero's Cave: key chest": {
        "patcher_name": "d0 key chest",
        "region_id": "d0 key chest",
        "vanilla_item": "Small Key (Hero's Cave)",
        "dungeon": 0,
        "flag_byte": 0xC903
    },
    "Hero's Cave: sword chest": {
        "patcher_name": "d0 sword chest",
        "region_id": "d0 sword chest",
        "vanilla_item": "Progressive Sword",
        "dungeon": 0,
        "flag_byte": 0xC906
    },
    "Hero's Cave: item in hidden 2d section": {
        "patcher_name": "d0 hidden 2d section",
        "region_id": "d0 hidden 2d section",
        "vanilla_item": "Gasha Seed",
        "dungeon": 0,
        "flag_byte": 0xC901
    },
    "Hero's Cave: alternative entrance chest": {
        "patcher_name": "d0 rupee chest",
        "region_id": "d0 rupee chest",
        "vanilla_item": "Rupees (30)",
        "dungeon": 0,
        "flag_byte": 0xC905
    },

    "Gnarled Root Dungeon: stalfos drop": {
        "patcher_name": "d1 stalfos drop",
        "region_id": "d1 stalfos drop",
        "vanilla_item": "Small Key (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC91B
    },
    "Gnarled Root Dungeon: side-scrolling basement item": {
        "patcher_name": "d1 basement",
        "region_id": "d1 basement",
        "vanilla_item": "Seed Satchel",
        "dungeon": 1,
        "flag_byte": 0xC909
    },
    "Gnarled Root Dungeon: block-pushing room chest": {
        "patcher_name": "d1 block-pushing room",
        "region_id": "d1 block-pushing room",
        "vanilla_item": "Gasha Seed",
        "dungeon": 1,
        "flag_byte": 0xC90D
    },
    "Gnarled Root Dungeon: railway chest": {
        "patcher_name": "d1 railway chest",
        "region_id": "d1 railway chest",
        "vanilla_item": "Bombs (10)",
        "dungeon": 1,
        "flag_byte": 0xC910
    },
    "Gnarled Root Dungeon: floormaster room chest": {
        "patcher_name": "d1 floormaster room",
        "region_id": "d1 floormaster room",
        "vanilla_item": "Discovery Ring",
        "dungeon": 1,
        "flag_byte": 0xC917
    },
    "Gnarled Root Dungeon: chest near minecart lever": {
        "patcher_name": "d1 lever room",
        "region_id": "d1 lever room",
        "vanilla_item": "Compass (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC90F
    },
    "Gnarled Root Dungeon: stalfos chest": {
        "patcher_name": "d1 stalfos chest",
        "region_id": "d1 stalfos chest",
        "vanilla_item": "Dungeon Map (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC919
    },
    "Gnarled Root Dungeon: button chest": {
        "patcher_name": "d1 button chest",
        "region_id": "d1 button chest",
        "vanilla_item": "Small Key (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC911
    },
    "Gnarled Root Dungeon: goriya chest": {
        "patcher_name": "d1 goriya chest",
        "region_id": "d1 goriya chest",
        "vanilla_item": "Boss Key (Gnarled Root Dungeon)",
        "dungeon": 1,
        "flag_byte": 0xC914
    },
    "Gnarled Root Dungeon: boss reward": {
        "patcher_name": "d1 boss",
        "region_id": "d1 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 1,
        "flag_byte": 0xC912
    },
    # Essence is 0xC913

    "Snake's Remains: rope drop": {
        "patcher_name": "d2 rope drop",
        "region_id": "d2 rope drop",
        "vanilla_item": "Small Key (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC934
    },
    "Snake's Remains: distant moblins chest": {
        "patcher_name": "d2 moblin chest",
        "region_id": "d2 moblin chest",
        "vanilla_item": "Bracelet",
        "dungeon": 2,
        "flag_byte": 0xC92A
    },
    "Snake's Remains: chest in rollers section": {
        "patcher_name": "d2 roller chest",
        "region_id": "d2 roller chest",
        "vanilla_item": "Rupees (10)",
        "dungeon": 2,
        "flag_byte": 0xC91F
    },
    "Snake's Remains: chest left from entrance": {
        "patcher_name": "d2 left from entrance",
        "region_id": "d2 left from entrance",
        "vanilla_item": "Rupees (5)",
        "dungeon": 2,
        "flag_byte": 0xC938
    },
    "Snake's Remains: hardhat room chest behind pots": {
        "patcher_name": "d2 pot chest",
        "region_id": "d2 pot chest",
        "vanilla_item": "Dungeon Map (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC92B
    },
    "Snake's Remains: rope chest": {
        "patcher_name": "d2 rope chest",
        "region_id": "d2 rope chest",
        "vanilla_item": "Compass (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC936
    },
    "Snake's Remains: moving blades room chest": {
        "patcher_name": "d2 blade chest",
        "region_id": "d2 blade chest",
        "vanilla_item": "Small Key (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC931
    },
    "Snake's Remains: timed spiral chest": {
        "patcher_name": "d2 spiral chest",
        "region_id": "d2 spiral chest",
        "vanilla_item": "Small Key (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC92D
    },
    "Snake's Remains: terrace chest": {
        "patcher_name": "d2 terrace chest",
        "region_id": "d2 terrace chest",
        "vanilla_item": "Boss Key (Snake's Remains)",
        "dungeon": 2,
        "flag_byte": 0xC924
    },
    "Snake's Remains: boss reward": {
        "patcher_name": "d2 boss",
        "region_id": "d2 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 2,
        "flag_byte": 0xC929
    },
    # Essence is 0xC92C

    "Poison Moth's Lair (B1F): roller room chest": {
        "patcher_name": "d3 roller chest",
        "region_id": "d3 roller chest",
        "vanilla_item": "Small Key (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC94C
    },
    "Poison Moth's Lair (1F): mimic room chest": {
        "patcher_name": "d3 mimic chest",
        "region_id": "d3 mimic chest",
        "vanilla_item": "Progressive Feather",
        "dungeon": 3,
        "flag_byte": 0xC950
    },
    "Poison Moth's Lair (1F): zol throne chest": {
        "patcher_name": "d3 zol chest",
        "region_id": "d3 zol chest",
        "vanilla_item": "Small Key (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC94F
    },
    "Poison Moth's Lair (B1F): water room chest": {
        "patcher_name": "d3 water room",
        "region_id": "d3 water room",
        "vanilla_item": "Rupees (30)",
        "dungeon": 3,
        "flag_byte": 0xC941
    },
    "Poison Moth's Lair (B1F): quicksand terrace chest": {
        "patcher_name": "d3 quicksand terrace",
        "region_id": "d3 quicksand terrace",
        "vanilla_item": "Gasha Seed",
        "dungeon": 3,
        "flag_byte": 0xC944
    },
    "Poison Moth's Lair (1F): moldorm chest": {
        "patcher_name": "d3 moldorm chest",
        "region_id": "d3 moldorm chest",
        "vanilla_item": "Bombs (10)",
        "dungeon": 3,
        "flag_byte": 0xC954
    },
    "Poison Moth's Lair (1F): chest above trampoline & owl room": {
        "patcher_name": "d3 trampoline chest",
        "region_id": "d3 trampoline chest",
        "vanilla_item": "Compass (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC94D
    },
    "Poison Moth's Lair (1F): secret bombable wall chest": {
        "patcher_name": "d3 bombed wall chest",
        "region_id": "d3 bombed wall chest",
        "vanilla_item": "Dungeon Map (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC951
    },
    "Poison Moth's Lair (B1F): moving blade room chest": {
        "patcher_name": "d3 giant blade room",
        "region_id": "d3 giant blade room",
        "vanilla_item": "Boss Key (Poison Moth's Lair)",
        "dungeon": 3,
        "flag_byte": 0xC946
    },
    "Poison Moth's Lair (1F): boss reward": {
        "patcher_name": "d3 boss",
        "region_id": "d3 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 3,
        "flag_byte": 0xC953
    },
    # Essence is 0xC940

    "Dancing Dragon Dungeon (2F): pots & buttons puzzle drop": {
        "patcher_name": "d4 pot puzzle",
        "region_id": "d4 pot puzzle",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC97B
    },
    "Dancing Dragon Dungeon (2F): chest north of entrance": {
        "patcher_name": "d4 north of entrance",
        "region_id": "d4 north of entrance",
        "vanilla_item": "Bombs (10)",
        "dungeon": 4,
        "flag_byte": 0xC97F
    },
    "Dancing Dragon Dungeon (1F): beamos room isolated chest": {
        "patcher_name": "d4 maze chest",
        "region_id": "d4 maze chest",
        "vanilla_item": "Dungeon Map (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC969
    },
    "Dancing Dragon Dungeon (1F): dark room chest": {
        "patcher_name": "d4 dark room",
        "region_id": "d4 dark room",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC96D
    },
    "Dancing Dragon Dungeon (2F): water donut room chest": {
        "patcher_name": "d4 water ring room",
        "region_id": "d4 water ring room",
        "vanilla_item": "Compass (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC983
    },
    "Dancing Dragon Dungeon (2F): pool drop": {
        "patcher_name": "d4 pool",
        "region_id": "d4 pool",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC975
    },
    "Dancing Dragon Dungeon (1F): small terrace chest": {
        "patcher_name": "d4 terrace",
        "region_id": "d4 terrace",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC963
    },
    "Dancing Dragon Dungeon (1F): minecart torches chest": {
        "patcher_name": "d4 torch chest",
        "region_id": "d4 torch chest",
        "vanilla_item": "Small Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC964
    },
    "Dancing Dragon Dungeon (1F): cracked floor time trial chest": {
        "patcher_name": "d4 cracked floor room",
        "region_id": "d4 cracked floor room",
        "vanilla_item": "Progressive Slingshot",
        "dungeon": 4,
        "flag_byte": 0xC973
    },
    "Dancing Dragon Dungeon (1F): eye dive spot item": {
        "patcher_name": "d4 dive spot",
        "region_id": "d4 dive spot",
        "vanilla_item": "Boss Key (Dancing Dragon Dungeon)",
        "dungeon": 4,
        "flag_byte": 0xC96C
    },
    "Dancing Dragon Dungeon (B1F): boss reward": {
        "patcher_name": "d4 boss",
        "region_id": "d4 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 4,
        "flag_byte": 0xC95F
    },
    # Essence is 0xC960

    "Unicorn's Cave: right cart chest": {
        "patcher_name": "d5 cart chest",
        "region_id": "d5 cart chest",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC999
    },
    "Unicorn's Cave: chest left of entrance": {
        "patcher_name": "d5 left chest",
        "region_id": "d5 left chest",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC9A3
    },
    "Unicorn's Cave: magnet gloves chest": {
        "patcher_name": "d5 magnet ball chest",
        "region_id": "d5 magnet ball chest",
        "vanilla_item": "Magnet Gloves",
        "dungeon": 5,
        "flag_byte": 0xC989
    },
    "Unicorn's Cave: terrace chest": {
        "patcher_name": "d5 terrace chest",
        "region_id": "d5 terrace chest",
        "vanilla_item": "Rupees (100)",
        "dungeon": 5,
        "flag_byte": 0xC997
    },
    "Unicorn's Cave: armos puzzle room chest": {
        "patcher_name": "d5 armos chest",
        "region_id": "d5 armos chest",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC991
    },
    "Unicorn's Cave: gibdo room chest": {
        "patcher_name": "d5 gibdo/zol chest",
        "region_id": "d5 gibdo/zol chest",
        "vanilla_item": "Dungeon Map (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC98F
    },
    "Unicorn's Cave: quicksand spiral chest": {
        "patcher_name": "d5 spiral chest",
        "region_id": "d5 spiral chest",
        "vanilla_item": "Compass (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC99D
    },
    "Unicorn's Cave: magnet spinner chest": {
        "patcher_name": "d5 spinner chest",
        "region_id": "d5 spinner chest",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC99F
    },
    "Unicorn's Cave: isolated minecart bay chest": {
        "patcher_name": "d5 stalfos room",
        "region_id": "d5 stalfos room",
        "vanilla_item": "Small Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC9A5
    },
    "Unicorn's Cave: side-scrolling basement item": {
        "patcher_name": "d5 basement",
        "region_id": "d5 basement",
        "vanilla_item": "Boss Key (Unicorn's Cave)",
        "dungeon": 5,
        "flag_byte": 0xC98B
    },
    "Unicorn's Cave: boss reward": {
        "patcher_name": "d5 boss",
        "region_id": "d5 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 5,
        "flag_byte": 0xC98C
    },
    # Essence is 0xC988

    "Ancient Ruins (1F): magnet ball puzzle drop": {
        "patcher_name": "d6 magnet ball drop",
        "region_id": "d6 magnet ball drop",
        "vanilla_item": "Small Key (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9AB
    },
    "Ancient Ruins (2F): chest north of main spinner": {
        "patcher_name": "d6 spinner north",
        "region_id": "d6 spinner north",
        "vanilla_item": "Small Key (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9C2
    },
    "Ancient Ruins (3F): armos hall chest": {
        "patcher_name": "d6 armos hall",
        "region_id": "d6 armos hall",
        "vanilla_item": "Progressive Boomerang",
        "dungeon": 6,
        "flag_byte": 0xC9D0
    },
    "Ancient Ruins (1F): crystal maze room chest": {
        "patcher_name": "d6 crystal trap room",
        "region_id": "d6 crystal trap room",
        "vanilla_item": "Rupees (10)",
        "dungeon": 6,
        "flag_byte": 0xC9AF
    },
    "Ancient Ruins (1F): crumbling ground room chest": {
        "patcher_name": "d6 1F east",
        "region_id": "d6 1F east",
        "vanilla_item": "Rupees (5)",
        "dungeon": 6,
        "flag_byte": 0xC9B3
    },
    "Ancient Ruins (2F): gibdo chest": {
        "patcher_name": "d6 2F gibdo chest",
        "region_id": "d6 2F gibdo chest",
        "vanilla_item": "Bombs (10)",
        "dungeon": 6,
        "flag_byte": 0xC9BF
    },
    "Ancient Ruins (2F): armos chest": {
        "patcher_name": "d6 2F armos chest",
        "region_id": "d6 2F armos chest",
        "vanilla_item": "Rupees (5)",
        "dungeon": 6,
        "flag_byte": 0xC9C3
    },
    "Ancient Ruins (1F): beamos room chest": {
        "patcher_name": "d6 beamos room",
        "region_id": "d6 beamos room",
        "vanilla_item": "Compass (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9AD
    },
    "Ancient Ruins (1F): terrace chest": {
        "patcher_name": "d6 1F terrace",
        "region_id": "d6 1F terrace",
        "vanilla_item": "Dungeon Map (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9B0
    },
    "Ancient Ruins (2F): chest after escape room": {
        "patcher_name": "d6 escape room",
        "region_id": "d6 escape room",
        "vanilla_item": "Boss Key (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9C4
    },
    "Ancient Ruins (2F): red terrace chest before Vire": {
        "patcher_name": "d6 vire chest",
        "region_id": "d6 vire chest",
        "vanilla_item": "Small Key (Ancient Ruins)",
        "dungeon": 6,
        "flag_byte": 0xC9C1
    },
    "Ancient Ruins (5F): boss reward": {
        "patcher_name": "d6 boss",
        "region_id": "d6 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 6,
        "flag_byte": 0xC9D5
    },
    # Essence is 0xC898

    "Explorer's Crypt (1F): wizzrobe room chest": {
        "patcher_name": "d7 wizzrobe chest",
        "region_id": "d7 wizzrobe chest",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA54
    },
    "Explorer's Crypt (B1F): fast moving platform room chest": {
        "patcher_name": "d7 spike chest",
        "region_id": "d7 spike chest",
        "vanilla_item": "Progressive Feather",
        "dungeon": 7,
        "flag_byte": 0xCA44
    },
    "Explorer's Crypt (B2F): stair maze chest": {
        "patcher_name": "d7 maze chest",
        "region_id": "d7 maze chest",
        "vanilla_item": "Rupees (1)",
        "dungeon": 7,
        "flag_byte": 0xCA43
    },
    "Explorer's Crypt (1F): chest right of entrance": {
        "patcher_name": "d7 right of entrance",
        "region_id": "d7 right of entrance",
        "vanilla_item": "Power Ring L-1",
        "dungeon": 7,
        "flag_byte": 0xCA5A
    },
    "Explorer's Crypt (1F): chest behind bombable wall": {
        "patcher_name": "d7 bombed wall chest",
        "region_id": "d7 bombed wall chest",
        "vanilla_item": "Compass (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA52
    },
    "Explorer's Crypt (B1F): zol button drop": {
        "patcher_name": "d7 zol button",
        "region_id": "d7 zol button",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA45
    },
    "Explorer's Crypt (B2F): armos puzzle drop": {
        "patcher_name": "d7 armos puzzle",
        "region_id": "d7 armos puzzle",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA35
    },
    "Explorer's Crypt (B1F): magnet ball on button chest": {
        "patcher_name": "d7 magunesu chest",
        "region_id": "d7 magunesu chest",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA47
    },
    "Explorer's Crypt (1F): chest accessed using trampoline before 2nd Poe": {
        "patcher_name": "d7 quicksand chest",
        "region_id": "d7 quicksand chest",
        "vanilla_item": "Dungeon Map (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA58
    },
    "Explorer's Crypt (B2F): drop after magnet spinners": {
        "patcher_name": "d7 B2F drop",
        "region_id": "d7 B2F drop",
        "vanilla_item": "Small Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA3D
    },
    "Explorer's Crypt (B1F): jumping stalfos chest": {
        "patcher_name": "d7 stalfos chest",
        "region_id": "d7 stalfos chest",
        "vanilla_item": "Boss Key (Explorer's Crypt)",
        "dungeon": 7,
        "flag_byte": 0xCA48
    },
    "Explorer's Crypt (B1F): boss reward": {
        "patcher_name": "d7 boss",
        "region_id": "d7 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 7,
        "flag_byte": 0xCA50
    },
    # Essence is 0xCA4F

    "Sword & Shield Dungeon (1F): eye drop near entrance": {
        "patcher_name": "d8 eye drop",
        "region_id": "d8 eye drop",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA82
    },
    "Sword & Shield Dungeon (1F): three eyes chest": {
        "patcher_name": "d8 three eyes chest",
        "region_id": "d8 three eyes chest",
        "vanilla_item": "Steadfast Ring",
        "dungeon": 8,
        "flag_byte": 0xCA7D
    },
    "Sword & Shield Dungeon (1F): hardhat & magnet ball room drop": {
        "patcher_name": "d8 hardhat drop",
        "region_id": "d8 hardhat drop",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA75
    },
    "Sword & Shield Dungeon (1F): U-shaped spiky freezer chest": {
        "patcher_name": "d8 spike room",
        "region_id": "d8 spike room",
        "vanilla_item": "Compass (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA8B
    },
    "Sword & Shield Dungeon (B1F): chest right of spinner": {
        "patcher_name": "d8 spinner chest",
        "region_id": "d8 spinner chest",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA70
    },
    "Sword & Shield Dungeon (1F): lava bridge room upper chest": {
        "patcher_name": "d8 armos chest",
        "region_id": "d8 armos chest",
        "vanilla_item": "Progressive Slingshot",
        "dungeon": 8,
        "flag_byte": 0xCA8D
    },
    "Sword & Shield Dungeon (1F): lava bridge room bottom chest": {
        "patcher_name": "d8 magnet ball room",
        "region_id": "d8 magnet ball room",
        "vanilla_item": "Dungeon Map (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA8E
    },
    "Sword & Shield Dungeon (1F): bombable blocks room chest": {
        "patcher_name": "d8 darknut chest",
        "region_id": "d8 darknut chest",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA8C
    },
    "Sword & Shield Dungeon (1F): chest on terrace after pols voice room": {
        "patcher_name": "d8 pols voice chest",
        "region_id": "d8 pols voice chest",
        "vanilla_item": "Boss Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA80
    },
    "Sword & Shield Dungeon (1F): ghost armos puzzle drop": {
        "patcher_name": "d8 ghost armos drop",
        "region_id": "d8 ghost armos drop",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA7F
    },
    "Sword & Shield Dungeon (B1F): south-east lava chest": {
        "patcher_name": "d8 SE lava chest",
        "region_id": "d8 SE lava chest",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA6B
    },
    "Sword & Shield Dungeon (B1F): south-west lava chest": {
        "patcher_name": "d8 SW lava chest",
        "region_id": "d8 SW lava chest",
        "vanilla_item": "Bombs (10)",
        "dungeon": 8,
        "flag_byte": 0xCA6A
    },
    "Sword & Shield Dungeon (1F): sparks & pots room chest": {
        "patcher_name": "d8 spark chest",
        "region_id": "d8 spark chest",
        "vanilla_item": "Small Key (Sword & Shield Dungeon)",
        "dungeon": 8,
        "flag_byte": 0xCA8A
    },
    "Sword & Shield Dungeon (B1F): boss reward": {
        "patcher_name": "d8 boss",
        "region_id": "d8 boss",
        "vanilla_item": "Heart Container",
        "dungeon": 8,
        "flag_byte": 0xCA64
    },
    # Essence is 0xCA5F

    "Horon Village: freestanding item behind small tree": {
        "patcher_name": "horon heart piece",
        "region_id": "horon heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC7D8
    },
    "Woods of Winter: freestanding item below lake": {
        "patcher_name": "woods of winter heart piece",
        "region_id": "woods of winter heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC7AF
    },
    "Mt. Cucco: freestanding item on ledge": {
        "patcher_name": "mt. cucco heart piece",
        "region_id": "mt. cucco heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC72D
    },
    "Eastern Suburbs: freestanding item in windmill cave": {
        "patcher_name": "windmill heart piece",
        "region_id": "windmill heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xCAB2
    },
    "Western Coast: freestanding item in graveyard": {
        "patcher_name": "graveyard heart piece",
        "region_id": "graveyard heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC7D1
    },
    "Spool Swamp: freestanding item reachable in spring": {
        "patcher_name": "spool swamp heart piece",
        "region_id": "spool swamp heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xC7B1
    },
    "Temple Remains: freestanding item in bombable cave": {
        "patcher_name": "temple remains heart piece",
        "region_id": "temple remains heart piece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xCAC7
    },
    "Horon Village: freestanding item in mayor's house secret room": {
        "patcher_name": "mayor's house secret room",
        "region_id": "mayor's house secret room",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC887
    },
    "Subrosia: freestanding item in house": {
        "patcher_name": "subrosian house",
        "region_id": "subrosian house",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC8A1
    },
    "Subrosia: freestanding item in side-scrolling cave": {
        "patcher_name": "subrosian 2d cave",
        "region_id": "subrosian 2d cave",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xCAE3
    },

    "Horon Village: mayor's gift": {
        "patcher_name": "mayor's gift",
        "region_id": "mayor's gift",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xC886
    },
    "Horon Village: Vasu's gift": {
        "patcher_name": "vasu's gift",
        "region_id": "vasu's gift",
        "vanilla_item": "Friendship Ring",
        "flag_byte": 0xC891
    },
    "Goron Mountain: goron's gift": {
        "patcher_name": "goron's gift",
        "region_id": "goron's gift",
        "vanilla_item": "Biggoron's Sword",  # Ring Box doesn't really exist anymore
        "flag_byte": 0xCAC5
    },

    "Horon Village: Dr. Left reward": {
        "patcher_name": "dr. left reward",
        "region_id": "dr. left reward",
        "vanilla_item": "Cuccodex",
        "flag_byte": 0xC8A4
    },
    "North Horon: Malon trade": {
        "patcher_name": "malon trade",
        "region_id": "malon trade",
        "vanilla_item": "Lon Lon Egg",
        "flag_byte": 0xC880
    },
    "Maple trade": {
        "patcher_name": "maple trade",
        "region_id": "maple trade",
        "vanilla_item": "Ghastly Doll",
        "conditional": True,  # Not yet implemented
        # "flag_byte": 0x
    },
    "Holodrum Plain: Mrs. Ruul trade": {
        "patcher_name": "mrs. ruul trade",
        "region_id": "mrs. ruul trade",
        "vanilla_item": "Iron Pot",
        "flag_byte": 0xC8B3
    },
    "Subrosia: Subrosian chef trade": {
        "patcher_name": "subrosian chef trade",
        "region_id": "subrosian chef trade",
        "vanilla_item": "Lava Soup",
        "flag_byte": 0xC88F
    },
    "Goron Mountain: Biggoron trade": {
        "patcher_name": "biggoron trade",
        "region_id": "biggoron trade",
        "vanilla_item": "Goron Vase",
        "flag_byte": 0xC708
    },
    "Sunken City: Ingo trade": {
        "patcher_name": "ingo trade",
        "region_id": "ingo trade",
        "vanilla_item": "Fish",
        "flag_byte": 0xC899
    },
    "North Horon: old man with cat trade": {
        "patcher_name": "old man trade",
        "region_id": "old man trade",
        "vanilla_item": "Megaphone",
        "flag_byte": 0xC7B7
    },
    "Mt. Cucco: Talon trade": {
        "patcher_name": "talon trade",
        "region_id": "talon trade",
        "vanilla_item": "Mushroom",
        "flag_byte": 0xCAB6,
        "bit_mask": 0x40
    },
    "Sunken City: Syrup trade": {
        "patcher_name": "syrup trade",
        "region_id": "syrup trade",
        "vanilla_item": "Wooden Bird",
        "flag_byte": 0xC89C
    },
    "Horon Village: Tick Tock trade": {
        "patcher_name": "tick tock trade",
        "region_id": "tick tock trade",
        "vanilla_item": "Engine Grease",
        "flag_byte": 0xC883
    },
    "Eastern Suburbs: Guru-Guru trade": {
        "patcher_name": "guru-guru trade",
        "region_id": "guru-guru trade",
        "vanilla_item": "Phonograph",
        "flag_byte": 0xC7DA
    },

    "Subrosia: buried bomb flower": {
        "patcher_name": "subrosian buried bomb flower",
        "region_id": "subrosian buried bomb flower",
        "vanilla_item": "bomb flower",
        "conditional": True,
        "flag_byte": 0xC869
    },
    "Subrosia: sign-loving guy reward": {
        "patcher_name": "subrosian sign guy",
        "region_id": "subrosian sign guy",
        "vanilla_item": "sign ring",
        "conditional": True,
        "flag_byte": 0xC8A9
    },
    # Maku seed is 0xC85D

    "Horon Village: Old Man": {
        "patcher_name": "old man in horon",
        "region_id": "old man in horon",
        "flag_byte": 0xCA05,
        "bit_mask": 0x40,
        "conditional": True
    },
    "North Horon: Old Man near D1": {
        "patcher_name": "old man near d1",
        "region_id": "old man near d1",
        "flag_byte": 0xCA03,
        "bit_mask": 0x40,
        "conditional": True
    },
    "North Horon: Old Man near Blaino's Gym": {
        "patcher_name": "old man near blaino",
        "region_id": "old man near blaino",
        "flag_byte": 0xCA02,
        "bit_mask": 0x40,
        "conditional": True
    },
    "Goron Mountain: Old Man": {
        "patcher_name": "old man in goron mountain",
        "region_id": "old man in goron mountain",
        "flag_byte": 0xCA01,
        "bit_mask": 0x40,
        "conditional": True
    },
    "Western Coast: Old Man": {
        "patcher_name": "old man near western coast house",
        "region_id": "old man near western coast house",
        "flag_byte": 0xCA04,
        "bit_mask": 0x40,
        "conditional": True
    },
    "Woods of Winter: Old Man": {
        "patcher_name": "old man near holly's house",
        "region_id": "old man near holly's house",
        "flag_byte": 0xCA07,
        "bit_mask": 0x40,
        "conditional": True
    },
    "Holodrum Plain: Old Man near Mrs. Ruul's house": {
        "patcher_name": "old man near mrs. ruul",
        "region_id": "old man near mrs. ruul",
        "flag_byte": 0xCA08,
        "bit_mask": 0x40,
        "conditional": True
    },
    "Tarm Ruins: Old Man near D6": {
        "patcher_name": "old man near d6",
        "region_id": "old man near d6",
        "flag_byte": 0xCA06,
        "bit_mask": 0x40,
        "conditional": True
    },

    "Horon Village: seed tree": {
        "patcher_name": "horon village tree",
        "region_id": "horon village tree",
        "local": True
    },
    "Woods of Winter: seed tree": {
        "patcher_name": "woods of winter tree",
        "region_id": "woods of winter tree",
        "local": True
    },
    "North Horon: seed tree": {
        "patcher_name": "north horon tree",
        "region_id": "north horon tree",
        "local": True
    },
    "Spool Swamp: seed tree": {
        "patcher_name": "spool swamp tree",
        "region_id": "spool swamp tree",
        "local": True
    },
    "Sunken City: seed tree": {
        "patcher_name": "sunken city tree",
        "region_id": "sunken city tree",
        "local": True
    },
    "Tarm Ruins: seed tree": {
        "patcher_name": "tarm ruins tree",
        "region_id": "tarm ruins tree",
        "local": True
    },

    "North Horon: golden beasts Old Man": {
        "patcher_name": "golden beasts old man",
        "region_id": "golden beasts old man",
        "vanilla_item": "Red Ring",
        "flag_byte": 0xCA11,
    }
}
