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
    - Random Singularity: a single season is randomly picked and put as default season in every region in the game
    - Specific Singularity: the given season is put as default season in every region in the game
    """
    display_name = "Default Seasons"

    option_vanilla = 0
    option_randomized = 1
    option_random_singularity = 2
    option_spring_singularity = 3
    option_summer_singularity = 4
    option_winter_singularity = 5
    option_autumn_singularity = 6

    default = 1


class OracleOfSeasonsHoronSeason(Choice):
    """
    In the vanilla game, Horon Village default season is chaotic: every time you enter it, it sets a random season.
    This nullifies every condition where a season is required inside Horon Village, since you can leave and re-enter
    again and again until you get the season that suits you.
    - Chaotic: vanilla behavior, which makes logic less interesting inside Horon Village and sometimes expects from
      you to leave and re-enter town a dozen times until you get the right season
    - Normalized: Horon Village behaves like any other region in the game (it has a default season that can be changed
      using Rod of Seasons)
    Setting this option to "Normalized" makes it follow the global behavior defined in "Default Seasons" option
    """
    display_name = "Horon Village Default Season"

    option_chaotic = 0
    option_normalized = 1

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

    default = "random"


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
    display_name = "Shuffle Old Men"

    option_vanilla = 0
    option_shuffled_values = 1
#    option_turn_into_locations = 2

    default = 0


class OraclesOfSeasonsTreehouseOldManRequirement(Range):
    """
    The amount of essences that you need to bring to the treehouse old man for him to give his item.
    """
    display_name = "Treehouse Old Man Requirement"

    range_start = 0
    range_end = 8
    default = 5


class OraclesOfSeasonsGoldenBeastsRequirement(Range):
    """
    The amount of golden beasts that need to be beaten for the golden old man to give his item.
    Golden beasts are 4 unique enemies that appear at specific spots on specific seasons, and beating all four of them
    requires all seasons and having access to most of the overworld.
    """
    display_name = "Golden Beasts Requirement"

    range_start = 0
    range_end = 4
    default = 1


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


class OracleOfSeasonsPricesFactor(Range):
    """
    A factor (expressed as percentage) that will be applied to all prices inside all shops in the game.
    - Setting it at 10% will make all items almost free
    - Setting it at 300% will make all items horrendously expensive, use at your own risk!
    """
    display_name = "Prices Factor (%)"

    range_start = 10
    range_end = 300
    default = 100


class OracleOfSeasonsAdvanceShop(Toggle):
    """
    In the vanilla game, there is a house northwest of Horon Village hosting the secret "Advance Shop" that can only
    be accessed if the game is being played on a Game Boy Advance console.
    If enabled, this option makes this shop always open, adding 3 shop locations to the game (and some rupees to the
    item pool to compensate for the extra purchases that might be required)
    """
    display_name = "Open Advance Shop"


class OracleOfSeasonsFoolsOre(Choice):
    """
    In the vanilla game, the Fool's Ore is the item "given" by the strange brothers in "exchange" for your feather.
    The way the vanilla game is done means you never get to use it, but it's by far the strongest weapon in the game
    (dealing 4 times more damage than an L-2 sword!)
    - Vanilla: Fool's Ore appears in the item pool with its stats unchanged
    - Balanced: Fool's Ore appears in the item pool but its stats are lowered to become comparable to an L-2 sword
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


class OracleOfSeasonsQuickFlute(DefaultOnToggle):
    """
    When enabled, playing the flute will immobilize you during a very small amount of time compared to vanilla game.
    """
    display_name = "Quick Flute"


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
    horon_village_season: OracleOfSeasonsHoronSeason
    animal_companion: OracleOfSeasonsAnimalCompanion
    shuffle_dungeons: OracleOfSeasonsDungeonShuffle
    shuffle_portals: OracleOfSeasonsPortalShuffle
    shuffle_old_men: OracleOfSeasonsOldMenShuffle
    treehouse_old_man_requirement: OraclesOfSeasonsTreehouseOldManRequirement
    golden_beasts_requirement: OraclesOfSeasonsGoldenBeastsRequirement
    lost_woods_item_sequence: OracleOfSeasonsLostWoodsItemSequence
    ring_quality: OracleOfSeasonsRingQuality
    shop_prices_factor: OracleOfSeasonsPricesFactor
    advance_shop: OracleOfSeasonsAdvanceShop
    fools_ore: OracleOfSeasonsFoolsOre
    warp_to_start: OracleOfSeasonsWarpToStart
    quick_flute: OracleOfSeasonsQuickFlute
    heart_beep_interval: OracleOfSeasonsHeartBeepInterval
    death_link: DeathLink
