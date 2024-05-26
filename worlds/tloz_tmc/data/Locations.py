
BASE_LOCATION_ID = 27022001000

LOCATIONS_DATA = {
    "Smith House Chest": {
        "region_id": "Smith",
        "vanilla_item": "Rupee20",
        "flag_logic":0x22-0x11-0x00,
        "flag_byte": 0x2002CDE,
        "bit_mask": 0x40
    },
    "Smith Floor Item 1": {
        "region_id": "Smith",
        "vanilla_item": "SmithSword",
        "flag_logic":0x0F252B,
        "flag": 0x2002CDE,
        "bit_mask": 0x80

    },
    "Smith Floor Item 2": {
        "region_id": "Smith",
        "vanilla_item": "Shield",
        "flag_logic":0x0F253B,
        "flag": 0x2002CDF,
        "bit_mask": 0x01
    },
    "South Field Puddle Fusion Item1": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":	0x0F8283,
        "flag_byte": 0x2002D1E,
        "bit_mask": 0x20
	},
	"South Field Puddle Fusion Item2": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F8293,
        "flag_byte": 0x2002D1E,
        "bit_mask": 0x40
	},
	"South Field Puddle Fusion Item3": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F82A3,
        "flag_byte": 0x2002D1E,
        "bit_mask": 0x80
	},
	"South Field Puddle Fusion Item4": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F82B3,
        "flag_byte": 0x2002D1F,
        "bit_mask": 0x01
	},
	"South Field Puddle Fusion Item5": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F82C3,
        "flag_byte": 0x2002D1F,
        "bit_mask": 0x02
	},
	"South Field Puddle Fusion Item6": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F82D3,
        "flag_byte": 0x2002D1F,
        "bit_mask": 0x04
	},
	"South Field Puddle Fusion Item7": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F82E3,
        "flag_byte": 0x2002D1F,
        "bit_mask": 0x08
	},
	"South Field Puddle Fusion Item8": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F82F3,
        "flag_byte": 0x2002D1F,
        "bit_mask": 0x10
	},
	"South Field Puddle Fusion Item9": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F8303,
        "flag_byte": 0x2002D1F,
        "bit_mask": 0x20
	},
	"South Field Puddle Fusion Item10": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F8313,
        "flag_byte": 0x2002D1F,
        "bit_mask": 0x40
	},
	"South Field Puddle Fusion Item11": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F8323,
        "flag_byte": 0x2002D1F,
        "bit_mask": 0x80
	},
	"South Field Puddle Fusion Item12": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F8333,
        "flag_byte": 0x2002D20,
        "bit_mask": 0x01
	},
	"South Field Puddle Fusion Item13": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F8343,
        "flag_byte": 0x2002D20,
        "bit_mask": 0x02
	},
	"South Field Puddle Fusion Item14": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F8353,
        "flag_byte": 0x2002D20,
        "bit_mask": 0x04
	},
	"South Field Puddle Fusion Item15": {
		"region_id": "South Field",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F8363,
        "flag_byte": 0x2002D20,
        "bit_mask": 0x08
	},
	"South Field Fusion Chest": {
		"region_id": "South Field",
        "vanilla_item": "Shells",
        "flag_logic":0x0FE0D6,
        "flag_byte": 0x2002CD3,
        "bit_mask": 0x02
	},
	"South Field Tree Fusion HP": {
		"region_id": "South Field",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F9BA7,
        "flag_byte": 0x2002CEE,
        "bit_mask": 0x80
	},
	"South Field Minish Size Water Hole HP": {
		"region_id": "South Field",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0DB55F,
        "flag_byte": 0x2002D2C,
        "bit_mask": 0x02
	},
	"South Field Tingle NPC": {
		"region_id": "South Field",
        "vanilla_item": "TingleTrophy",
        "flag_logic":0x016966,
        "flag_byte": 0x2002CA3,
        "bit_mask": 0x04
	},
	"Town Cafe Lady NPC": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x00EDDA,
        "flag_byte": 0x2002CD6,
        "bit_mask": 0x10
	},
	"Town Shop 80 Item": {
		"region_id": "Town",
        "vanilla_item": "Wallet",
        "flag_logic":"walletShopItem:Define:FirstByte, walletShopSub:Define:SecondByte",
        "flag_byte": 0x2002CE6,
        "bit_mask": 0x20
	},
	"Town Shop 300 Item": {
		"region_id": "Town",
        "vanilla_item": "Boomerang",
        "flag_logic":"boomerangShopItem:Define:FirstByte, boomerangShopSub:Define:SecondByte",
        "flag_byte": 0x2002B34,
        "bit_mask": 0x40
	},
	"Town Shop 600 Item": {
		"region_id": "Town",
        "vanilla_item": "LargeQuiver",
        "flag_logic":"quiverShopItem:Define:FirstByte, quiverShopSub:Define:SecondByte",
        "flag_byte": 0x2002CE6,
        "bit_mask": 0x40
	},
	"Town Shop Behind Counter Item": {
		"region_id": "Town",
        "vanilla_item": "DogFoodBottle",
        "flag_logic":"dogShopItem:Define:FirstByte, dogShopSub:Define:SecondByte",
        "flag_byte": 0x2002B3F,
        "bit_mask": 0x10
	},
	"Town Shop Attic Chest": {
		"region_id": "Town",
        "vanilla_item": "Shells",
        "flag_logic":0x2E-0x01-0x01,
        "flag_byte": 0x2002D0A,
        "bit_mask": 0x80
	},
	"Town Bakery Attic Chest": {
		"region_id": "Town",
        "vanilla_item": "Rupee100",
        "flag_logic":0x2E-0x03-0x00,
        "flag_byte": 0x2002D13,
        "bit_mask": 0x20
	},
	"Town Inn Backdoor HP": {
		"region_id": "Town",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0D66D7,
        "flag_byte": 0x2002CF3,
        "bit_mask": 0x01
	},
	"Town Inn Ledge Chest": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x02-0x00-0x06,
        "flag_byte": 0x2002CD5,
        "bit_mask": 0x01
	},
	"Town Inn Pot": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"0x0D663B:FirstByte, 0x0D663D:SecondByte",
        "flag_byte": 0x2002CE0,
        "bit_mask": 0x80
	},
	"Town Well Right Chest": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x41-0x00-0x04,
        "flag_byte": 0x2002CFD,
        "bit_mask": 0x01
	},
	"Town Goron Merchant 1 Left": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron1LeftItem:Define:FirstByte,	goron1LeftSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 1 Middle": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron1MiddleItem:Define:FirstByte,	goron1MiddleSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 1 Right": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron1RightItem:Define:FirstByte,	goron1RightSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 2 Left": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron2LeftItem:Define:FirstByte,	goron2LeftSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 2 Middle": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron2MiddleItem:Define:FirstByte, goron2MiddleSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 2 Right": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron2RightItem:Define:FirstByte,	goron2RightSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 3 Left": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron3LeftItem:Define:FirstByte,	goron3LeftSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 3 Middle": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron3MiddleItem:Define:FirstByte,	goron3MiddleSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 3 Right": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron3RightItem:Define:FirstByte,	goron3RightSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 4 Left": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron4LeftItem:Define:FirstByte,	goron4LeftSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 4 Middle": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron4MiddleItem:Define:FirstByte,	goron4MiddleSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 4 Right": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron4RightItem:Define:FirstByte,	goron4RightSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 5 Left": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron5LeftItem:Define:FirstByte,	goron5LeftSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 5 Middle": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron5MiddleItem:Define:FirstByte,	goron5MiddleSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Goron Merchant 5 Right": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":"goron5RightItem:Define:FirstByte,	goron5RightSub:Define:SecondByte",
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Dojo NPC 1": {
		"region_id": "Town",
        "vanilla_item": "SpinAttack",
        "flag_logic":"swiftblade1DojoItem:Define:FirstByte, swiftblade1DojoSub:Define:SecondByte",
        "flag_byte": 0x2002EA5,
        "bit_mask": 0x10
	},
	"Town Dojo NPC 2": {
		"region_id": "Town",
        "vanilla_item": "RollAttack",
        "flag_logic":"swiftblade2DojoItem:Define:FirstByte, swiftblade2DojoSub:Define:SecondByte",
        "flag_byte": 0x2002EA5,
        "bit_mask": 0x20
	},
	"Town Dojo NPC 3": {
		"region_id": "Town",
        "vanilla_item": "DashAttack",
        "flag_logic":"swiftblade3DojoItem:Define:FirstByte, swiftblade3DojoSub:Define:SecondByte",
        "flag_byte": 0x2002EA5,
        "bit_mask": 0x40
	},
	"Town Dojo NPC 4": {
		"region_id": "Town",
        "vanilla_item": "DownThrust",
        "flag_logic":"swiftblade4DojoItem:Define:FirstByte, swiftblade4DojoSub:Define:SecondByte",
        "flag_byte": 0x2002EA5,
        "bit_mask": 0x80
	},
	"Town Well Top Chest": {
		"region_id": "Town",
        "vanilla_item": "Rupee100",
        "flag_logic":0x41-0x00-0x00,
        "flag_byte": 0x2002CFD,
        "bit_mask": 0x04
	},
	"Town School Roof Chest": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x02-0x00-0x07,
        "flag_byte": 0x2002CD5,
        "bit_mask": 0x02
	},
	"Town School Path Fusion Chest": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE076,
        "flag_byte": 0x2002D11,
        "bit_mask": 0x01
	},
	"Town School Path Left Chest": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x11-0x02-0x00,
        "flag_byte": 0x2002D0B,
        "bit_mask": 0x80
	},
	"Town School Path Middle Chest": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x11-0x02-0x01,
        "flag_byte": 0x2002D0C,
        "bit_mask": 0x01
	},
	"Town School Path Right Chest": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x11-0x02-0x02,
        "flag_byte": 0x2002D0C,
        "bit_mask": 0x02
	},
	"Town School Path HP": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0D5557,
        "flag_byte": 0x2002D0B,
        "bit_mask": 0x40
	},
	"Town Digging Top Chest": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0F-0x00-0x00,
        "flag_byte": 0x2002D04,
        "bit_mask": 0x04
	},
	"Town Digging Right Chest": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0F-0x00-0x01,
        "flag_byte": 0x2002D04,
        "bit_mask": 0x08
	},
	"Town Digging Left Chest": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0F-0x00-0x02,
        "flag_byte": 0x2002D04,
        "bit_mask": 0x10
	},
	"Town Well Left Chest": {
		"region_id": "Town",
        "vanilla_item": "Rupee100",
        "flag_logic":0x41-0x00-0x01,
        "flag_byte": 0x2002CFC,
        "bit_mask": 0x80
	},
	"Town Bell HP": {
		"region_id": "Town",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":"0x05D602:FirstByte, 0x5D604:SecondByte",
        "flag_byte": 0x2002CD5,
        "bit_mask": 0x20
	},
	"Town Waterfall Fusion Chest": {
		"region_id": "Town",
        "vanilla_item": "Shells",
        "flag_logic":0x32-0x0B-0x00,
        "flag_byte": 0x2002D1D,
        "bit_mask": 0x40
	},
	"Town Carlov NPC": {
		"region_id": "Town",
        "vanilla_item": "CarlovMedal",
        "flag_logic":"carlovSpotItem:Define:FirstByte, carlovSpotSub:Define:SecondByte",
        "flag_byte": 0x2002EA5,
        "bit_mask": 0x02
	},
	"Town Well Bottom Chest": {
		"region_id": "Town",
        "vanilla_item": "Rupee100",
        "flag_logic":0x41-0x00-0x02,
        "flag_byte": 0x2002CFD,
        "bit_mask": 0x02
	},
	"Town Cuccos Lv 1 NPC": {
		"region_id": "Town",
        "vanilla_item": "Shells",
        "flag_logic":0x1245E8,
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Cuccos Lv 2 NPC": {
		"region_id": "Town",
        "vanilla_item": "Shells",
        "flag_logic":0x1245EC,
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Cuccos Lv 3 NPC": {
		"region_id": "Town",
        "vanilla_item": "Shells",
        "flag_logic":0x1245F0,
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Cuccos Lv 4 NPC": {
		"region_id": "Town",
        "vanilla_item": "Shells",
        "flag_logic":0x1245F4,
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Cuccos Lv 5 NPC": {
		"region_id": "Town",
        "vanilla_item": "Shells30",
        "flag_logic":0x1245F8,
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Cuccos Lv 6 NPC": {
		"region_id": "Town",
        "vanilla_item": "Shells30",
        "flag_logic":0x1245FC,
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Cuccos Lv 7 NPC": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x124600,
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Cuccos Lv 8 NPC": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x124604,
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Cuccos Lv 9 NPC": {
		"region_id": "Town",
        "vanilla_item": "Kinstone",
        "flag_logic":0x124608,
        "flag_byte": 0x2002aaa,
        "bit_mask": 0xbb
	},
	"Town Cuccos Lv 10 NPC": {
		"region_id": "Town",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x12460C,
        "flag_byte": 0x2002CA5,
        "bit_mask": 0x80
	},
	"Town Jullieta Item": {
		"region_id": "Town",
        "vanilla_item": "RedBook",
        "flag_logic":"redBookItem:Define:FirstByte, redBookSub:Define:SecondByte",
        "flag_byte": 0x2002EA4,
        "bit_mask": 0x10
	},
	"Town Simulation Chest": {
		"region_id": "Town",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F04C2,
        "flag_byte": 0x2002C9C,
        "bit_mask": 0x02
	},
	"Town Shoe Shop NPC": {
		"region_id": "Town",
        "vanilla_item": "PegasusBoots",
        "flag_logic":0x0130EE,
        "flag_byte": 0x2002EA4,
        "bit_mask": 0x08
	},
	"Town Music House Left Chest": {
		"region_id": "Town",
        "vanilla_item": "Rupee200",
        "flag_logic":0x23-0x05-0x00,
        "flag_byte": 0x2002CF2,
        "bit_mask": 0x20
	},
	"Town Music House Middle Chest": {
		"region_id": "Town",
        "vanilla_item": "Rupee200",
        "flag_logic":0x23-0x05-0x01,
        "flag_byte": 0x2002CF2,
        "bit_mask": 0x40
	},
	"Town Music House Right Chest": {
		"region_id": "Town",
        "vanilla_item": "Rupee200",
        "flag_logic":0x23-0x05-0x02,
        "flag_byte": 0x2002CF2,
        "bit_mask": 0x80
	},
	"Town Music House HP": {
		"region_id": "Town",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F5407,
        "flag_byte": 0x2002CF2,
        "bit_mask": 0x10
	},
	"Town Well Pillar Chest": {
		"region_id": "Town",
        "vanilla_item": "Rupee200",
        "flag_logic":0x41-0x00-0x03,
        "flag_byte": 0x2002CFD,
        "bit_mask": 0x02
	},
	"Town Dr Left Attic Item": {
		"region_id": "Town",
        "vanilla_item": "GreenBook",
        "flag_logic":"greenBookItem:Define:FirstByte, greenBookSub:Define:SecondByte",
        "flag_byte": 0x2002EA4,
        "bit_mask": 0x20
	},
	"Town Fountain Big Chest": {
		"region_id": "Town",
        "vanilla_item": "PowerBracelets",
        "flag_logic":0x62-0x03-0x00,
        "flag_byte": 0x2002CFD,
        "bit_mask": 0x80
	},
	"Town Fountain Small Chest": {
		"region_id": "Town",
        "vanilla_item": "Rupee100",
        "flag_logic":0x62-0x04-0x00,
        "flag_byte": 0x2002CFE,
        "bit_mask": 0x01
	},
	"Town Fountain HP": {
		"region_id": "Town",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0EF3B7,
        "flag_byte": 0x2002D14,
        "bit_mask": 0x08
	},
	"Town Library Yellow Minish NPC": {
		"region_id": "Town",
        "vanilla_item": "Rupee50",
        "flag_logic":0x00E7BE,
        "flag_byte": 0x2002CEB,
        "bit_mask": 0x01
	},
	"Town Under Library Frozen Chest": {
		"region_id": "Town",
        "vanilla_item": "Shells",
        "flag_logic":0x62-0x12-0x00,
        "flag_byte": 0x2002CFE,
        "bit_mask": 0x20
	},
	"Town Under Library Big Chest": {
		"region_id": "Town",
        "vanilla_item": "Flippers",
        "flag_logic":0x62-0x10-0x00,
        "flag_byte": 0x2002CFE,
        "bit_mask": 0x10
	},
	"Town Under Library Underwater": {
		"region_id": "Town",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0EF79B,
        "flag_byte": 0x2002CFE,
        "bit_mask": 0x08
	},
	"North Field Dig Spot": {
		"region_id": "North Field",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0F720F,
        "flag_byte": 0x2002CCD,
        "bit_mask": 0x20
	},
	"North Field HP": {
		"region_id": "North Field",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F864B,
        "flag_byte": 0x2002D2B,
        "bit_mask": 0x08
	},
	"North Field Tree Fusion Top Left Chest": {
		"region_id": "North Field",
        "vanilla_item": "Kinstone",
        "flag_logic":0x32-0x00-0x00,
        "flag_byte": 0x2002D1C,
        "bit_mask": 0x10
	},
	"North Field Tree Fusion Top Right Chest": {
		"region_id": "North Field",
        "vanilla_item": "Kinstone",
        "flag_logic":0x32-0x00-0x01,
        "flag_byte": 0x2002D1C,
        "bit_mask": 0x20
	},
	"North Field Tree Fusion Bottom Left Chest": {
		"region_id": "North Field",
        "vanilla_item": "Kinstone",
        "flag_logic":0x32-0x00-0x02,
        "flag_byte": 0x2002D1C,
        "bit_mask": 0x40
	},
	"North Field Tree Fusion Bottom Right Chest": {
		"region_id": "North Field",
        "vanilla_item": "Shells",
        "flag_logic":0x32-0x00-0x03,
        "flag_byte": 0x2002D1C,
        "bit_mask": 0x80
	},
	"North Field Tree Fusion Center Big Chest": {
		"region_id": "North Field",
        "vanilla_item": "MagicBoomerang",
        "flag_logic":0x32-0x00-0x04,
        "flag_byte": 0x2002D1D,
        "bit_mask": 0x01
	},
	"North Field Waterfall Fusion Dojo NPC": {
		"region_id": "North Field",
        "vanilla_item": "LongSpin",
        "flag_logic":"greatbladeDojoItem:Define:FirstByte, greatbladeDojoSub:Define:SecondByte",
        "flag_byte": 0x2002EA6,
        "bit_mask": 0x20
	},
	"Castle Moat Left Chest": {
		"region_id": "Castle",
        "vanilla_item": "Shells",
        "flag_logic":0x07-0x00-0x01,
        "flag_byte": 0x2002CBE,
        "bit_mask": 0x04
	},
	"Castle Moat Right Chest": {
		"region_id": "Castle",
        "vanilla_item": "Rupee200",
        "flag_logic":0x07-0x00-0x02,
        "flag_byte": 0x2002CBE,
        "bit_mask": 0x08
	},
	"Castle Golden Rope": {
		"region_id": "Castle",
        "vanilla_item": "Rupee100",
        "flag_logic":"golden5Item:Define:FirstByte, golden5Sub:Define:SecondByte",
        "flag_byte": 0x2002CA2,
        "bit_mask": 0x20
	},
	"Castle Right Fountain Fusion HP": {
		"region_id": "Castle",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0D9C2B,
        "flag_byte": 0x2002D0E,
        "bit_mask": 0x10
	},
	"Castle Dojo HP": {
		"region_id": "Castle",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0D79BB,
        "flag_byte": 0x2002D2C,
        "bit_mask": 0x08
	},
	"Castle Dojo NPC": {
		"region_id": "Castle",
        "vanilla_item": "SwordBeam",
        "flag_logic":"grimbladeDojoItem:Define:FirstByte, grimbladeDojoSub:Define:SecondByte",
        "flag_byte": 0x2002EA6,
        "bit_mask": 0x02
	},
	"Castle Right Fountain Fusion Minish Hole Chest": {
		"region_id": "Castle",
        "vanilla_item": "Shells",
        "flag_logic":0x36-0x00-0x00,
        "flag_byte": 0x2002D28,
        "bit_mask": 0x10
	},
	"Castle Left Fountain Fusion Minish Hole Chest": {
		"region_id": "Castle",
        "vanilla_item": "Shells",
        "flag_logic":0x36-0x01-0x00,
        "flag_byte": 0x2002D28,
        "bit_mask": 0x20
	},
	"Hills Golden Rope": {
		"region_id": "Hills",
        "vanilla_item": "Rupee100",
        "flag_logic":"golden4Item:Define:FirstByte, golden4Sub:Define:SecondByte",
        "flag_byte": 0x2002CA2,
        "bit_mask": 0x10
	},
	"Hills Fusion Chest": {
		"region_id": "Hills",
        "vanilla_item": "Bottle",
        "flag_logic":0x0FE05E,
        "flag_byte": 0x2002CD2,
        "bit_mask": 0x04
	},
	"Hills Beanstalk Fusion Left Chest": {
		"region_id": "Hills",
        "vanilla_item": "Shells",
        "flag_logic":0x0D-0x03-0x01,
        "flag_byte": 0x2002D0D,
        "bit_mask": 0x02
	},
	"Hills Beanstalk Fusion HP": {
		"region_id": "Hills",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F6073,
        "flag_byte": 0x2002D0D,
        "bit_mask": 0x01
	},
	"Hills Beanstalk Fusion Right Chest": {
		"region_id": "Hills",
        "vanilla_item": "Rupee200",
        "flag_logic":0x0D-0x03-0x00,
        "flag_byte": 0x2002D0D,
        "bit_mask": 0x04
	},
	"Hills Bomb Cave Chest": {
		"region_id": "Hills",
        "vanilla_item": "Shells",
        "flag_logic":0x32-0x13-0x00,
        "flag_byte": 0x2002D22,
        "bit_mask": 0x08
	},
	"Minish Great Fairy NPC": {
		"region_id": "Minish",
        "vanilla_item": "Wallet",
        "flag_logic":0x00B7B4,
        "flag_byte": 0x2002CEF,
        "bit_mask": 0x80
	},
	"Hills Farm Dig Cave Item": {
		"region_id": "Hills",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F3C9F,
        "flag_byte": 0x2002CD2,
        "bit_mask": 0x04
	},
	"Lon Lon Ranch Pot": {
		"region_id": "Lon Lon",
        "vanilla_item": "LonLonKey",
        "flag_logic":"0x0F2C9B:FirstByte, 0x0F2C9D:SecondByte",
        "flag_byte": 0x2002CE5,
        "bit_mask": 0x20
	},
	"Lon Lon Puddle Fusion Big Chest": {
		"region_id": "Lon Lon",
        "vanilla_item": "Wallet",
        "flag_logic":0x32-0x0F-0x00,
        "flag_byte": 0x2002D1E,
        "bit_mask": 0x10
	},
	"Lon Lon Cave Chest": {
		"region_id": "Lon Lon",
        "vanilla_item": "Rupee50",
        "flag_logic":0x32-0x0C-0x00,
        "flag_byte": 0x2002D1D,
        "bit_mask": 0x80
	},
	"Lon Lon Cave Secret Chest": {
		"region_id": "Lon Lon",
        "vanilla_item": "Kinstone",
        "flag_logic":0x32-0x0D-0x00,
        "flag_byte": 0x2002D1E,
        "bit_mask": 0x04
	},
	"Lon Lon Path Fusion Chest": {
		"region_id": "Lon Lon",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE086,
        "flag_byte": 0x2002D11,
        "bit_mask": 0x02
	},
	"Lon Lon Path HP": {
		"region_id": "Lon Lon",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0D56EF,
        "flag_byte": 0x2002D13,
        "bit_mask": 0x04
	},
	"Lon Lon Dig Spot": {
		"region_id": "Lon Lon",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0F6CFF,
        "flag_byte": 0x2002CCB,
        "bit_mask": 0x20
	},
	"Lon Lon North Minish Crack Chest": {
		"region_id": "Lon Lon",
        "vanilla_item": "Kinstone",
        "flag_logic":0x27-0x00-0x00,
        "flag_byte": 0x2002CF2,
        "bit_mask": 0x04
	},
	"Lon Lon Goron Cave Fusion Small Chest": {
		"region_id": "Lon Lon",
        "vanilla_item": "Rupee200",
        "flag_logic":0x2F-0x01-0x00,
        "flag_byte": 0x2002D2A,
        "bit_mask": 0x80
	},
	"Lon Lon Goron Cave Fusion Big Chest": {
		"region_id": "Lon Lon",
        "vanilla_item": "Bottle",
        "flag_logic":0x2F-0x01-0x01,
        "flag_byte": 0x2002D2A,
        "bit_mask": 0x40
	},
	"Falls Lower Lon Lon Fusion Chest": {
		"region_id": "Falls Lower",
        "vanilla_item": "Rupee200",
        "flag_logic":0x0FE0FE,
        "flag_byte": 0x2002CD3,
        "bit_mask": 0x40
	},
	"Falls Lower HP": {
		"region_id": "Falls Lower",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F87D3,
        "flag_byte": 0x2002CD1,
        "bit_mask": 0x02
	},
	"Falls Lower Waterfall Fusion Dojo NPC": {
		"region_id": "Falls Lower",
        "vanilla_item": "FastSplit",
        "flag_logic":"splitbladeDojoItem:Define:FirstByte, splitbladeDojoSub:Define:SecondByte",
        "flag_byte": 0x2002EA6,
        "bit_mask": 0x20
	},
	"Falls Lower Rock Item1": {
		"region_id": "Falls Lower",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F87E3,
        "flag_byte": 0x2002CD0,
        "bit_mask": 0x04
	},
	"Falls Lower Rock Item2": {
		"region_id": "Falls Lower",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F87F3,
        "flag_byte": 0x2002CD0,
        "bit_mask": 0x08
	},
	"Falls Lower Rock Item3": {
		"region_id": "Falls Lower",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F8803,
        "flag_byte": 0x2002CD0,
        "bit_mask": 0x10
	},
	"Falls Lower Dig Cave Left Chest": {
		"region_id": "Falls Lower",
        "vanilla_item": "Shells",
        "flag_logic":0x16-0x00-0x01,
        "flag_byte": 0x2002D05,
        "bit_mask": 0x08
	},
	"Falls Lower Dig Cave Right Chest": {
		"region_id": "Falls Lower",
        "vanilla_item": "Rupee50",
        "flag_logic":0x16-0x00-0x02,
        "flag_byte": 0x2002D05,
        "bit_mask": 0x10
	},
	"Hylia Sunken HP": {
		"region_id": "Hylia",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F323B,
        "flag_byte": 0x2002CBD,
        "bit_mask": 0x02
	},
	"Hylia Dog NPC": {
		"region_id": "Hylia",
        "vanilla_item": "Bottle",
        "flag_logic":"0x094908:FirstByte, 0x09490A:SecondByte",
        "flag_byte": 0x2002B3F,
        "bit_mask": 0x20
	},
	"Hylia Small Island HP": {
		"region_id": "Hylia",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F322B,
        "flag_byte": 0x2002CBD,
        "bit_mask": 0x04
	},
	"Hylia Cape Cave Top Right": {
		"region_id": "Hylia",
        "vanilla_item": "Shells",
        "flag_logic":0x19-0x01-0x00,
        "flag_byte": 0x2002D02,
        "bit_mask": 0x80
	},
	"Hylia Cape Cave Bottom Left": {
		"region_id": "Hylia",
        "vanilla_item": "Shells",
        "flag_logic":0x19-0x01-0x02,
        "flag_byte": 0x2002D03,
        "bit_mask": 0x02
	},
	"Hylia Cape Cave Top Left": {
		"region_id": "Hylia",
        "vanilla_item": "Kinstone",
        "flag_logic":0x19-0x01-0x03,
        "flag_byte": 0x2002D03,
        "bit_mask": 0x04
	},
	"Hylia Cape Cave Top Middle": {
		"region_id": "Hylia",
        "vanilla_item": "Kinstone",
        "flag_logic":0x19-0x01-0x04,
        "flag_byte": 0x2002D03,
        "bit_mask": 0x08
	},
	"Hylia Cape Cave Right": {
		"region_id": "Hylia",
        "vanilla_item": "Kinstone",
        "flag_logic":0x19-0x01-0x05,
        "flag_byte": 0x2002D03,
        "bit_mask": 0x10
	},
	"Hylia Cape Cave Bottom Right": {
		"region_id": "Hylia",
        "vanilla_item": "Kinstone",
        "flag_logic":0x19-0x01-0x06,
        "flag_byte": 0x2002D03,
        "bit_mask": 0x20
	},
	"Hylia Cape Cave Bottom Middle": {
		"region_id": "Hylia",
        "vanilla_item": "Kinstone",
        "flag_logic":0x19-0x01-0x07,
        "flag_byte": 0x2002D03,
        "bit_mask": 0x40
	},
	"Hylia Cape Cave Lon Lon HP": {
		"region_id": "Hylia",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F6CEF,
        "flag_byte": 0x2002CCB,
        "bit_mask": 0x10
	},
	"Hylia Beanstalk Fusion Left Chest": {
		"region_id": "Hylia",
        "vanilla_item": "Rupee200",
        "flag_logic":0x0D-0x01-0x00,
        "flag_byte": 0x2002D0C,
        "bit_mask": 0x20
	},
	"Hylia Beanstalk Fusion HP": {
		"region_id": "Hylia",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F5EDB,
        "flag_byte": 0x2002D0C,
        "bit_mask": 0x10
	},
	"Hylia Beanstalk Fusion Right Chest": {
		"region_id": "Hylia",
        "vanilla_item": "Shells",
        "flag_logic":0x0D-0x01-0x01,
        "flag_byte": 0x2002D0C,
        "bit_mask": 0x40
	},
	"Hylia Middle Island Fusion Dig Cave Chest": {
		"region_id": "Hylia",
        "vanilla_item": "Rupee50",
        "flag_logic":0x19-0x00-0x00,
        "flag_byte": 0x2002D02,
        "bit_mask": 0x40
	},
	"Hylia Bottom HP": {
		"region_id": "Hylia",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F324B,
        "flag_byte": 0x2002CBD,
        "bit_mask": 0x02
	},
	"Hylia Dojo HP": {
		"region_id": "Hylia",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0D7B03,
        "flag_byte": 0x2002D2C,
        "bit_mask": 0x04
	},
	"Hylia Dojo NPC": {
		"region_id": "Hylia",
        "vanilla_item": "PerilBeam",
        "flag_logic":"wavebladeDojoItem:Define:FirstByte, wavebladeDojoSub:Define:SecondByte",
        "flag_byte": 0x2002EA6,
        "bit_mask": 0x04
	},
	"Hylia Crack Fusion Librari NPC": {
		"region_id": "Hylia",
        "vanilla_item": "HeartContainer",
        "flag_logic":0x0124EC,
        "flag_byte": 0x2002CF2,
        "bit_mask": 0x08
	},
	"Hylia North Minish Hole Chest": {
		"region_id": "Hylia",
        "vanilla_item": "Kinstone",
        "flag_logic":0x35-0x07-0x00,
        "flag_byte": 0x2002D2A,
        "bit_mask": 0x04
	},
	"Hylia South Minish Hole Chest": {
		"region_id": "Hylia",
        "vanilla_item": "Kinstone",
        "flag_logic":0x35-0x05-0x00,
        "flag_byte": 0x2002D28,
        "bit_mask": 0x04
	},
	"Hylia Cabin Path Fusion Chest": {
		"region_id": "Hylia",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE09E,
        "flag_byte": 0x2002D11,
        "bit_mask": 0x10
	},
	"Hylia Mayor Cabin Item": {
		"region_id": "Hylia",
        "vanilla_item": "BlueBook",
        "flag_logic":"blueBookItem:Define:FirstByte, blueBookSub:Define:SecondByte",
        "flag_byte": 0x2002EA4,
        "bit_mask": 0x40
	},
	"Minish Woods Golden Octo": {
		"region_id": "Minish Woods",
        "vanilla_item": "Rupee100",
        "flag_logic":"golden8Item:Define:FirstByte, golden8Sub:Define:SecondByte",
        "flag_byte": 0x2002CA3,
        "bit_mask": 0x01
	},
	"Minish Woods Witch Hut Item": {
		"region_id": "Minish Woods",
        "vanilla_item": "WakeUpMushroom",
        "flag_logic":0x0F94D7,
        "flag_byte": 0x2002EA4,
        "bit_mask": 0x04
	},
	"Witch Digging Cave Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0C-0x00-0x00,
        "flag_byte": 0x2002D02,
        "bit_mask": 0x08
	},
	"Minish Woods North Fusion Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE07E,
        "flag_byte": 0x2002CD2,
        "bit_mask": 0x08
	},
	"Minish Woods Top HP": {
		"region_id": "Minish Woods",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F4347,
        "flag_byte": 0x2002CC3,
        "bit_mask": 0x08
	},
	"Minish Woods West Fusion Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Rupee200",
        "flag_logic":0x0FE0CE,
        "flag_byte": 0x2002CD3,
        "bit_mask": 0x01
	},
	"Minish Woods Like Like Digging Cave Left Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0C-0x00-0x01,
        "flag_byte": 0x2002D02,
        "bit_mask": 0x10
	},
	"Minish Woods Like Like Digging Cave Right Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0C-0x00-0x02,
        "flag_byte": 0x2002D02,
        "bit_mask": 0x20
	},
	"Minish Woods East Fusion Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE0B6,
        "flag_byte": 0x2002CD2,
        "bit_mask": 0x20
	},
	"Minish Woods South Fusion Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE0C6,
        "flag_byte": 0x2002CD2,
        "bit_mask": 0x80
	},
	"Minish Woods Bottom HP": {
		"region_id": "Minish Woods",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F4357,
        "flag_byte": 0x2002CC3,
        "bit_mask": 0x10
	},
	"Minish Woods Crack Fusion Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Kinstone",
        "flag_logic":0x27-0x08-0x00,
        "flag_byte": 0x2002CF0,
        "bit_mask": 0x08
	},
	"Minish Woods Minish Path Fusion Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Rupee200",
        "flag_logic":0x0FE08E,
        "flag_byte": 0x2002D11,
        "bit_mask": 0x04
	},
	"Minish Village Barrel House Item": {
		"region_id": "Minish Village",
        "vanilla_item": "JabberNut",
        "flag_logic":0x0DA283,
        "flag_byte": 0x2002CF5,
        "bit_mask": 0x04
	},
	"Minish Village HP": {
		"region_id": "Minish Village",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0DBCC7,
        "flag_byte": 0x2002CF4,
        "bit_mask": 0x04
	},
	"Minish Woods Bomb Minish NPC 1": {
		"region_id": "Minish Woods",
        "vanilla_item": "BombBag",
        "flag_logic":0x00A00C,
        "flag_byte": 0x2002EA5,
        "bit_mask": 0x01
	},
	"Minish Woods Bomb Minish NPC 2": {
		"region_id": "Minish Woods",
        "vanilla_item": "RemoteBombs",
        "flag_logic":0x00A0A0,
        "flag_byte": 0x2002CF2,
        "bit_mask": 0x01
	},
	"Minish Woods Post Village Fusion Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE0A6,
        "flag_byte": 0x2002CDB,
        "bit_mask": 0x08
	},
	"Minish Woods Flipper Hole Middle Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Kinstone",
        "flag_logic":0x35-0x09-0x00,
        "flag_byte": 0x2002D2A,
        "bit_mask": 0x08
	},
	"Minish Woods Flipper Hole Right Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Kinstone",
        "flag_logic":0x35-0x09-0x01,
        "flag_byte": 0x2002D2A,
        "bit_mask": 0x10
	},
	"Minish Woods Flipper Hole Left Chest": {
		"region_id": "Minish Woods",
        "vanilla_item": "Kinstone",
        "flag_logic":0x35-0x09-0x02,
        "flag_byte": 0x2002D2A,
        "bit_mask": 0x20
	},
	"Minish Woods Flipper Hole HP": {
		"region_id": "Minish Woods",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0DB8BF,
        "flag_byte": 0x2002D2B,
        "bit_mask": 0x04
	},
	"Trilby Middle Fusion Chest": {
		"region_id": "Trilby",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE0EE,
        "flag_byte": 0x2002CD3,
        "bit_mask": 0x10
	},
	"Trilby Top Fusion Chest": {
		"region_id": "Trilby",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE0BE,
        "flag_byte": 0x2002CD2,
        "bit_mask": 0x40
	},
	"Trilby Dig Cave Left Chest": {
		"region_id": "Trilby",
        "vanilla_item": "Kinstone",
        "flag_logic":0x13-0x03-0x00,
        "flag_byte": 0x2002D04,
        "bit_mask": 0x80
	},
	"Trilby Dig Cave Right Chest": {
		"region_id": "Trilby",
        "vanilla_item": "Kinstone",
        "flag_logic":0x13-0x03-0x02,
        "flag_byte": 0x2002D05,
        "bit_mask": 0x02
	},
	"Trilby Dig Cave Water Fusion Chest": {
		"region_id": "Trilby",
        "vanilla_item": "Kinstone",
        "flag_logic":0x13-0x03-0x01,
        "flag_byte": 0x2002D05,
        "bit_mask": 0x01
	},
	"Trilby Scrub NPC": {
		"region_id": "Trilby",
        "vanilla_item": "Bottle",
        "flag_logic":"bottleScrubItem:Define:FirstByte, bottleScrubSub:Define:SecondByte",
        "flag_byte": 0x2002CA7,
        "bit_mask": 0x04
	},
	"Trilby Bomb Cave Chest": {
		"region_id": "Trilby",
        "vanilla_item": "Kinstone",
        "flag_logic":0x32-0x07-0x00,
        "flag_byte": 0x2002D1D,
        "bit_mask": 0x20
	},
	"Trilby Puddle Fusion Item1": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F83BB,
        "flag_byte": 0x2002D20,
        "bit_mask": 0x10
	},
	"Trilby Puddle Fusion Item2": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F83CB,
        "flag_byte": 0x2002D20,
        "bit_mask": 0x20
	},
	"Trilby Puddle Fusion Item3": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F83DB,
        "flag_byte": 0x2002D20,
        "bit_mask": 0x40
	},
	"Trilby Puddle Fusion Item4": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F83EB,
        "flag_byte": 0x2002D20,
        "bit_mask": 0x80
	},
	"Trilby Puddle Fusion Item5": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F83FB,
        "flag_byte": 0x2002D21,
        "bit_mask": 0x01
	},
	"Trilby Puddle Fusion Item6": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F840B,
        "flag_byte": 0x2002D21,
        "bit_mask": 0x02
	},
	"Trilby Puddle Fusion Item7": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F841B,
        "flag_byte": 0x2002D21,
        "bit_mask": 0x04
	},
	"Trilby Puddle Fusion Item8": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F842B,
        "flag_byte": 0x2002D21,
        "bit_mask": 0x08
	},
	"Trilby Puddle Fusion Item9": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F843B,
        "flag_byte": 0x2002D21,
        "bit_mask": 0x10
	},
	"Trilby Puddle Fusion Item10": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F844B,
        "flag_byte": 0x2002D21,
        "bit_mask": 0x20
	},
	"Trilby Puddle Fusion Item11": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F845B,
        "flag_byte": 0x2002D21,
        "bit_mask": 0x40
	},
	"Trilby Puddle Fusion Item12": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F846B,
        "flag_byte": 0x2002D21,
        "bit_mask": 0x80
	},
	"Trilby Puddle Fusion Item13": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F847B,
        "flag_byte": 0x2002D22,
        "bit_mask": 0x01
	},
	"Trilby Puddle Fusion Item14": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F848B,
        "flag_byte": 0x2002D22,
        "bit_mask": 0x02
	},
	"Trilby Puddle Fusion Item15": {
		"region_id": "Trilby",
        "vanilla_item" : "Rupee5",
        "flag_logic":0x0F849B,
        "flag_byte": 0x2002D22,
        "bit_mask": 0x04
	},
	"Western Woods Fusion Chest": {
		"region_id": "Western Woods",
        "vanilla_item": "Shells",
        "flag_logic":0x03-0x08-0x01,
        "flag_byte": 0x2002CCF,
        "bit_mask": 0x10
	},
	"Western Woods Tree Fusion HP": {
		"region_id": "Western Woods",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F9E1F,
        "flag_byte": 0x2002CEF,
        "bit_mask": 0x01
	},
	"Western Woods Top Dig1": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0F77CF,
        "flag_byte": 0x2002CCE,
        "bit_mask": 0x08
	},
	"Western Woods Top Dig2": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0F77DF,
        "flag_byte": 0x2002CCE,
        "bit_mask": 0x10
	},
	"Western Woods Top Dig3": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0F77EF,
        "flag_byte": 0x2002CCE,
        "bit_mask": 0x20
	},
	"Western Woods Top Dig4": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0F77FF,
        "flag_byte": 0x2002CCE,
        "bit_mask": 0x40
	},
	"Western Woods Top Dig5": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0F780F,
        "flag_byte": 0x2002CCE,
        "bit_mask": 0x80
	},
	"Western Woods Top Dig6": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0F781F,
        "flag_byte": 0x2002CCF,
        "bit_mask": 0x01
	},
	"Western Woods Percy Fusion Moblin": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0123D6,
        "flag_byte": 0x2002CE4,
        "bit_mask": 0x04
	},
	"Western Woods Percy Fusion Percy": {
		"region_id": "Western Woods",
        "vanilla_item": "Shells",
        "flag_logic":"0x06B058:FirstByte, 0x06B05A:SecondByte",
        "flag_byte": 0x2002CE3,
        "bit_mask": 0x80
	},
	"Western Woods Bottom Dig1": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee200",
        "flag_logic":0x0F782F,
        "flag_byte": 0x2002CCF,
        "bit_mask": 0x02
	},
	"Western Woods Bottom Dig2": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee200",
        "flag_logic":0x0F783F,
        "flag_byte": 0x2002CCF,
        "bit_mask": 0x04
	},
	"Western Woods Golden Octo": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee100",
        "flag_logic":"golden9Item:Define:FirstByte, golden9Sub:Define:SecondByte",
        "flag_byte": 0x2002CA3,
        "bit_mask": 0x02
	},
	"Western Woods Beanstalk Fusion Chest": {
		"region_id": "Western Woods",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0D-0x04-0x00,
        "flag_byte": 0x2002D0D,
        "bit_mask": 0x08
	},
	"Western Woods Beanstalk Fusion Item1": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F6143,
        "flag_byte": 0x2002D0D,
        "bit_mask": 0x10
	},
	"Western Woods Beanstalk Fusion Item2": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F6153,
        "flag_byte": 0x2002D0D,
        "bit_mask": 0x20
	},
	"Western Woods Beanstalk Fusion Item3": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F6163,
        "flag_byte": 0x2002D0D,
        "bit_mask": 0x40
	},
	"Western Woods Beanstalk Fusion Item4": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F6173,
        "flag_byte": 0x2002D0D,
        "bit_mask": 0x80
	},
	"Western Woods Beanstalk Fusion Item5": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F6183,
        "flag_byte": 0x2002D0E,
        "bit_mask": 0x01
	},
	"Western Woods Beanstalk Fusion Item6": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F6193,
        "flag_byte": 0x2002D0E,
        "bit_mask": 0x02
	},
	"Western Woods Beanstalk Fusion Item7": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F61A3,
        "flag_byte": 0x2002D0E,
        "bit_mask": 0x04
	},
	"Western Woods Beanstalk Fusion Item8": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F61B3,
        "flag_byte": 0x2002D0E,
        "bit_mask": 0x08
	},
	"Western Woods Beanstalk Fusion Item9": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F61C3,
        "flag_byte": 0x2002D0F,
        "bit_mask": 0x40
	},
	"Western Woods Beanstalk Fusion Item10": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F61D3,
        "flag_byte": 0x2002D0F,
        "bit_mask": 0x80
	},
	"Western Woods Beanstalk Fusion Item11": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F61E3,
        "flag_byte": 0x2002D10,
        "bit_mask": 0x01
	},
	"Western Woods Beanstalk Fusion Item12": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F61F3,
        "flag_byte": 0x2002D10,
        "bit_mask": 0x02
	},
	"Western Woods Beanstalk Fusion Item13": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F6203,
        "flag_byte": 0x2002D10,
        "bit_mask": 0x04
	},
	"Western Woods Beanstalk Fusion Item14": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F6213,
        "flag_byte": 0x2002D10,
        "bit_mask": 0x08
	},
	"Western Woods Beanstalk Fusion Item15": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F6223,
        "flag_byte": 0x2002D10,
        "bit_mask": 0x10
	},
	"Western Woods Beanstalk Fusion Item16": {
		"region_id": "Western Woods",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F6233,
        "flag_byte": 0x2002D10,
        "bit_mask": 0x20
	},
	"Crenel Base Entrance Vine": {
		"region_id": "Crenel Base",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0FAACF,
        "flag_byte": 0x2002CC5,
        "bit_mask": 0x02
	},
	"Crenel Base Fairy Cave Item1": {
		"region_id": "Crenel Base",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0FB3F3,
        "flag_byte": 0x2002D24,
        "bit_mask": 0x08
	},
	"Crenel Base Fairy Cave Item2": {
		"region_id": "Crenel Base",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0FB403,
        "flag_byte": 0x2002D24,
        "bit_mask": 0x10
	},
	"Crenel Base Fairy Cave Item3": {
		"region_id": "Crenel Base",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0FB413,
        "flag_byte": 0x2002D24,
        "bit_mask": 0x20
	},
	"Crenel Base Green Water Fusion Chest": {
		"region_id": "Crenel Base",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE06E,
        "flag_byte": 0x2002D10,
        "bit_mask": 0x80
	},
	"Crenel Base West Fusion Chest": {
		"region_id": "Crenel Base",
        "vanilla_item": "Rupee200",
        "flag_logic":0x0FE116,
        "flag_byte": 0x2002CD4,
        "bit_mask": 0x02
	},
	"Crenel Base Water Cave Left Chest": {
		"region_id": "Crenel Base",
        "vanilla_item": "Rupee50",
        "flag_logic":0x26-0x08-0x00,
        "flag_byte": 0x2002D24,
        "bit_mask": 0x02
	},
	"Crenel Base Water Cave Right Chest": {
		"region_id": "Crenel Base",
        "vanilla_item": "Kinstone",
        "flag_logic":0x26-0x08-0x01,
        "flag_byte": 0x2002D24,
        "bit_mask": 0x04
	},
	"Crenel Base Water Cave HP": {
		"region_id": "Crenel Base",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0FB32B,
        "flag_byte": 0x2002D24,
        "bit_mask": 0x01
	},
	"Crenel Base Minish Vine Hole Chest": {
		"region_id": "Crenel Base",
        "vanilla_item": "Kinstone",
        "flag_logic":0x35-0x00-0x00,
        "flag_byte": 0x2002D28,
        "bit_mask": 0x01
	},
	"Crenel Base Minish Crack Chest": {
		"region_id": "Crenel Base",
        "vanilla_item": "Kinstone",
        "flag_logic":0x27-0x03-0x00,
        "flag_byte": 0x2002CDE,
        "bit_mask": 0x02
	},
	"Crenel Vine Top Golden Tektite": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee100",
        "flag_logic":"golden2Item:Define:FirstByte, golden2Sub:Define:SecondByte",
        "flag_byte": 0x2002CA2,
        "bit_mask": 0x80
	},
	"Crenel Bridge Cave Chest": {
		"region_id": "Crenel",
        "vanilla_item": "Kinstone",
        "flag_logic":0x26-0x07-0x00,
        "flag_byte": 0x2002D23,
        "bit_mask": 0x80
	},
	"Crenel Fairy Cave HP": {
		"region_id": "Crenel",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0FB0BB,
        "flag_byte": 0x2002D2B,
        "bit_mask": 0x20
	},
	"Crenel Below CoF Golden Tektite": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee100",
        "flag_logic":"golden7Item:Define:FirstByte, golden7Sub:Define:SecondByte",
        "flag_byte": 0x2002CA2,
        "bit_mask": 0x04
	},
	"Crenel Scrub NPC": {
		"region_id": "Crenel",
        "vanilla_item": "GripRing",
        "flag_logic":"gripScrubItem:Define:FirstByte, gripScrubSub:Define:SecondByte",
        "flag_byte": 0x2002EA5,
        "bit_mask": 0x04
	},
	"Crenel Dojo Left Chest": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee50",
        "flag_logic":0x25-0x00-0x00,
        "flag_byte": 0x2002D1C,
        "bit_mask": 0x02
	},
	"Crenel Dojo Right Chest": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee50",
        "flag_logic":0x25-0x00-0x01,
        "flag_byte": 0x2002D1C,
        "bit_mask": 0x04
	},
	"Crenel Dojo HP": {
		"region_id": "Crenel",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0D752B,
        "flag_byte": 0x2002D2C,
        "bit_mask": 0x01
	},
	"Crenel Dojo NPC": {
		"region_id": "Crenel",
        "vanilla_item": "RollAttack",
        "flag_logic":"graybladeDojoItem:Define:FirstByte, graybladeDojoSub:Define:SecondByte",
        "flag_byte": 0x2002EA6,
        "bit_mask": 0x01
	},
	"Crenel Great Fairy NPC": {
		"region_id": "Crenel",
        "vanilla_item": "BombBag",
        "flag_logic":0x00B828,
        "flag_byte": 0x2002CF0,
        "bit_mask": 0x01
	},
	"Crenel Climb Fusion Chest": {
		"region_id": "Crenel",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE10E,
        "flag_byte": 0x2002CD4,
        "bit_mask": 0x01
	},
	"Crenel Dig Cave HP": {
		"region_id": "Crenel",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F3BA7,
        "flag_byte": 0x2002D04,
        "bit_mask": 0x20
	},
	"Crenel Beanstalk Fusion HP": {
		"region_id": "Crenel",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F5D9B,
        "flag_byte": 0x2002D0C,
        "bit_mask": 0x08
	},
	"Crenel Beanstalk Fusion Item1": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F5DAB,
        "flag_byte": 0x2002D0E,
        "bit_mask": 0x40
	},
	"Crenel Beanstalk Fusion Item2": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F5DBB,
        "flag_byte": 0x2002D0E,
        "bit_mask": 0x80
	},
	"Crenel Beanstalk Fusion Item3": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F5DCB,
        "flag_byte": 0x2002D0F,
        "bit_mask": 0x01
	},
	"Crenel Beanstalk Fusion Item4": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F5DDB,
        "flag_byte": 0x2002D0F,
        "bit_mask": 0x02
	},
	"Crenel Beanstalk Fusion Item5": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F5DEB,
        "flag_byte": 0x2002D0F,
        "bit_mask": 0x04
	},
	"Crenel Beanstalk Fusion Item6": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F5DFB,
        "flag_byte": 0x2002D0F,
        "bit_mask": 0x08
	},
	"Crenel Beanstalk Fusion Item7": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F5E0B,
        "flag_byte": 0x2002D0F,
        "bit_mask": 0x10
	},
	"Crenel Beanstalk Fusion Item8": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F5E1B,
        "flag_byte": 0x2002D0F,
        "bit_mask": 0x20
	},
	"Crenel Rain Path Fusion Chest": {
		"region_id": "Crenel",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE066,
        "flag_byte": 0x2002D10,
        "bit_mask": 0x40
	},
	"Crenel Upper Block Chest": {
		"region_id": "Crenel",
        "vanilla_item": "Kinstone",
        "flag_logic":0x26-0x03-0x00,
        "flag_byte": 0x2002D23,
        "bit_mask": 0x20
	},
	"Crenel Mines Path Fusion Chest": {
		"region_id": "Crenel",
        "vanilla_item": "Shells",
        "flag_logic":0x0FE096,
        "flag_byte": 0x2002D11,
        "bit_mask": 0x08
	},
	"Crenel Melari Lower Middle Dig": {
		"region_id": "Crenel",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0DC8C3,
        "flag_byte": 0x2002CF3,
        "bit_mask": 0x02
	},
	"Crenel Melari Very Bottom Dig": {
		"region_id": "Crenel",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0DC933,
        "flag_byte": 0x2002CF3,
        "bit_mask": 0x04
	},
	"Crenel Melari Upper Middle Left Dig": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0DC923,
        "flag_byte": 0x2002CF3,
        "bit_mask": 0x08
	},
	"Crenel Melari Upper Middle Middle Dig": {
		"region_id": "Crenel",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0DC913,
        "flag_byte": 0x2002CF3,
        "bit_mask": 0x10
	},
	"Crenel Melari Upper Middle Right Dig": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0DC903,
        "flag_byte": 0x2002CF3,
        "bit_mask": 0x20
	},
	"Crenel Melari Upper Top Right Dig": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0DC8F3,
        "flag_byte": 0x2002CF3,
        "bit_mask": 0x40
	},
	"Crenel Melari Upper Top Middle Dig": {
		"region_id": "Crenel",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0DC8D3,
        "flag_byte": 0x2002CF3,
        "bit_mask": 0x80
	},
	"Crenel Melari Upper Top Left Dig": {
		"region_id": "Crenel",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0DC8E3,
        "flag_byte": 0x2002CF4,
        "bit_mask": 0x01
	},
	"Swamp Butterfly Fusion Item": {
		"region_id": "Swamp",
        "vanilla_item": "DigButterfly",
        "flag_logic":0x0FE13F,
        "flag_byte": 0x2002EA7,
        "bit_mask": 0x10
	},
	"Swamp Center Cave Darknut Chest": {
		"region_id": "Swamp",
        "vanilla_item": "KinstoneSwamp",
        "flag_logic":0x2B-0x00-0x00,
        "flag_byte": 0x2002D23,
        "bit_mask": 0x04
	},
	"Swamp Center Chest": {
		"region_id": "Swamp",
        "vanilla_item": "Kinstone",
        "flag_logic":0x04-0x00-0x00,
        "flag_byte": 0x2002CBD,
        "bit_mask": 0x10
	},
	"Swamp Golden Rope": {
		"region_id": "Swamp",
        "vanilla_item": "Rupee100",
        "flag_logic":"golden3Item:Define:FirstByte, golden3Sub:Define:SecondByte",
        "flag_byte": 0x2002CA2,
        "bit_mask": 0x08
	},
	"Swamp Near Waterfall Cave HP": {
		"region_id": "Swamp",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0D9907,
        "flag_byte": 0x2002D23,
        "bit_mask": 0x01
	},
	"Swamp Waterfall Fusion Dojo NPC": {
		"region_id": "Swamp",
        "vanilla_item": "FastSpin",
        "flag_logic":"scarbladeDojoItem:Define:FirstByte, scarbladeDojoSub:Define:SecondByte",
        "flag_byte": 0x2002EA6,
        "bit_mask": 0x10
	},
	"Swamp North Cave Chest": {
		"region_id": "Swamp",
        "vanilla_item": "KinstoneSwamp",
        "flag_logic":0x2A-0x01-0x00,
        "flag_byte": 0x2002D22,
        "bit_mask": 0x40
	},
	"Swamp Digging Cave Left Chest": {
		"region_id": "Swamp",
        "vanilla_item": "Shells",
        "flag_logic":0x17-0x00-0x00,
        "flag_byte": 0x2002D04,
        "bit_mask": 0x01
	},
	"Swamp Digging Cave Right Chest": {
		"region_id": "Swamp",
        "vanilla_item": "Kinstone",
        "flag_logic":0x17-0x00-0x01,
        "flag_byte": 0x2002D04,
        "bit_mask": 0x02
	},
	"Swamp Underwater Top": {
		"region_id": "Swamp",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0D9347,
        "flag_byte": 0x2002CC0,
        "bit_mask": 0x04
	},
	"Swamp Underwater Middle": {
		"region_id": "Swamp",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0D9357,
        "flag_byte": 0x2002CC0,
        "bit_mask": 0x08
	},
	"Swamp Underwater Bottom": {
		"region_id": "Swamp",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0D9367,
        "flag_byte": 0x2002CC0,
        "bit_mask": 0x10
	},
	"Swamp South Cave Chest": {
		"region_id": "Swamp",
        "vanilla_item": "KinstoneSwamp",
        "flag_logic":0x2A-0x00-0x00,
        "flag_byte": 0x2002D22,
        "bit_mask": 0x10
	},
	"Swamp Dojo HP": {
		"region_id": "Swamp",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0D78CB,
        "flag_byte": 0x2002D2B,
        "bit_mask": 0x80
	},
	"Swamp Dojo NPC": {
		"region_id": "Swamp",
        "vanilla_item": "GreatSpin",
        "flag_logic":"swiftbladeIDojoItem:Define:FirstByte, swiftbladeIDojoSub:Define:SecondByte",
        "flag_byte": 0x2002EA6,
        "bit_mask": 0x08
	},
	"Swamp Minish Fusion North Crack Chest": {
		"region_id": "Swamp",
        "vanilla_item": "Kinstone",
        "flag_logic":0x27-0x09-0x00,
        "flag_byte": 0x2002CDE,
        "bit_mask": 0x08
	},
	"Swamp Minish Mulldozer Big Chest": {
		"region_id": "Swamp",
        "vanilla_item": "Bow",
        "flag_logic":0x27-0x06-0x00,
        "flag_byte": 0x2002CDE,
        "bit_mask": 0x01
	},
	"Swamp Minish Fusion North West Crack Chest": {
		"region_id": "Swamp",
        "vanilla_item": "Kinstone",
        "flag_logic":0x27-0x0D-0x00,
        "flag_byte": 0x2002CF0,
        "bit_mask": 0x20
	},
	"Swamp Minish Fusion West Crack Chest": {
		"region_id": "Swamp",
        "vanilla_item": "Kinstone",
        "flag_logic":0x27-0x0A-0x00,
        "flag_byte": 0x2002CDE,
        "bit_mask": 0x10
	},
	"Swamp Minish Fusion Vine Crack Chest": {
		"region_id": "Swamp",
        "vanilla_item": "Kinstone",
        "flag_logic":0x27-0x0B-0x00,
        "flag_byte": 0x2002CDE,
        "bit_mask": 0x20
	},
	"Swamp Minish Fusion Water Hole Chest": {
		"region_id": "Swamp",
        "vanilla_item": "Kinstone",
        "flag_logic":0x35-0x01-0x00,
        "flag_byte": 0x2002D2C,
        "bit_mask": 0x20
	},
	"Swamp Minish Fusion Water Hole HP": {
		"region_id": "Swamp",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0DB3F7,
        "flag_byte": 0x2002D2C,
        "bit_mask": 0x10
	},
	"Ruins Butterfly Fusion Item": {
		"region_id": "Ruins",
        "vanilla_item": "ArrowButterfly",
        "flag_logic":0x0FE12F,
        "flag_byte": 0x2002EA7,
        "bit_mask": 0x08
	},
	"Ruins Bomb Cave Chest": {
		"region_id": "Ruins",
        "vanilla_item": "Kinstone",
        "flag_logic":0x2A-0x02-0x00,
        "flag_byte": 0x2002D22,
        "bit_mask": 0x80
	},
	"Ruins Minish Home Chest": {
		"region_id": "Ruins",
        "vanilla_item": "Kinstone",
        "flag_logic":0x27-0x07-0x00,
        "flag_byte": 0x2002CDE,
        "bit_mask": 0x04
	},
	"Ruins Pillars Fusion Chest": {
		"region_id": "Ruins",
        "vanilla_item": "Shells",
        "flag_logic":0x0FE11E,
        "flag_byte": 0x2002CD4,
        "bit_mask": 0x04
	},
	"Ruins Bean Stalk Fusion Big Chest": {
		"region_id": "Ruins",
        "vanilla_item": "LargeQuiver",
        "flag_logic":0x0D-0x02-0x00,
        "flag_byte": 0x2002D0C,
        "bit_mask": 0x80
	},
	"Ruins Crack Fusion Chest": {
		"region_id": "Ruins",
        "vanilla_item": "Kinstone",
        "flag_logic":0x27-0x0C-0x00,
        "flag_byte": 0x2002CF0,
        "bit_mask": 0x10
	},
	"Ruins Minish Cave HP": {
		"region_id": "Ruins",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0DB4BF,
        "flag_byte": 0x2002D2B,
        "bit_mask": 0x40
	},
	"Ruins Armos Kill Left Chest": {
		"region_id": "Ruins",
        "vanilla_item": "Rupee50",
        "flag_logic":0x05-0x05-0x00,
        "flag_byte": 0x2002CC2,
        "bit_mask": 0x08
	},
	"Ruins Armos Kill Right Chest": {
		"region_id": "Ruins",
        "vanilla_item": "Shells",
        "flag_logic":0x05-0x05-0x01,
        "flag_byte": 0x2002CC2,
        "bit_mask": 0x10
	},
	"Ruins Golden Octo": {
		"region_id": "Ruins",
        "vanilla_item": "Rupee100",
        "flag_logic":"golden1Item:Define:FirstByte, golden1Sub:Define:SecondByte",
        "flag_byte": 0x2002CA2,
        "bit_mask": 0x02
	},
	"Ruins Near FoW Fusion Chest": {
		"region_id": "Ruins",
        "vanilla_item": "BombBag",
        "flag_logic":0x0FE0AE,
        "flag_byte": 0x2002CD2,
        "bit_mask": 0x10
	},
	"Valley Pre Valley Fusion Chest": {
		"region_id": "Valley",
        "vanilla_item": "Shells",
        "flag_logic":0x0FE0F6,
        "flag_byte": 0x2002CD3,
        "bit_mask": 0x20
	},
	"Valley Great Fairy NPC": {
		"region_id": "Valley",
        "vanilla_item": "LargeQuiver",
        "flag_logic":0x00B722,
        "flag_byte": 0x2002CEF,
        "bit_mask": 0x40
	},
	"Valley Lost Woods Chest": {
		"region_id": "Valley",
        "vanilla_item": "Shells",
        "flag_logic":0x0D8A86,
        "flag_byte": 0x2002CC7,
        "bit_mask": 0x04
	},
	"Valley Dampe NPC": {
		"region_id": "Valley",
        "vanilla_item": "GraveyardKey",
        "flag_logic":0x0096B6,
        "flag_byte": 0x2002CE9,
        "bit_mask": 0x02
	},
	"Valley Graveyard Butterfly Fusion Item": {
		"region_id": "Valley",
        "vanilla_item": "SwimButterfly",
        "flag_logic":0x0FE14F,
        "flag_byte": 0x2002EA7,
        "bit_mask": 0x20
	},
	"Valley Graveyard Left Fusion Chest": {
		"region_id": "Valley",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE0DE,
        "flag_byte": 0x2002CD3,
        "bit_mask": 0x04
	},
	"Valley Graveyard Left Grave HP": {
		"region_id": "Valley",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0D8AE7,
        "flag_byte": 0x2002D27,
        "bit_mask": 0x20
	},
	"Valley Graveyard Right Fusion Chest": {
		"region_id": "Valley",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE0E6,
        "flag_byte": 0x2002CD3,
        "bit_mask": 0x08
	},
	"Valley Graveyard Right Grave Fusion Chest": {
		"region_id": "Valley",
        "vanilla_item": "Shells",
        "flag_logic":0x34-0x01-0x00,
        "flag_byte": 0x2002D27,
        "bit_mask": 0x40
	},
	"Crypt Gibdo Left Item": {
		"region_id": "Crypt",
        "vanilla_item": "Bombs5",
        "flag_logic":0x0E688B,
        "flag_byte": 0x2002D14,
        "bit_mask": 0x10
	},
	"Crypt Gibdo Right Item": {
		"region_id": "Crypt",
        "vanilla_item": "SmallKey (Crypt Royal)",
        "flag_logic":0x0E68AB,
        "flag_byte": 0x2002D14,
        "bit_mask": 0x20
	},
	"Crypt Left Item": {
		"region_id": "Crypt",
        "vanilla_item": "SmallKey (Crypt Royal)",
        "flag_logic":0x0E6357,
        "flag_byte": 0x2002D12,
        "bit_mask": 0x40
	},
	"Crypt Right Item": {
		"region_id": "Crypt",
        "vanilla_item": "SmallKey (Crypt Royal)",
        "flag_logic":0x0E63A7,
        "flag_byte": 0x2002D12,
        "bit_mask": 0x80
	},
	"Crypt Prize": {
		"region_id": "Crypt",
        "vanilla_item": "KinstoneFalls",
        "flag_logic":0x00DA5A,
        "flag_byte": 0x2002D02,
        "bit_mask": 0x04
	},
	"Falls Entrance HP": {
		"region_id": "Falls",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F87C3,
        "flag_byte": 0x2002CD0,
        "bit_mask": 0x01
	},
	"Falls Water Dig Cave Fusion HP": {
		"region_id": "Falls",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F3DD7,
        "flag_byte": 0x2002D05,
        "bit_mask": 0x20
	},
	"Falls Water Dig Cave Fusion Chest": {
		"region_id": "Falls",
        "vanilla_item": "Shells",
        "flag_logic":0x16-0x00-0x00,
        "flag_byte": 0x2002D05,
        "bit_mask": 0x04
	},
	"Falls 1st Cave Chest": {
		"region_id": "Falls",
        "vanilla_item": "Shells",
        "flag_logic":0x33-0x05-0x00,
        "flag_byte": 0x2002D25,
        "bit_mask": 0x10
	},
	"Falls Cliff Chest": {
		"region_id": "Falls",
        "vanilla_item": "Shells",
        "flag_logic":0x0A-0x00-0x00,
        "flag_byte": 0x2002CD0,
        "bit_mask": 0x02
	},
	"Falls South Dig Spot": {
		"region_id": "Falls",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0F8823,
        "flag_byte": 0x2002CDA,
        "bit_mask": 0x80
	},
	"Falls Golden Tektite": {
		"region_id": "Falls",
        "vanilla_item": "Rupee100",
        "flag_logic":"golden6Item:Define:FirstByte, golden6Sub:Define:SecondByte",
        "flag_byte": 0x2002CA2,
        "bit_mask": 0x40
	},
	"Falls North Dig Spot": {
		"region_id": "Falls",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0F8813,
        "flag_byte": 0x2002CD0,
        "bit_mask": 0x80
	},
	"Falls Rock Fusion Chest": {
		"region_id": "Falls",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0FE106,
        "flag_byte": 0x2002CD3,
        "bit_mask": 0x80
	},
	"Falls Waterfall Fusion HP": {
		"region_id": "Falls",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0F906F,
        "flag_byte": 0x2002D27,
        "bit_mask": 0x10
	},
	"Falls Rupee Cave Top Top": {
		"region_id": "Falls",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F8F27,
        "flag_byte": 0x2002D25,
        "bit_mask": 0x20
	},
	"Falls Rupee Cave Top Left": {
		"region_id": "Falls",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F8F37,
        "flag_byte": 0x2002D25,
        "bit_mask": 0x40
	},
	"Falls Rupee Cave Top Middle": {
		"region_id": "Falls",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F8F47,
        "flag_byte": 0x2002D25,
        "bit_mask": 0x80
	},
	"Falls Rupee Cave Top Right": {
		"region_id": "Falls",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F8F57,
        "flag_byte": 0x2002D26,
        "bit_mask": 0x01
	},
	"Falls Rupee Cave Top Bottom": {
		"region_id": "Falls",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F8F67,
        "flag_byte": 0x2002D26,
        "bit_mask": 0x02
	},
	"Falls Rupee Cave Side Top": {
		"region_id": "Falls",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F8F77,
        "flag_byte": 0x2002D26,
        "bit_mask": 0x04
	},
	"Falls Rupee Cave Side Left": {
		"region_id": "Falls",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F8F87,
        "flag_byte": 0x2002D26,
        "bit_mask": 0x08
	},
	"Falls Rupee Cave Side Right": {
		"region_id": "Falls",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F8F97,
        "flag_byte": 0x2002D26,
        "bit_mask": 0x10
	},
	"Falls Rupee Cave Side Bottom": {
		"region_id": "Falls",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F8FA7,
        "flag_byte": 0x2002D26,
        "bit_mask": 0x20
	},
	"Falls Rupee Cave Underwater Top Left": {
		"region_id": "Falls",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F8FB7,
        "flag_byte": 0x2002D26,
        "bit_mask": 0x40
	},
	"Falls Rupee Cave Underwater Top Right": {
		"region_id": "Falls",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F8FC7,
        "flag_byte": 0x2002D26,
        "bit_mask": 0x80
	},
	"Falls Rupee Cave Underwater Middle Left": {
		"region_id": "Falls",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F8FD7,
        "flag_byte": 0x2002D27,
        "bit_mask": 0x01
	},
	"Falls Rupee Cave Underwater Middle Right": {
		"region_id": "Falls",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F8FE7,
        "flag_byte": 0x2002D27,
        "bit_mask": 0x02
	},
	"Falls Rupee Cave Underwater Bottom Left": {
		"region_id": "Falls",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F8FF7,
        "flag_byte": 0x2002D27,
        "bit_mask": 0x04
	},
	"Falls Rupee Cave Underwater Bottom Right": {
		"region_id": "Falls",
        "vanilla_item": "Rupee20",
        "flag_logic":0x0F9007,
        "flag_byte": 0x2002D27,
        "bit_mask": 0x08
	},
	"Falls Top Cave Bomb Wall Chest": {
		"region_id": "Falls",
        "vanilla_item": "Shells",
        "flag_logic":0x33-0x02-0x00,
        "flag_byte": 0x2002D25,
        "bit_mask": 0x04
	},
	"Falls Top Cave Chest": {
		"region_id": "Falls",
        "vanilla_item": "Rupee100",
        "flag_logic":0x33-0x00-0x00,
        "flag_byte": 0x2002D25,
        "bit_mask": 0x01
	},
	"Clouds Free Chest": {
		"region_id": "Clouds",
        "vanilla_item": "KinstoneCloudTops",
        "flag_logic":0x08-0x01-0x00,
        "flag_byte": 0x2002CD7,
        "bit_mask": 0x08
	},
	"Clouds North East Dig Spot": {
		"region_id": "Clouds",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0DCB5B,
        "flag_byte": 0x2002CD8,
        "bit_mask": 0x08
	},
	"Clouds North Kill": {
		"region_id": "Clouds",
        "vanilla_item": "KinstoneCloudTops",
        "flag_logic":0x0DCEDF,
        "flag_byte": 0x2002CDA,
        "bit_mask": 0x02
	},
	"Clouds North West Left Chest": {
		"region_id": "Clouds",
        "vanilla_item": "Shells",
        "flag_logic":0x08-0x01-0x03,
        "flag_byte": 0x2002CD7,
        "bit_mask": 0x40
	},
	"Clouds North West Right Chest": {
		"region_id": "Clouds",
        "vanilla_item": "Shells",
        "flag_logic":0x08-0x01-0x04,
        "flag_byte": 0x2002CD7,
        "bit_mask": 0x80
	},
	"Clouds North West Dig Spot": {
		"region_id": "Clouds",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0DCB4B,
        "flag_byte": 0x2002CD8,
        "bit_mask": 0x04
	},
	"Clouds North West Bottom Chest": {
		"region_id": "Clouds",
        "vanilla_item": "KinstoneCloudTops",
        "flag_logic":0x08-0x01-0x02,
        "flag_byte": 0x2002CD7,
        "bit_mask": 0x20
	},
	"Clouds South Left Chest": {
		"region_id": "Clouds",
        "vanilla_item": "Shells",
        "flag_logic":0x08-0x01-0x05,
        "flag_byte": 0x2002CD8,
        "bit_mask": 0x01
	},
	"Clouds South Dig Spot": {
		"region_id": "Clouds",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0DCB8B,
        "flag_byte": 0x2002CD8,
        "bit_mask": 0x40
	},
	"Clouds South Middle Chest": {
		"region_id": "Clouds",
        "vanilla_item": "KinstoneCloudTops",
        "flag_logic":0x08-0x01-0x01,
        "flag_byte": 0x2002CD7,
        "bit_mask": 0x10
	},
	"Clouds South Middle Dig Spot": {
		"region_id": "Clouds",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0DCB6B,
        "flag_byte": 0x2002CD8,
        "bit_mask": 0x10
	},
	"Clouds South Kill": {
		"region_id": "Clouds",
        "vanilla_item": "KinstoneCloudTops",
        "flag_logic":0x0DCEEF,
        "flag_byte": 0x2002CDA,
        "bit_mask": 0x08
	},
	"Clouds South Right Chest": {
		"region_id": "Clouds",
        "vanilla_item": "Shells",
        "flag_logic":0x08-0x01-0x06,
        "flag_byte": 0x2002CD8,
        "bit_mask": 0x02
	},
	"Clouds South Right Dig Spot": {
		"region_id": "Clouds",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0DCB9B,
        "flag_byte": 0x2002CD8,
        "bit_mask": 0x80
	},
	"Clouds South East Bottom Dig Spot": {
		"region_id": "Clouds",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0DCBAB,
        "flag_byte": 0x2002CD9,
        "bit_mask": 0x01
	},
	"Clouds South East Top Dig Spot": {
		"region_id": "Clouds",
        "vanilla_item": "Kinstone",
        "flag_logic":0x0DCB7B,
        "flag_byte": 0x2002CD8,
        "bit_mask": 0x20
	},
	"Wind Tribe 1F Left Chest": {
		"region_id": "Wind Tribe",
        "vanilla_item": "Kinstone",
        "flag_logic":0x30-0x00-0x00,
        "flag_byte": 0x2002CDC,
        "bit_mask": 0x20
	},
	"Wind Tribe 1F Right Chest": {
		"region_id": "Wind Tribe",
        "vanilla_item": "Kinstone",
        "flag_logic":0x30-0x00-0x01,
        "flag_byte": 0x2002CDC,
        "bit_mask": 0x40
	},
	"Wind Tribe 2F Chest": {
		"region_id": "Wind Tribe",
        "vanilla_item": "Kinstone",
        "flag_logic":0x30-0x01-0x00,
        "flag_byte": 0x2002CDC,
        "bit_mask": 0x80
	},
	"Wind Tribe 2F Gregal NPC 1": {
		"region_id": "Wind Tribe",
        "vanilla_item": "Shells",
        "flag_logic":0x014C5C,
        "flag_byte": 0x2002CE8,
        "bit_mask": 0x20
	},
	"Wind Tribe 2F Gregal NPC 2": {
		"region_id": "Wind Tribe",
        "vanilla_item": "LightArrow",
        "flag_logic":0x014CBC,
        "flag_byte": 0x2002CE8,
        "bit_mask": 0x40
	},
	"Wind Tribe 3F Left Chest": {
		"region_id": "Wind Tribe",
        "vanilla_item": "Kinstone",
        "flag_logic":0x30-0x02-0x02,
        "flag_byte": 0x2002CDD,
        "bit_mask": 0x01
	},
	"Wind Tribe 3F Center Chest": {
		"region_id": "Wind Tribe",
        "vanilla_item": "Kinstone",
        "flag_logic":0x30-0x02-0x01,
        "flag_byte": 0x2002CDD,
        "bit_mask": 0x02
	},
	"Wind Tribe 3F Right Chest": {
		"region_id": "Wind Tribe",
        "vanilla_item": "Kinstone",
        "flag_logic":0x30-0x02-0x00,
        "flag_byte": 0x2002CDD,
        "bit_mask": 0x04
	},
	"Wind Tribe 4F Left Chest": {
		"region_id": "Wind Tribe",
        "vanilla_item": "Kinstone",
        "flag_logic":0x30-0x03-0x00,
        "flag_byte": 0x2002CDD,
        "bit_mask": 0x40
	},
	"Wind Tribe 4F Right Chest": {
		"region_id": "Wind Tribe",
        "vanilla_item": "Kinstone",
        "flag_logic":0x30-0x03-0x01,
        "flag_byte": 0x2002CDD,
        "bit_mask": 0x80
	},
	"Deepwood 2F Chest": {
		"region_id": "Deepwood",
        "vanilla_item": "Rupee20",
        "flag_logic":0x48-0x17-0x01,
        "flag_byte": 0x2002D45,
        "bit_mask": 0x04
	},
	"Deepwood 1F Slug Torches Chest": {
		"region_id": "Deepwood",
        "vanilla_item": "SmallKey (DeepWoods)",
        "flag_logic":0x48-0x10-0x01,
        "flag_byte": 0x2002D43,
        "bit_mask": 0x20
	},
	"Deepwood 1F Barrel Room Chest": {
		"region_id": "Deepwood",
        "vanilla_item": "Shells",
        "flag_logic":0x48-0x06-0x01,
        "flag_byte": 0x2002D41,
        "bit_mask": 0x08
	},
	"Deepwood 1F West Big Chest": {
		"region_id": "Deepwood",
        "vanilla_item": "Compass (DeepWoods)",
        "flag_logic":0x48-0x05-0x01,
        "flag_byte": 0x2002D41,
        "bit_mask": 0x02
	},
	"Deepwood 1F West Statue Puzzle Chest": {
		"region_id": "Deepwood",
        "vanilla_item": "SmallKey (DeepWoods)",
        "flag_logic":0x48-0x04-0x01,
        "flag_byte": 0x2002D40,
        "bit_mask": 0x80
	},
	"Deepwood 1F East Mulldozer Fight Item": {
		"region_id": "Deepwood",
        "vanilla_item": "SmallKey (DeepWoods)",
        "flag_logic":0x0DE51B,
        "flag_byte": 0x2002D42,
        "bit_mask": 0x01
	},
	"Deepwood 1F North East Chest": {
		"region_id": "Deepwood",
        "vanilla_item": "Shells",
        "flag_logic":0x48-0x02-0x01,
        "flag_byte": 0x2002D40,
        "bit_mask": 0x10
	},
	"Deepwood B1 Switch Room Big Chest": {
		"region_id": "Deepwood",
        "vanilla_item": "DungeonMap (DeepWoods)",
        "flag_logic":0x48-0x12-0x02,
        "flag_byte": 0x2002D44,
        "bit_mask": 0x04
	},
	"Deepwood B1 Switch Room Chest": {
		"region_id": "Deepwood",
        "vanilla_item": "SmallKey (DeepWoods)",
        "flag_logic":0x48-0x12-0x01,
        "flag_byte": 0x2002D44,
        "bit_mask": 0x02
	},
	"Deepwood 1F Blue Warp HP": {
		"region_id": "Deepwood",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0DDE03,
        "flag_byte": 0x2002D45,
        "bit_mask": 0x80
	},
	"Deepwood 1F Blue Warp Left Chest": {
		"region_id": "Deepwood",
        "vanilla_item": "Shells",
        "flag_logic":0x48-0x01-0x01,
        "flag_byte": 0x2002D40,
        "bit_mask": 0x04
	},
	"Deepwood 1F Blue Warp Right Chest": {
		"region_id": "Deepwood",
        "vanilla_item": "Shells",
        "flag_logic":0x48-0x01-0x02,
        "flag_byte": 0x2002D40,
        "bit_mask": 0x08
	},
	"Deepwood 1F Madderpillar Big Chest": {
		"region_id": "Deepwood",
        "vanilla_item": "GustJar",
        "flag_logic":0x48-0x00-0x01,
        "flag_byte": 0x2002D3F,
        "bit_mask": 0x08
	},
	"Deepwood 1F Madderpillar HP": {
		"region_id": "Deepwood",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0DE1F7,
        "flag_byte": 0x2002D46,
        "bit_mask": 0x04
	},
	"Deepwood B1 West Big Chest": {
		"region_id": "Deepwood",
        "vanilla_item": "BigKey (DeepWoods)",
        "flag_logic":0x48-0x11-0x01,
        "flag_byte": 0x2002D43,
        "bit_mask": 0x80
	},
	"Deepwood Boss Item": {
		"region_id": "Deepwood",
        "vanilla_item": "HeartContainer",
        "flag_logic":"chuContainerItem:Define:FirstByte, chuContainerSub:Define:SecondByte",
        "flag_byte": 0x2002D44,
        "bit_mask": 0x80
	},
	"Deepwood Prize": {
		"region_id": "Deepwood",
        "vanilla_item": "EarthElement",
        "flag_logic":0x0DF03B,
        "flag_byte": 0x2002C9C,
        "bit_mask": 0x04
	},
	"CoF 1F Spike Beetle Big Chest": {
		"region_id": "CoF",
        "vanilla_item": "DungeonMap (Cave of Flame)",
        "flag_logic":0x50-0x15-0x00,
        "flag_byte": 0x2002D5A,
        "bit_mask": 0x04
	},
	"CoF 1F Item1": {
		"region_id": "CoF",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0DFAEB,
        "flag_byte": 0x2002D5B,
        "bit_mask": 0x40
	},
	"CoF 1F Item2": {
		"region_id": "CoF",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0DFAFB,
        "flag_byte": 0x2002D5B,
        "bit_mask": 0x80
	},
	"CoF 1F Item3": {
		"region_id": "CoF",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0DFB0B,
        "flag_byte": 0x2002D5C,
        "bit_mask": 0x01
	},
	"CoF 1F Item4": {
		"region_id": "CoF",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0DFB1B,
        "flag_byte": 0x2002D5C,
        "bit_mask": 0x02
	},
	"CoF 1F Item5": {
		"region_id": "CoF",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0DFB2B,
        "flag_byte": 0x2002D5C,
        "bit_mask": 0x04
	},
	"CoF B1 Hazy Room Big Chest": {
		"region_id": "CoF",
        "vanilla_item": "Compass (Cave of Flame)",
        "flag_logic":0x50-0x09-0x01,
        "flag_byte": 0x2002D59,
        "bit_mask": 0x02
	},
	"CoF B1 Hazy Room Small Chest": {
		"region_id": "CoF",
        "vanilla_item": "Kinstone",
        "flag_logic":0x50-0x09-0x00,
        "flag_byte": 0x2002D59,
        "bit_mask": 0x04
	},
	"CoF B1 Rollobite Chest": {
		"region_id": "CoF",
        "vanilla_item": "Rupee50",
        "flag_logic":0x50-0x08-0x01,
        "flag_byte": 0x2002D58,
        "bit_mask": 0x40
	},
	"CoF B1 Rollobite Pillar Chest": {
		"region_id": "CoF",
        "vanilla_item": "SmallKey (Cave of Flame)",
        "flag_logic":0x50-0x08-0x00,
        "flag_byte": 0x2002D58,
        "bit_mask": 0x80
	},
	"CoF B1 Spikey Chus Pillar Chest": {
		"region_id": "CoF",
        "vanilla_item": "SmallKey (Cave of Flame)",
        "flag_logic":0x50-0x01-0x01,
        "flag_byte": 0x2002D57,
        "bit_mask": 0x01
	},
	"CoF B1 HP": {
		"region_id": "CoF",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0DFC9F,
        "flag_byte": 0x2002D5B,
        "bit_mask": 0x10
	},
	"CoF B1 Spikey Chus Big Chest": {
		"region_id": "CoF",
        "vanilla_item": "PacciCane",
        "flag_logic":0x50-0x01-0x02,
        "flag_byte": 0x2002D57,
        "bit_mask": 0x02
	},
	"CoF B2 Pre Lava North Chest": {
		"region_id": "CoF",
        "vanilla_item": "Kinstone",
        "flag_logic":0x50-0x10-0x00,
        "flag_byte": 0x2002D59,
        "bit_mask": 0x10
	},
	"CoF B2 Pre Lava South Chest": {
		"region_id": "CoF",
        "vanilla_item": "Kinstone",
        "flag_logic":0x50-0x10-0x01,
        "flag_byte": 0x2002D59,
        "bit_mask": 0x20
	},
	"CoF B2 Lava Room Blade Chest": {
		"region_id": "CoF",
        "vanilla_item": "Kinstone",
        "flag_logic":0x50-0x14-0x00,
        "flag_byte": 0x2002D5A,
        "bit_mask": 0x01
	},
	"CoF B2 Lava Room Right Chest": {
		"region_id": "CoF",
        "vanilla_item": "Rupee100",
        "flag_logic":0x50-0x17-0x01,
        "flag_byte": 0x2002D5B,
        "bit_mask": 0x01
	},
	"CoF B2 Lava Room Left Chest": {
		"region_id": "CoF",
        "vanilla_item": "Kinstone",
        "flag_logic":0x50-0x17-0x00,
        "flag_byte": 0x2002D5A,
        "bit_mask": 0x80
	},
	"CoF B2 Lava Room Big Chest": {
		"region_id": "CoF",
        "vanilla_item": "BigKey (Cave of Flame)",
        "flag_logic":0x50-0x17-0x02,
        "flag_byte": 0x2002D5B,
        "bit_mask": 0x02
	},
	"CoF Boss Item": {
		"region_id": "CoF",
        "vanilla_item": "HeartContainer",
        "flag_logic":"gleerokContainerItem:Define:FirstByte, gleerokContainerSub:Define:SecondByte",
        "flag_byte": 0x2002D5B,
        "bit_mask": 0x04
	},
	"CoF Prize": {
		"region_id": "CoF",
        "vanilla_item": "FireElement",
        "flag_logic":0x0E0F03,
        "flag_byte": 0x2002C9C,
        "bit_mask": 0x08
	},
	"Crenel Melari NPC  CoF": {
		"region_id": "Crenel",
        "vanilla_item": "GreenSword",
        "flag_logic":0x00D26E,
        "flag_byte": 0x2002EA4,
        "bit_mask": 0x80
	},
	"Fortress Entrance 1F Left Chest": {
		"region_id": "Fortress",
        "vanilla_item": "Kinstone",
        "flag_logic":0x18-0x00-0x00,
        "flag_byte": 0x2002D05,
        "bit_mask": 0x80
	},
	"Fortress Entrance 1F Left Wizrobe Chest": {
		"region_id": "Fortress",
        "vanilla_item": "Shells",
        "flag_logic":0x58-0x23-0x00,
        "flag_byte": 0x2002D74,
        "bit_mask": 0x08
	},
	"Fortress Entrance 1F Right Item": {
		"region_id": "Fortress",
        "vanilla_item": "Rupee50",
        "flag_logic":0x0F3E67,
        "flag_byte": 0x2002D05,
        "bit_mask": 0x40
	},
	"Fortress Left 2F Dig Chest": {
		"region_id": "Fortress",
        "vanilla_item": "Kinstone",
        "flag_logic":0x18-0x01-0x00,
        "flag_byte": 0x2002D06,
        "bit_mask": 0x01
	},
	"Fortress Left 2F Item1": {
		"region_id": "Fortress",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F3F37,
        "flag_byte": 0x2002D06,
        "bit_mask": 0x20
	},
	"Fortress Left 2F Item2": {
		"region_id": "Fortress",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F3F47,
        "flag_byte": 0x2002D06,
        "bit_mask": 0x40
	},
	"Fortress Left 2F Item3": {
		"region_id": "Fortress",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F3F57,
        "flag_byte": 0x2002D06,
        "bit_mask": 0x80
	},
	"Fortress Left 2F Item4": {
		"region_id": "Fortress",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F3F67,
        "flag_byte": 0x2002D07,
        "bit_mask": 0x01
	},
	"Fortress Left 2F Item5": {
		"region_id": "Fortress",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0F3F77,
        "flag_byte": 0x2002D07,
        "bit_mask": 0x04
	},
	"Fortress Left 2F Item6": {
		"region_id": "Fortress",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F3F87,
        "flag_byte": 0x2002D07,
        "bit_mask": 0x08
	},
	"Fortress Left 2F Item7": {
		"region_id": "Fortress",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0F3F97,
        "flag_byte": 0x2002D07,
        "bit_mask": 0x02
	},
	"Fortress Left 3F Switch Chest": {
		"region_id": "Fortress",
        "vanilla_item": "Kinstone",
        "flag_logic":0x18-0x02-0x00,
        "flag_byte": 0x2002D07,
        "bit_mask": 0x20
	},
	"Fortress Left 3F Eyegore Big Chest": {
		"region_id": "Fortress",
        "vanilla_item": "DungeonMap (Fortress of Wind)",
        "flag_logic":0x58-0x00-0x00,
        "flag_byte": 0x2002D6F,
        "bit_mask": 0x10
	},
	"Fortress Left 3F Item Drop": {
		"region_id": "Fortress",
        "vanilla_item": "SmallKey (Fortress of Wind)",
        "flag_logic":"fowLeftItem:Define:FirstByte,fowLeftSub:Define:SecondByte",
        "flag_byte": 0x2002D73,
        "bit_mask": 0x80
	},
	"Fortress Middle 2F Big Chest": {
		"region_id": "Fortress",
        "vanilla_item": "Compass (Fortress of Wind)",
        "flag_logic":0x58-0x19-0x00,
        "flag_byte": 0x2002D73,
        "bit_mask": 0x02
	},
	"Fortress Middle 2F Statue Chest": {
		"region_id": "Fortress",
        "vanilla_item": "Kinstone",
        "flag_logic":0x18-0x01-0x01,
        "flag_byte": 0x2002D06,
        "bit_mask": 0x02
	},
	"Fortress Right 2F Left Chest": {
		"region_id": "Fortress",
        "vanilla_item": "Kinstone",
        "flag_logic":0x58-0x1D-0x00,
        "flag_byte": 0x2002D73,
        "bit_mask": 0x20
	},
	"Fortress Right 2F Right Chest": {
		"region_id": "Fortress",
        "vanilla_item": "Kinstone",
        "flag_logic":0x58-0x1D-0x01,
        "flag_byte": 0x2002D73,
        "bit_mask": 0x40
	},
	"Fortress Right 2F Dig Chest": {
		"region_id": "Fortress",
        "vanilla_item": "Kinstone",
        "flag_logic":0x18-0x01-0x02,
        "flag_byte": 0x2002D06,
        "bit_mask": 0x04
	},
	"Fortress Right 3F Dig Chest": {
		"region_id": "Fortress",
        "vanilla_item": "Kinstone",
        "flag_logic":0x18-0x02-0x01,
        "flag_byte": 0x2002D07,
        "bit_mask": 0x40
	},
	"Fortress Right 3F Item Drop": {
		"region_id": "Fortress",
        "vanilla_item": "SmallKey (Fortress of Wind)",
        "flag_logic":"fowRightItem:Define:FirstByte,fowRightSub:Define:SecondByte",
        "flag_byte": 0x2002D74,
        "bit_mask": 0x02
	},
	"Fortress Entrance 1F Right HP": {
		"region_id": "Fortress",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0E2DD7,
        "flag_byte": 0x2002D74,
        "bit_mask": 0x80
	},
	"Fortress Back Left Big Chest": {
		"region_id": "Fortress",
        "vanilla_item": "MoleMitts",
        "flag_logic":0x18-0x03-0x00,
        "flag_byte": 0x2002D08,
        "bit_mask": 0x01
	},
	"Fortress Back Left Small Chest": {
		"region_id": "Fortress",
        "vanilla_item": "Rupee100",
        "flag_logic":0x18-0x03-0x01,
        "flag_byte": 0x2002D08,
        "bit_mask": 0x02
	},
	"Fortress Back Right Statue Item Drop": {
		"region_id": "Fortress",
        "vanilla_item": "SmallKey (Fortress of Wind)",
        "flag_logic":0x0E1E8B,
        "flag_byte": 0x2002D71,
        "bit_mask": 0x40
	},
	"Fortress Back Right Minish Item Drop": {
		"region_id": "Fortress",
        "vanilla_item": "SmallKey (Fortress of Wind)",
        "flag_logic":0x0F424F,
        "flag_byte": 0x2002D08,
        "bit_mask": 0x10
	},
	"Fortress Back Right Dig Room Top Pot": {
		"region_id": "Fortress",
        "vanilla_item": "Rupee50",
        "flag_logic":"0x0F3FC7:FirstByte, 0x0F3FC9:SecondByte",
        "flag_byte": 0x2002D06,
        "bit_mask": 0x08
	},
	"Fortress Back Right Dig Room Bottom Pot": {
		"region_id": "Fortress",
        "vanilla_item": "Shells",
        "flag_logic":"0x0F3FD7:FirstByte, 0x0F3FD9:SecondByte",
        "flag_byte": 0x2002D06,
        "bit_mask": 0x10
	},
	"Fortress Back Right Big Chest": {
		"region_id": "Fortress",
        "vanilla_item": "BigKey (Fortress of Wind)",
        "flag_logic":0x58-0x1B-0x00,
        "flag_byte": 0x2002D73,
        "bit_mask": 0x04
	},
	"Fortress Boss Item": {
		"region_id": "Fortress",
        "vanilla_item": "HeartContainer",
        "flag_logic":"mazaalContainerItem:Define:FirstByte, mazaalContainerSub:Define:SecondByte",
        "flag_byte": 0x2002D72,
        "bit_mask": 0x04
	},
	"Fortress Prize": {
		"region_id": "Fortress",
        "vanilla_item": "Ocarina",
        "flag_logic":"0x09C9E6:FirstByte, 0x09C9E8:SecondByte",
        "flag_byte": 0x2002D74,
        "bit_mask": 0x20
	},
	"Droplets Entrance B2 East Iceblock": {
		"region_id": "Droplets",
        "vanilla_item": "SmallKey (Temple of Droplet)",
        "flag_logic":"0x098C1A:FirstByte, 0x098C1C:SecondByte",
        "flag_byte": 0x2002D8E,
        "bit_mask": 0x04
	},
	"Droplets Entrance B2 West Iceblock": {
		"region_id": "Droplets",
        "vanilla_item": "BigKey (Temple of Droplet)",
        "flag_logic":"0x098C3C:FirstByte, 0x098C3E:SecondByte",
        "flag_byte": 0x2002D8D,
        "bit_mask": 0x80
	},
	"Droplets Left Path B1 Underpass Item1": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E3F8B,
        "flag_byte": 0x2002D94,
        "bit_mask": 0x20
	},
	"Droplets Left Path B1 Underpass Item2": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E3F9B,
        "flag_byte": 0x2002D94,
        "bit_mask": 0x40
	},
	"Droplets Left Path B1 Underpass Item3": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E3FAB,
        "flag_byte": 0x2002D94,
        "bit_mask": 0x80
	},
	"Droplets Left Path B1 Underpass Item4": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E3FBB,
        "flag_byte": 0x2002D95,
        "bit_mask": 0x01
	},
	"Droplets Left Path B1 Underpass Item5": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E3FCB,
        "flag_byte": 0x2002D95,
        "bit_mask": 0x02
	},
	"Droplets Left Path B1 Waterfall Big Chest": {
		"region_id": "Droplets",
        "vanilla_item": "DungeonMap (Temple of Droplet)",
        "flag_logic":0x60-0x0D-0x00,
        "flag_byte": 0x2002D8B,
        "bit_mask": 0x80
	},
	"Droplets Left Path B1 Waterfall Underwater1": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0E3593,
        "flag_byte": 0x2002D96,
        "bit_mask": 0x20
	},
	"Droplets Left Path B1 Waterfall Underwater2": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0E35A3,
        "flag_byte": 0x2002D96,
        "bit_mask": 0x40
	},
	"Droplets Left Path B1 Waterfall Underwater3": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0E35B3,
        "flag_byte": 0x2002D96,
        "bit_mask": 0x80
	},
	"Droplets Left Path B1 Waterfall Underwater4": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0E35C3,
        "flag_byte": 0x2002D97,
        "bit_mask": 0x01
	},
	"Droplets Left Path B1 Waterfall Underwater5": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0E35D3,
        "flag_byte": 0x2002D97,
        "bit_mask": 0x02
	},
	"Droplets Left Path B1 Waterfall Underwater6": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0E35E3,
        "flag_byte": 0x2002D97,
        "bit_mask": 0x04
	},
	"Droplets Left Path B2 Waterfall Underwater1": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0E58DF,
        "flag_byte": 0x2002D95,
        "bit_mask": 0x80
	},
	"Droplets Left Path B2 Waterfall Underwater2": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0E58EF,
        "flag_byte": 0x2002D96,
        "bit_mask": 0x01
	},
	"Droplets Left Path B2 Waterfall Underwater3": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0E58FF,
        "flag_byte": 0x2002D96,
        "bit_mask": 0x02
	},
	"Droplets Left Path B2 Waterfall Underwater4": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0E590F,
        "flag_byte": 0x2002D96,
        "bit_mask": 0x04
	},
	"Droplets Left Path B2 Waterfall Underwater5": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0E591F,
        "flag_byte": 0x2002D96,
        "bit_mask": 0x08
	},
	"Droplets Left Path B2 Waterfall Underwater6": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee5",
        "flag_logic":0x0E592F,
        "flag_byte": 0x2002D96,
        "bit_mask": 0x10
	},
	"Droplets Left Path B2 Underwater Pot": {
		"region_id": "Droplets",
        "vanilla_item": "SmallKey (Temple of Droplet)",
        "flag_logic":0x0E5BC7,
        "flag_byte": 0x2002D93,
        "bit_mask": 0x04
	},
	"Droplets Left Path B2 Ice Madderpillar Big Chest": {
		"region_id": "Droplets",
        "vanilla_item": "Compass (Temple of Droplet)",
        "flag_logic":0x60-0x32-0x01,
        "flag_byte": 0x2002D92,
        "bit_mask": 0x80
	},
	"Droplets Left Path B2 Ice Plain Frozen Chest": {
		"region_id": "Droplets",
        "vanilla_item": "Shells",
        "flag_logic":0x60-0x28-0x00,
        "flag_byte": 0x2002D8F,
        "bit_mask": 0x04
	},
	"Droplets Left Path B2 Ice Plain Chest": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee50",
        "flag_logic":0x60-0x28-0x01,
        "flag_byte": 0x2002D8F,
        "bit_mask": 0x08
	},
	"Droplets Left Path B2 Lilypad Corner Frozen Chest": {
		"region_id": "Droplets",
        "vanilla_item": "Kinstone",
        "flag_logic":0x60-0x2D-0x00,
        "flag_byte": 0x2002D93,
        "bit_mask": 0x40
	},
	"Droplets Right Path B1 1st Chest": {
		"region_id": "Droplets",
        "vanilla_item": "Kinstone",
        "flag_logic":0x60-0x09-0x00,
        "flag_byte": 0x2002D8B,
        "bit_mask": 0x01
	},
	"Droplets Right Path B1 2nd Chest": {
		"region_id": "Droplets",
        "vanilla_item": "Kinstone",
        "flag_logic":0x60-0x0A-0x00,
        "flag_byte": 0x2002D8B,
        "bit_mask": 0x04
	},
	"Droplets Right Path B1 Pot": {
		"region_id": "Droplets",
        "vanilla_item": "Kinstone",
        "flag_logic":"0x0E3A73:FirstByte, 0x0E3A75:SecondByte",
        "flag_byte": 0x2002D8B,
        "bit_mask": 0x02
	},
	"Droplets Right Path B3Frozen Chest": {
		"region_id": "Droplets",
        "vanilla_item": "SmallKey (Temple of Droplet)",
        "flag_logic":0x60-0x11-0x00,
        "flag_byte": 0x2002D8D,
        "bit_mask": 0x10
	},
	"Droplets Right Path B1 Blu Chu Big Chest": {
		"region_id": "Droplets",
        "vanilla_item": "Lantern",
        "flag_logic":0x60-0x10-0x01,
        "flag_byte": 0x2002D8C,
        "bit_mask": 0x80
	},
	"Droplets Right Path B2Frozen Chest": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee100",
        "flag_logic":0x60-0x32-0x00,
        "flag_byte": 0x2002D92,
        "bit_mask": 0x40
	},
	"Droplets Right Path B2 Dark Maze Bottom Chest": {
		"region_id": "Droplets",
        "vanilla_item": "Kinstone",
        "flag_logic":0x60-0x2B-0x03,
        "flag_byte": 0x2002D8F,
        "bit_mask": 0x80
	},
	"Droplets Right Path B2 Mulldozers Item Drop": {
		"region_id": "Droplets",
        "vanilla_item": "SmallKey (Temple of Droplet)",
        "flag_logic":0x0E55CB,
        "flag_byte": 0x2002D91,
        "bit_mask": 0x80
	},
	"Droplets Right Path B2 Dark Maze Top Right Chest": {
		"region_id": "Droplets",
        "vanilla_item": "Kinstone",
        "flag_logic":0x60-0x2B-0x01,
        "flag_byte": 0x2002D8F,
        "bit_mask": 0x20
	},
	"Droplets Right Path B2 Dark Maze Top Left Chest": {
		"region_id": "Droplets",
        "vanilla_item": "Kinstone",
        "flag_logic":0x60-0x2B-0x02,
        "flag_byte": 0x2002D8F,
        "bit_mask": 0x40
	},
	"Droplets Right Path B2 Underpass Item1": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E483F,
        "flag_byte": 0x2002D95,
        "bit_mask": 0x10
	},
	"Droplets Right Path B2 Underpass Item2": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E484F,
        "flag_byte": 0x2002D95,
        "bit_mask": 0x20
	},
	"Droplets Right Path B2 Underpass Item3": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E485F,
        "flag_byte": 0x2002D95,
        "bit_mask": 0x40
	},
	"Droplets Right Path B2 Underpass Item4": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E486F,
        "flag_byte": 0x2002D95,
        "bit_mask": 0x04
	},
	"Droplets Right Path B2 Underpass Item5": {
		"region_id": "Droplets",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E487F,
        "flag_byte": 0x2002D95,
        "bit_mask": 0x08
	},
	"Droplets Boss Item": {
		"region_id": "Droplets",
        "vanilla_item": "HeartContainer",
        "flag_logic":"octoContainerItem:Define:FirstByte, octoContainerSub:Define:SecondByte",
        "flag_byte": 0x2002D8C,
        "bit_mask": 0x01
	},
	"Droplets Prize": {
		"region_id": "Droplets",
        "vanilla_item": "WaterElement",
        "flag_logic":0x0E40C3,
        "flag_byte": 0x2002C9C,
        "bit_mask": 0x20
	},
	"Palace 1st Half 1F Grate Chest": {
		"region_id": "Palace",
        "vanilla_item": "Kinstone",
        "flag_logic":0x70-0x2D-0x00,
        "flag_byte": 0x2002DAA,
        "bit_mask": 0x40
	},
	"Palace 1st Half 1F Wizrobe Big Chest": {
		"region_id": "Palace",
        "vanilla_item": "RocsCape",
        "flag_logic":0x70-0x2C-0x00,
        "flag_byte": 0x2002DAA,
        "bit_mask": 0x10
	},
	"Palace 1st Half 2F Item1": {
		"region_id": "Palace",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E8B1F,
        "flag_byte": 0x2002DA7,
        "bit_mask": 0x04
	},
	"Palace 1st Half 2F Item2": {
		"region_id": "Palace",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E8B2F,
        "flag_byte": 0x2002DA7,
        "bit_mask": 0x08
	},
	"Palace 1st Half 2F Item3": {
		"region_id": "Palace",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E8B3F,
        "flag_byte": 0x2002DA7,
        "bit_mask": 0x10
	},
	"Palace 1st Half 2F Item4": {
		"region_id": "Palace",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E8B4F,
        "flag_byte": 0x2002DA7,
        "bit_mask": 0x20
	},
	"Palace 1st Half 2F Item5": {
		"region_id": "Palace",
        "vanilla_item": "Rupee1",
        "flag_logic":0x0E8B5F,
        "flag_byte": 0x2002DA7,
        "bit_mask": 0x40
	},
	"Palace 1st Half 3F Pot Puzzle Item Drop": {
		"region_id": "Palace",
        "vanilla_item": "SmallKey (Palace of Wind)",
        "flag_logic":0x0E896F,
        "flag_byte": 0x2002DA7,
        "bit_mask": 0x02
	},
	"Palace 1st Half 4F Bow Moblins Chest": {
		"region_id": "Palace",
        "vanilla_item": "Kinstone",
        "flag_logic":0x70-0x0F-0x00,
        "flag_byte": 0x2002DA4,
        "bit_mask": 0x80
	},
	"Palace 1st Half 5F Ball And Chain Soldiers Item Drop": {
		"region_id": "Palace",
        "vanilla_item": "SmallKey (Palace of Wind)",
        "flag_logic":0x0E719F,
        "flag_byte": 0x2002DA4,
        "bit_mask": 0x02
	},
	"Palace 1st Half 5F Fan Loop Chest": {
		"region_id": "Palace",
        "vanilla_item": "SmallKey (Palace of Wind)",
        "flag_logic":0x70-0x07-0x00,
        "flag_byte": 0x2002DA3,
        "bit_mask": 0x40
	},
	"Palace 1st Half 5F Big Chest": {
		"region_id": "Palace",
        "vanilla_item": "BigKey (Palace of Wind)",
        "flag_logic":0x70-0x01-0x00,
        "flag_byte": 0x2002DA2,
        "bit_mask": 0x10
	},
	"Palace 2nd Half 1F Dark Room Big Chest": {
		"region_id": "Palace",
        "vanilla_item": "Compass (Palace of Wind)",
        "flag_logic":0x70-0x32-0x00,
        "flag_byte": 0x2002DAB,
        "bit_mask": 0x02
	},
	"Palace 2nd Half 1F Dark Room Small Chest": {
		"region_id": "Palace",
        "vanilla_item": "SmallKey (Palace of Wind)",
        "flag_logic":0x70-0x32-0x01,
        "flag_byte": 0x2002DAB,
        "bit_mask": 0x04
	},
	"Palace 2nd Half 2F Many Rollers Chest": {
		"region_id": "Palace",
        "vanilla_item": "SmallKey (Palace of Wind)",
        "flag_logic":0x70-0x2B-0x00,
        "flag_byte": 0x2002DA9,
        "bit_mask": 0x80
	},
	"Palace 2nd Half 2F Twin Wizrobes Chest": {
		"region_id": "Palace",
        "vanilla_item": "Kinstone",
        "flag_logic":0x70-0x29-0x00,
        "flag_byte": 0x2002DA9,
        "bit_mask": 0x40
	},
	"Palace 2nd Half 3F Fire Wizrobes Big Chest": {
		"region_id": "Palace",
        "vanilla_item": "DungeonMap (Palace of Wind)",
        "flag_logic":0x70-0x1C-0x00,
        "flag_byte": 0x2002DA6,
        "bit_mask": 0x80
	},
	"Palace 2nd Half 4F HP": {
		"region_id": "Palace",
        "vanilla_item": "PieceOfHeart",
        "flag_logic":0x0E77A7,
        "flag_byte": 0x2002DAC,
        "bit_mask": 0x01
	},
	"Palace 2nd Half 4F Switch Hit Chest": {
		"region_id": "Palace",
        "vanilla_item": "Rupee200",
        "flag_logic":0x70-0x15-0x00,
        "flag_byte": 0x2002DA5,
        "bit_mask": 0x80
	},
	"Palace 2nd Half 5F Bombarossa Chest": {
		"region_id": "Palace",
        "vanilla_item": "SmallKey (Palace of Wind)",
        "flag_logic":0x70-0x03-0x00,
        "flag_byte": 0x2002DA2,
        "bit_mask": 0x20
	},
	"Palace 2nd Half 4F Block Maze Chest": {
		"region_id": "Palace",
        "vanilla_item": "Kinstone",
        "flag_logic":0x70-0x10-0x00,
        "flag_byte": 0x2002DA5,
        "bit_mask": 0x02
	},
	"Palace 2nd Half 5F Right Side Chest": {
		"region_id": "Palace",
        "vanilla_item": "Kinstone",
        "flag_logic":0x70-0x04-0x00,
        "flag_byte": 0x2002DA2,
        "bit_mask": 0x80
	},
	"Palace Boss Item": {
		"region_id": "Palace",
        "vanilla_item": "HeartContainer",
        "flag_logic":"gyorgContainerItem:Define:FirstByte, gyorgContainerSub:Define:SecondByte",
        "flag_byte": 0x2002DAB,
        "bit_mask": 0x20
	},
	"Palace Prize": {
		"region_id": "Palace",
        "vanilla_item": "WindElement",
        "flag_logic":0x0E69E3,
        "flag_byte": 0x2002C9C,
        "bit_mask": 0x40
	},
	"Sanctuary Pedestal Item1": {
		"region_id": "Sanctuary",
        "vanilla_item": "RedSword",
        "flag_logic":"pedestalSpot1Item:Define:FirstByte, pedestalSpot1Sub:Define:SecondByte",
        "flag_byte": 0x2002EA7,
        "bit_mask": 0x80
	},
	"Sanctuary Pedestal Item2": {
		"region_id": "Sanctuary",
        "vanilla_item": "BlueSword",
        "flag_logic":"pedestalSpot2Item:Define:FirstByte, pedestalSpot2Sub:Define:SecondByte",
        "flag_byte": 0x2002EA8,
        "bit_mask": 0x01
	},
	"Sanctuary Pedestal Item3": {
		"region_id": "Sanctuary",
        "vanilla_item": "FourSword",
        "flag_logic":"pedestalSpot3Item:Define:FirstByte, pedestalSpot3Sub:Define:SecondByte",
        "flag_byte": 0x2002EA8,
        "bit_mask": 0x02
	},
	"DHC B2 King": {
		"region_id": "DHC",
        "vanilla_item": "Rupee1",
        "flag_logic":0x00E46A,
        "flag_byte": 0x2002DC2,
        "bit_mask": 0x02
	},
	"DHC B1 Big Chest": {
		"region_id": "DHC",
        "vanilla_item": "DungeonMap (Dark Hyrule Castle)",
        "flag_logic":0x88-0x37-0x00,
        "flag_byte": 0x2002DC1,
        "bit_mask": 0x08
	},
	"DHC 1F Blade Chest": {
		"region_id": "DHC",
        "vanilla_item": "SmallKey (Dark Hyrule Castle)",
        "flag_logic":0x88-0x27-0x00,
        "flag_byte": 0x2002DC0,
        "bit_mask": 0x20
	},
	"DHC 1F Throne Big Chest": {
		"region_id": "DHC",
        "vanilla_item": "Compass (Dark Hyrule Castle)",
        "flag_logic":0x88-0x20-0x00,
        "flag_byte": 0x2002DBF,
        "bit_mask": 0x80
	},
	"DHC 3F North West Chest": {
		"region_id": "DHC",
        "vanilla_item": "SmallKey (Dark Hyrule Castle)",
        "flag_logic":0x88-0x01-0x00,
        "flag_byte": 0x2002DBB,
        "bit_mask": 0x40
	},
	"DHC 3F North East Chest": {
		"region_id": "DHC",
        "vanilla_item": "SmallKey (Dark Hyrule Castle)",
        "flag_logic":0x88-0x02-0x00,
        "flag_byte": 0x2002DBB,
        "bit_mask": 0x80
	},
	"DHC 3F South West Chest": {
		"region_id": "DHC",
        "vanilla_item": "SmallKey (Dark Hyrule Castle)",
        "flag_logic":0x88-0x03-0x00,
        "flag_byte": 0x2002DBC,
        "bit_mask": 0x01
	},
	"DHC 3F South East Chest": {
		"region_id": "DHC",
        "vanilla_item": "SmallKey (Dark Hyrule Castle)",
        "flag_logic":0x88-0x04-0x00,
        "flag_byte": 0x2002DBC,
        "bit_mask": 0x02
	},
	"DHC 2F Blue Warp Big Chest": {
		"region_id": "DHC",
        "vanilla_item": "BigKey (Dark Hyrule Castle)",
        "flag_logic":0x88-0x09-0x00,
        "flag_byte": 0x2002DBC,
        "bit_mask": 0x08
	},
	"Beat Vaati": {
		"region_id": "Beat Vaati",
        "vanilla_item": "",
        "flag_logic":0xaaaa,
        "flag_byte": 0x2002CA6,
        "bit_mask": 0x20,
		"victory": true
	}
}
