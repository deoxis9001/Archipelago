from BaseClasses import Item
import typing
from typing import Dict

from worlds.ff6wc import Rom


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool


espers = Rom.espers

characters = Rom.characters

items = list(Rom.item_name_id.keys())

all_items = [*espers, *characters, *items]

item_table = {name: index for index, name in enumerate(all_items)}

good_items = [
    'Marvel Shoes',
    'Cat Hood',
    'Snow Muffler',
    'Gem Box',
    'ValiantKnife',
    'Fixed Dice',
    'Offering',
    'Ragnarok Sword',
    'Minerva',
    'Exp. Egg',
    'Illumina',
    'Paladin Shld',
    "Pearl Lance",
    "Aura Lance",
    "Magus Rod",
    "Aegis Shld",
    "Flame Shld",
    "Ice Shld",
    "Thunder Shld",
    "Genji Shld",
    "Force Shld",
    "Red Cap",
    "Genji Helmet",
    "Force Armor",
    "Genji Armor",
    "BehemothSuit",
    "Economizer",
    "Genji Glove",
    "Dragon Horn"
]

okay_items = [item for item in items if item not in good_items or item == "Empty"]