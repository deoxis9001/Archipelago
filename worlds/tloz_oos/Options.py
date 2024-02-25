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
    - Shuffle: each dungeon entrance leads to a random dungeon picked at generation time
    """
    display_name = "Shuffle Dungeons"

    option_vanilla = 0
    option_shuffle = 1

    default = 0


class OracleOfSeasonsPortalShuffle(Choice):
    """
    - Vanilla: pairs of portals are the same as in the original game
    - Shuffle: each portal in Holodrum is connected to a random portal in Subrosia picked at generation time
    """
    display_name = "Shuffle Subrosia Portals"

    option_vanilla = 0
    option_shuffle = 1

    default = 0


class OracleOfSeasonsOldMenShuffle(Choice):
    """
    Determine how the Old Men that can be found under specific bushes are handled by the randomizer
    - Vanilla: Each Old Man gives/takes the amount of rupees it usually does in the base game
    - Shuffled Values: The rupee values given/taken are shuffled among Old Men
    """
    # - Turn Into Locations: Each Old Man becomes a randomized check, and the total amount of rupees they usually give
    #   in vanilla is shuffled into the item pool
    diplay_name = "Shuffle Old Men"

    option_vanilla = 0
    option_shuffle_values = 1
#    option_turn_into_locations = 2

    default = 0


class OracleOfSeasonsLostWoodsItemSequence(Choice):
    """
    This option defines how the "secret sequence" (both directions and seasons) leading to the Noble Sword pedestal
    is handled by the randomizer.
    - Vanilla: the sequence is the same as in the original game
    - Randomized: the sequence is randomized, and you need to use the Phonograph on the Deku Scrub to learn the sequence
    """
    display_name = "Lost Woods Item Sequence"

    option_vanilla = 0
    option_randomized = 1

    default = 1


class OracleOfSeasonsRingQuality(Choice):
    """
    Defines the quality of the rings that will be shuffled in your seed:
    - Any: any ring can potentially be shuffled (including literally useless ones)
    - Only Useful: only useful rings will be shuffled
    """
    display_name = "Rings Quality"

    option_any = 0
    option_only_useful = 1

    default = 1


class OracleOfSeasonsFoolsOre(Choice):
    """
    In the vanilla game, the Fool's Ore is the item "given" by the strange brothers in "exchange" for your feather.
    The way the vanilla game is done means you never get to use it, but it's by far the strongest weapon in the game
    (dealing 4 times more damage than a L-2 sword!)
    - Vanilla: Fool's Ore appears in the item pool with its stats unchanged
    - Balanced: Fool's Ore appears in the item pool but its stats are lowered to become comparable to a L-2 sword
    - Excluded: Fool's Ore doesn't appear in the item pool at all. Problem solved!
    """
    display_name = "Fool's Ore"

    option_vanilla = 0
    option_balanced = 1
    option_excluded = 2

    default = 1


class OracleOfSeasonsWarpToStart(DefaultOnToggle):
    """
    When enabled, you can warp to start by holding Start while exiting map screen.
    This can be used to make backtracking a bit more bearable in seeds where Gale Seeds take time to obtain and prevent
    most softlock situations from happening
    """
    display_name = "Warp to Start"


class OracleOfSeasonsHeartBeepInterval(Choice):
    """
    - Default: play the beeping sound at the usual frequency when low on health
    - Half: play the beeping sound two times less when low on health
    - Quarter: play the beeping sound four times less when low on health
    - Disabled: never play the beeping sound when low on health
    """
    display_name = "Heart Beep Frequency"

    option_default = 0
    option_half = 1
    option_quarter = 2
    option_disabled = 3

    default = 0


@dataclass
class OracleOfSeasonsOptions(PerGameCommonOptions):
    goal: OracleOfSeasonsGoal
    logic_difficulty: OracleOfSeasonsLogicDifficulty
    required_essences: OracleOfSeasonsRequiredEssences
    default_seasons: OracleOfSeasonsDefaultSeasons
    animal_companion: OracleOfSeasonsAnimalCompanion
    shuffle_dungeons: OracleOfSeasonsDungeonShuffle
    shuffle_portals: OracleOfSeasonsPortalShuffle
    shuffle_old_men: OracleOfSeasonsOldMenShuffle
    lost_woods_item_sequence: OracleOfSeasonsLostWoodsItemSequence
    ring_quality: OracleOfSeasonsRingQuality
    fools_ore: OracleOfSeasonsFoolsOre
    warp_to_start: OracleOfSeasonsWarpToStart
    heart_beep_interval: OracleOfSeasonsHeartBeepInterval
    death_link: DeathLink
