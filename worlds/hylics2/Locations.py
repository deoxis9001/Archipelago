from typing import Dict, TypedDict


class LocationDict(TypedDict, total=False):
    name: str
    region: int 


location_table: Dict[int, LocationDict] = {
    # Waynehouse
    200622: {'name': "Waynehouse: Toilet",
             'region': 2},
    200623: {'name': "Waynehouse: Basement Pot 1",
             'region': 2},
    200624: {'name': "Waynehouse: Basement Pot 2",
             'region': 2},
    200625: {'name': "Waynehouse: Basement Pot 3",
             'region': 2},
    200626: {'name': "Waynehouse: Sarcophagus",
             'region': 2},

    # Afterlife
    200628: {'name': "Afterlife: Mangled Wayne",
             'region': 1},
    200629: {'name': "Afterlife: Jar near Mangled Wayne",
             'region': 1},
    200630: {'name': "Afterlife: Jar under Pool",
             'region': 1},

    # New Muldul
    200632: {'name': "New Muldul: Shop Ceiling Pot 1",
             'region': 4},
    200633: {'name': "New Muldul: Shop Ceiling Pot 2",
             'region': 4},
    200634: {'name': "New Muldul: Flag Banana",
             'region': 4},
    200635: {'name': "New Muldul: Pot near Vault",
             'region': 4},
    200785: {'name': "New Muldul: Pot above Vault",
             'region': 4},
    200636: {'name': "New Muldul: Underground Pot",
             'region': 4},
    200637: {'name': "New Muldul: Underground Chest",
             'region': 4},
    200638: {'name': "New Muldul: Juice Trade",
             'region': 4},
    200639: {'name': "New Muldul: Basement Suitcase",
             'region': 4},
    200640: {'name': "New Muldul: Upper House Chest 1",
             'region': 4},
    200641: {'name': "New Muldul: Upper House Chest 2",
             'region': 4},

    # New Muldul Vault
    200643: {'name': "New Muldul: Talk to Pongorma",
             'region': 4},
    200645: {'name': "New Muldul: Rescued Blerol 1",
             'region': 4},
    200646: {'name': "New Muldul: Rescued Blerol 2",
             'region': 4},
    200647: {'name': "New Muldul: Vault Left Chest",
             'region': 5},
    200648: {'name': "New Muldul: Vault Right Chest",
             'region': 5},
    200649: {'name': "New Muldul: Vault Bomb",
             'region': 5},

    # Viewax's Edifice
    200650: {'name': "Viewax's Edifice: Fountain Banana",
             'region': 6},
    200651: {'name': "Viewax's Edifice: Dedusmuln's Suitcase",
             'region': 6},
    200652: {'name': "Viewax's Edifice: Dedusmuln's Campfire",
             'region': 6},
    200653: {'name': "Viewax's Edifice: Talk to Dedusmuln",
             'region': 6},
    200655: {'name': "Viewax's Edifice: Canopic Jar",
             'region': 6},
    200656: {'name': "Viewax's Edifice: Cave Sarcophagus",
             'region': 6},
    200657: {'name': "Viewax's Edifice: Shielded Key",
             'region': 6},
    200658: {'name': "Viewax's Edifice: Tower Pot",
             'region': 6},
    200659: {'name': "Viewax's Edifice: Tower Jar",
             'region': 6},
    200660: {'name': "Viewax's Edifice: Tower Chest",
             'region': 6},
    200661: {'name': "Viewax's Edifice: Sage Fridge",
             'region': 6},
    200662: {'name': "Viewax's Edifice: Sage Item 1",
             'region': 6},
    200663: {'name': "Viewax's Edifice: Sage Item 2",
             'region': 6},
    200664: {'name': "Viewax's Edifice: Viewax Pot",
             'region': 6},
    200665: {'name': "Viewax's Edifice: Defeat Viewax",
             'region': 6},

    # Viewax Arcade Minigame
    200667: {'name': "Arcade 1: Key",
             'region': 6},
    200668: {'name': "Arcade 1: Coin Dash",
             'region': 6},
    200669: {'name': "Arcade 1: Burrito Alcove 1",
             'region': 6},
    200670: {'name': "Arcade 1: Burrito Alcove 2",
             'region': 6},
    200671: {'name': "Arcade 1: Behind Spikes Banana",
             'region': 6},
    200672: {'name': "Arcade 1: Pyramid Banana",
             'region': 6},
    200673: {'name': "Arcade 1: Moving Platforms Muscle Applique",
             'region': 6},
    200674: {'name': "Arcade 1: Bed Banana",
             'region': 6},

    # Airship
    200675: {'name': "Airship: Talk to Somsnosa",
             'region': 7},
    
    # Arcade Island
    200676: {'name': "Arcade Island: Shielded Key",
             'region': 8},
    200677: {'name': "Arcade 2: Flying Machine Banana",
             'region': 8},
    200678: {'name': "Arcade 2: Paper Cup Detour",
             'region': 8},
    200679: {'name': "Arcade 2: Peak Muscle Applique",
             'region': 8},
    200680: {'name': "Arcade 2: Double Banana 1",
             'region': 8},
    200681: {'name': "Arcade 2: Double Banana 2",
             'region': 8},
    200682: {'name': "Arcade 2: Cave Burrito",
             'region': 8},

    # Juice Ranch
    200684: {'name': "Juice Ranch: Juice 1",
             'region': 10},
    200685: {'name': "Juice Ranch: Juice 2",
             'region': 10},
    200686: {'name': "Juice Ranch: Juice 3",
             'region': 10},
    200687: {'name': "Juice Ranch: Ledge Rancher",
             'region': 10},
    200688: {'name': "Juice Ranch: Battle with Somsnosa",
             'region': 10},
    200690: {'name': "Juice Ranch: Fridge",
             'region': 10},

    # Worm Pod
    200692: {'name': "Worm Pod: Key",
             'region': 12},

    # Foglast
    200693: {'name': "Foglast: West Sarcophagus",
             'region': 13},
    200694: {'name': "Foglast: Underground Sarcophagus",
             'region': 13},
    200695: {'name': "Foglast: Shielded Key",
             'region': 13},
    200696: {'name': "Foglast: Buy Clicker",
             'region': 13},
    200698: {'name': "Foglast: Shielded Chest",
             'region': 13},
    200699: {'name': "Foglast: Cave Fridge",
             'region': 13},
    200700: {'name': "Foglast: Roof Sarcophagus",
             'region': 13},
    200701: {'name': "Foglast: Under Lair Sarcophagus 1",
             'region': 13},
    200702: {'name': "Foglast: Under Lair Sarcophagus 2",
             'region': 13},
    200703: {'name': "Foglast: Under Lair Sarcophagus 3",
             'region': 13},
    200704: {'name': "Foglast: Sage Sarcophagus",
             'region': 13},
    200705: {'name': "Foglast: Sage Item 1",
             'region': 13},
    200706: {'name': "Foglast: Sage Item 2",
             'region': 13},

    # Drill Castle
    200707: {'name': "Drill Castle: Ledge Banana",
             'region': 14},
    200708: {'name': "Drill Castle: Island Banana",
             'region': 14},
    200709: {'name': "Drill Castle: Island Pot",
             'region': 14},
    200710: {'name': "Drill Castle: Cave Sarcophagus",
             'region': 14},
    200711: {'name': "Drill Castle: Roof Banana",
             'region': 14},

    # Sage Labyrinth
    200713: {'name': "Sage Labyrinth: 1F Chest Near Fountain",
             'region': 15},
    200714: {'name': "Sage Labyrinth: 1F Hidden Sarcophagus",
             'region': 15},
    200715: {'name': "Sage Labyrinth: 1F Four Statues Chest 1",
             'region': 15},
    200716: {'name': "Sage Labyrinth: 1F Four Statues Chest 2",
             'region': 15},
    200717: {'name': "Sage Labyrinth: B1 Double Chest 1",
             'region': 15},
    200718: {'name': "Sage Labyrinth: B1 Double Chest 2",
             'region': 15},
    200719: {'name': "Sage Labyrinth: B1 Single Chest",
             'region': 15},
    200720: {'name': "Sage Labyrinth: B1 Enemy Chest",
             'region': 15},
    200721: {'name': "Sage Labyrinth: B1 Hidden Sarcophagus",
             'region': 15},
    200722: {'name': "Sage Labyrinth: B1 Hole Chest",
             'region': 15},
    200723: {'name': "Sage Labyrinth: B2 Hidden Sarcophagus 1",
             'region': 15},
    200724: {'name': "Sage Labyrinth: B2 Hidden Sarcophagus 2",
             'region': 15},
    200754: {'name': "Sage Labyrinth: 2F Sarcophagus",
             'region': 15},
    200786: {'name': "Sage Labyrinth: Boss Secret Chest 1",
             'region': 15},
    200787: {'name': "Sage Labyrinth: Boss Secret Chest 2",
             'region': 15},
    200725: {'name': "Sage Labyrinth: Motor Hunter Sarcophagus",
             'region': 15},
    200726: {'name': "Sage Labyrinth: Sage Item 1",
             'region': 15},
    200727: {'name': "Sage Labyrinth: Sage Item 2",
             'region': 15},
    200728: {'name': "Sage Labyrinth: Sage Left Arm",
             'region': 15},
    200729: {'name': "Sage Labyrinth: Sage Right Arm",
             'region': 15},
    200730: {'name': "Sage Labyrinth: Sage Left Leg",
             'region': 15},
    200731: {'name': "Sage Labyrinth: Sage Right Leg",
             'region': 15},

    # Sage Airship
    200732: {'name': "Sage Airship: Bottom Level Pot",
             'region': 16},
    200733: {'name': "Sage Airship: Flesh Pot",
             'region': 16},
    200734: {'name': "Sage Airship: Top Jar",
             'region': 16},

    # Hylemxylem
    200736: {'name': "Hylemxylem: Jar",
             'region': 17},
    200737: {'name': "Hylemxylem: Lower Reservoir Key",
             'region': 17},
    200738: {'name': "Hylemxylem: Fountain Banana",
             'region': 17},
    200739: {'name': "Hylemxylem: East Island Banana",
             'region': 17},
    200740: {'name': "Hylemxylem: East Island Chest",
             'region': 17},
    200741: {'name': "Hylemxylem: Upper Chamber Banana",
             'region': 17},
    200742: {'name': "Hylemxylem: Across Upper Reservoir Chest",
             'region': 17},
    200743: {'name': "Hylemxylem: Drained Lower Reservoir Chest",
             'region': 17},
    200744: {'name': "Hylemxylem: Drained Lower Reservoir Burrito 1",
             'region': 17},
    200745: {'name': "Hylemxylem: Drained Lower Reservoir Burrito 2",
             'region': 17},
    200746: {'name': "Hylemxylem: Lower Reservoir Hole Pot 1",
             'region': 17},
    200747: {'name': "Hylemxylem: Lower Reservoir Hole Pot 2",
             'region': 17},
    200748: {'name': "Hylemxylem: Lower Reservoir Hole Pot 3",
             'region': 17},
    200749: {'name': "Hylemxylem: Lower Reservoir Hole Sarcophagus",
             'region': 17},
    200750: {'name': "Hylemxylem: Drained Upper Reservoir Burrito 1",
             'region': 17},
    200751: {'name': "Hylemxylem: Drained Upper Reservoir Burrito 2",
             'region': 17},
    200752: {'name': "Hylemxylem: Drained Upper Reservoir Burrito 3",
             'region': 17},
    200753: {'name': "Hylemxylem: Upper Reservoir Hole Key",
             'region': 17}
}


