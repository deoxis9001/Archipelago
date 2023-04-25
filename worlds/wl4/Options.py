import typing
from Options import Choice, Option, DefaultOnToggle, DeathLink


class Difficulty(Choice):
    """
    The game's difficulty level.
    Hard and S-Hard have slightly less locations to check since some Full Health item boxes are missing on those difficulties.
    """
    display_name = "Difficulty"
    option_normal = 0
    option_hard = 1
    option_s_hard = 2
    default = 0


class CrownShuffle(Choice):
    """
    Add extra locations to the crowns earned by collecting high amounts of coins in levels.
    Gold: Get an item when you complete a level with 10,000 coins.
    Silver: Get an item when you complete a level with 8,000 coins.
    Bronze: Get an item when you complete a level with 6,000 coins.
    All: Get an item individually for each crown, adding three items to each level.
    """
    display_name = "Crown Shuffle"
    option_off = 0
    option_gold = 1
    option_silver = 2
    option_bronze = 3
    option_all = 4
    default = 0


class EarlyEntryJewels(DefaultOnToggle):
    """
    Force the Entry Passage Jewel Pieces to appear early in the seed as a local item.
    Recommended to prevent early BK
    """
    display_name = "Early Entry Passage Jewels"


class MusicShuffle(Choice):
    """
    Music shuffle type
    None: Music is not shuffled
    Levels only: Only shuffle music between the main levels besides the Golden Passage
    Full: Shuffle all music
    """
    display_name = "Music Shuffle"
    option_none = 0
    option_levels_only = 1
    option_full = 2
    default = 0


wl4_options: typing.Dict[str, type[Option]] = {
    "difficulty": Difficulty,
    "crown_shuffle": CrownShuffle,
    "early_entry_jewels": EarlyEntryJewels,
    "death_link": DeathLink,
    #"music_shuffle": MusicShuffle,
}
