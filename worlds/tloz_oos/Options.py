from dataclasses import dataclass

from Options import Choice, DeathLink, DefaultOnToggle, PerGameCommonOptions, Range, Toggle


class OracleOfSeasonsGoal(Choice):
    """
    The goal to accomplish in order to complete the seed.
    - Beat Onox: beat the usual final boss (same as vanilla)
    """
    display_name = "Goal"

    option_beat_onox = 0

    default = 0


class OracleOfSeasonsLogicDifficulty(Choice):
    """
    The difficulty of the logic used to generate the seed.
    - Casual: expects you to know what you would know when playing the game for the first time
    - Medium: expects you to know well the alternatives on how to do basic things, but won't expect any trick
    - Hard: expects you to know difficult tricks such as bomb jumps
    """
    display_name = "Logic Difficulty"

    option_casual = 0
    option_medium = 1
    option_hard = 2

    default = 0


class OracleOfSeasonsRequiredEssences(Range):
    """
    The amount of essences that need to be obtained in order to get the Maku Seed from the Maku Tree and be able
    to fight Onox in his castle
    """
    display_name = "Required Essences"
    range_start = 0
    range_end = 8
    default = 8


class OracleOfSeasonsDefaultSeasons(Choice):
    """
    The world of Holodrum is split in regions, each one having its own default season being forced when entering it.
    This options gives several ways of manipulating those default seasons.
    - Vanilla: default seasons for each region are the ones from the original game
    - Randomized: each region has its own random default season picked at generation time
    - Singularity: only one season is randomly picked and put in every region in the game
    """
    display_name = "Default Seasons"

    option_vanilla = 0
    option_randomized = 1
    option_singularity = 2

    default = 1


class OracleOfSeasonsAnimalCompanion(Choice):
    """
    Determines which animal companion you can summon using the Flute, as well as the layout of the Natzu region.
    - Ricky: the kangaroo with boxing skills
    - Dimitri: the swimming dinosaur who can eat anything
    - Moosh: the flying blue bear with a passion for Spring Bananas
    """
    display_name = "Animal Companion"

    option_ricky = "Ricky"
    option_dimitri = "Dimitri"
    option_moosh = "Moosh"

    default = "Ricky"


class OracleOfSeasonsDungeonShuffle(Choice):
    """
    - Vanilla: each dungeon entrance leads to its intended dungeon
    - Shuffled: each dungeon entrance leads to a random dungeon picked at generation time
    """
    display_name = "Shuffle Dungeons"

    option_vanilla = 0
    option_shuffled = 1

    default = 0


class OracleOfSeasonsPortalShuffle(Choice):
    """
    - Vanilla: pairs of portals are the same as in the original game
    - Shuffled: each portal in Holodrum is connected to a random portal in Subrosia picked at generation time
    """
    display_name = "Shuffle Subrosia Portals"

    option_vanilla = 0
    option_shuffled = 1

    default = 0


class OracleOfSeasonsWarpToStart(DefaultOnToggle):
    """
    When enabled, you can warp to start by holding Start while exiting map screen.
    This can be used to make backtracking a bit more bearable in seeds where Gale Seeds take time to obtain and prevent
    most softlock situations from happening
    """
    display_name = "Warp to Start"


@dataclass
class OracleOfSeasonsOptions(PerGameCommonOptions):
    goal: OracleOfSeasonsGoal
    logic_difficulty: OracleOfSeasonsLogicDifficulty
    required_essences: OracleOfSeasonsRequiredEssences
    default_seasons: OracleOfSeasonsDefaultSeasons
    animal_companion: OracleOfSeasonsAnimalCompanion
    shuffle_dungeons: OracleOfSeasonsDungeonShuffle
    shuffle_portals: OracleOfSeasonsPortalShuffle
    warp_to_start: OracleOfSeasonsWarpToStart
    death_link: DeathLink
