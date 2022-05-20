from BaseClasses import Item
import typing

class TheBindingOfIsaacRebirthItem(Item):
    game: str = "The Binding of Isaac Rebirth"

# 78000 - ?????
item_table = {
    #items (main)
    "Treasure Room Item": 78000,
    "Shop Item": 78001,
    "Boss Item": 78002,
    "Devil Deal Item": 78003,
    "Angle Deal Item": 78004,
    "Secret Room Item": 78005,
    "Library Item": 78006,
    "Curse Room Item": 78007,
    "Planetarium Item": 78008,
    #item (expirimental)
    "Shell Game Item": 78009,
    "Golden Chest Item": 78010,
    "Red Chest Item": 78011,
    "Beggar Item": 78012,
    "Demon Baggar Item": 78013,
    "Key Master Item": 78014,
    "Battery Bum Item": 78015,
    "Mom's Chest Item": 78016,
    "Greed Treasure Room Item": 78017,
    "Greed Boss Item": 78018,
    "Greed Shop Item": 78019,
    "Greed Devil Deal Item": 78020,
    "Greed Angel Deal Item": 78021,
    "Greed Curse Room Item": 78022,
    "Greed Secret Room Item": 78023,
    "Crane Game Item": 78024,
    "Ultra Secret Room Item": 78025,
    "Bomb Bum Item": 78026,
    "Old Chest Item": 78027,
    "Baby Shop Item": 78028,
    "Wooden Chest Item": 78029,
    "Rotten Beggar Item": 78030,
    #other
    "Random Pickup": 78031,
    "Random Heart": 78032,
    "Random Coin": 78033,
    "Random Bomb": 78034,
    "Random Key": 78035,
    "Random Card": 78036,
    "Random Pill": 78037,
    "Random Chest": 78038,
    "Random Trinket": 78039,
    "Victory": None,
}

lookup_id_to_name: typing.Dict[int, str] = {id: name for name, id in item_table.items() if id}