tv_location_table: Dict[int, LocationDict] = {
    200627: {'name': "Waynehouse: TV",
             'region': 2},
    200631: {'name': "Afterlife: TV",
             'region': 1},
    200642: {'name': "New Muldul: TV",
             'region': 4},
    200666: {'name': "Viewax's Edifice: TV",
             'region': 6},
    200683: {'name': "TV Island: TV",
             'region': 9},
    200691: {'name': "Juice Ranch: TV",
             'region': 10},
    200697: {'name': "Foglast: TV",
             'region': 13},
    200712: {'name': "Drill Castle: TV",
             'region': 14},
    200735: {'name': "Sage Airship: TV",
             'region': 16}
}


party_location_table: Dict[int, LocationDict] = {
    200644: {'name': "New Muldul: Pongorma Joins",
             'region': 4},
    200654: {'name': "Viewax's Edifice: Dedusmuln Joins",
             'region': 6},
    200689: {'name': "Juice Ranch: Somsnosa Joins",
             'region': 10}
}


medallion_location_table: Dict[int, LocationDict] = {
    200755: {'name': "New Muldul: Upper House Medallion",
             'region': 4},

    200756: {'name': "New Muldul: Vault Rear Left Medallion",
             'region': 5},
    200757: {'name': "New Muldul: Vault Rear Right Medallion",
             'region': 5},
    200758: {'name': "New Muldul: Vault Center Medallion",
             'region': 5},
    200759: {'name': "New Muldul: Vault Front Left Medallion",
             'region': 5},
    200760: {'name': "New Muldul: Vault Front Right Medallion",
             'region': 5},

    200761: {'name': "Viewax's Edifice: Fort Wall Medallion",
             'region': 6},
    200762: {'name': "Viewax's Edifice: Jar Medallion",
             'region': 6},
    200763: {'name': "Viewax's Edifice: Sage Chair Medallion",
             'region': 6},
    200764: {'name': "Arcade 1: Lonely Medallion",
             'region': 6},
    200765: {'name': "Arcade 1: Alcove Medallion",
             'region': 6},
    200766: {'name': "Arcade 1: Lava Medallion",
             'region': 6},

    200767: {'name': "Arcade 2: Flying Machine Medallion",
             'region': 8},
    200768: {'name': "Arcade 2: Guarded Medallion",
             'region': 8},
    200769: {'name': "Arcade 2: Spinning Medallion",
             'region': 8},
    200770: {'name': "Arcade 2: Hook Medallion",
             'region': 8},
    200771: {'name': "Arcade 2: Flag Medallion",
             'region': 8},

    200772: {'name': "Foglast: Under Lair Medallion",
             'region': 13},
    200773: {'name': "Foglast: Mid-Air Medallion",
             'region': 13},
    200774: {'name': "Foglast: Top of Tower Medallion",
             'region': 13},

    200775: {'name': "Sage Airship: Walkway Medallion",
             'region': 16},
    200776: {'name': "Sage Airship: Flesh Medallion",
             'region': 16},
    200777: {'name': "Sage Airship: Top of Ship Medallion",
             'region': 16},
    200778: {'name': "Sage Airship: Hidden Medallion 1",
             'region': 16},
    200779: {'name': "Sage Airship: Hidden Medallion 2",
             'region': 16},
    200780: {'name': "Sage Airship: Hidden Medallion 3",
             'region': 16},

    200781: {'name': "Hylemxylem: Lower Reservoir Medallion",
             'region': 17},
    200782: {'name': "Hylemxylem: Lower Reservoir Hole Medallion",
             'region': 17},
    200783: {'name': "Hylemxylem: Drain Switch Medallion",
             'region': 17},
    200784: {'name': "Hylemxylem: Warpo Medallion",
             'region': 17}
}