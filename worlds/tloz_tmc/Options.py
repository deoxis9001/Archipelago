from dataclasses import dataclass

from Options import Choice, DeathLink, DefaultOnToggle, PerGameCommonOptions, Range, Toggle


class TheMinishCapDungeonsMap(Choice):
    """
    - Start With: Maps are given to you from the start.
    - Vanilla: Maps are in the same places they appear in the vanilla game.
    - Own Dungeon: Maps are randomized to locations in the dungeon they are used in.
    - Own Region: Maps are randomized inside and in the vicinity of their own dungeon.
    - Any Dungeon: Maps are randomized inside all dungeons.
    - Any Region: Maps are randomized inside and in the vicinity of all dungeons.
    - Own World: Maps are randomized to any location in the world.
    - Any World: Maps are randomized to any location in any world.
    DWS Region: 'Minish Village', 'Belari's House', 'Chest near Belari', 'Minish Cave near Belari'.
    CoF Region: 'Melari's Mines', 'Melari's Mines Outside Path', 'Pre Melari Block Puzzle Chest'.
    FOW Region: 'Wind Ruins'.
    TOD Region: 'Nothing'.
    RC Region: 'Graveyard (Not Dampe)'.
    POW Region: If Red Fusions are Removed: 'Wind Tribe', Otherwise: 'Upper Wind Tribe'.
    DHC Region: 'Castle Gardens (Not Moat)', If Pedestal Items is enabled: 'Sanctuary Pedestal'.
    """
    display_name = "Dungeon Maps"

    option_start_with = 0
    option_vanilla = 1
    option_own_dungeons = 2
    option_own_region = 3
    option_any_dungeons = 4
    option_any_region = 5
    option_own_world = 6
    option_any_world = 7

    default = 1

class TheMinishCapCompass(Choice):
    """
    - Start With: Compasses are given to you from the start.
    - Vanilla: Compasses are in the same places they appear in the vanilla game.
    - Own Dungeon: Compasses are randomized to locations in the dungeon they are used in.
    - Own Region: Compasses are randomized inside and in the vicinity of their own dungeon.
    - Any Dungeon: Compasses are randomized inside all dungeons.
    - Any Region: Compasses are randomized inside and in the vicinity of all dungeons.
    - Own World: Compasses are randomized to any location in the world.
    - Any World: Compasses are randomized to any location in any world.
    DWS Region: 'Minish Village', 'Belari's House', 'Chest near Belari', 'Minish Cave near Belari'.
    CoF Region: 'Melari's Mines', 'Melari's Mines Outside Path', 'Pre Melari Block Puzzle Chest'.
    FOW Region: 'Wind Ruins'.
    TOD Region: 'Nothing'.
    RC Region: 'Graveyard (Not Dampe)'.
    POW Region: If Red Fusions are Removed: 'Wind Tribe', Otherwise: 'Upper Wind Tribe'.
    DHC Region: 'Castle Gardens (Not Moat)', If Pedestal Items is enabled: 'Sanctuary Pedestal'.
    """
    display_name = "Compasses"

    option_start_with = 0
    option_vanilla = 1
    option_own_dungeons = 2
    option_own_region = 3
    option_any_dungeons = 4
    option_any_region = 5
    option_own_world = 6
    option_any_world = 7

    default = 1

class TheMinishCapSmallKeys(Choice):
    """
    - Start With: Small keys are given to you from the start.
    - Vanilla: Small keys are in the same places they appear in the vanilla game.
    - Own Dungeon: Small keys are randomized to locations in the dungeon they are used in.
    - Own Region: Small keys are randomized inside and in the vicinity of their own dungeon.
    - Any Dungeon: Small keys are randomized inside all dungeons.
    - Any Region: Small keys are randomized inside and in the vicinity of all dungeons.
    - Own World: Small keys are randomized to any location in the world.
    - Any World: Small keys are randomized to any location in any world.
    DWS Region: 'Minish Village', 'Belari's House', 'Chest near Belari', 'Minish Cave near Belari'.
    CoF Region: 'Melari's Mines', 'Melari's Mines Outside Path', 'Pre Melari Block Puzzle Chest'.
    FOW Region: 'Wind Ruins'.
    TOD Region: 'Nothing'.
    RC Region: 'Graveyard (Not Dampe)'.
    POW Region: If Red Fusions are Removed: 'Wind Tribe', Otherwise: 'Upper Wind Tribe'.
    DHC Region: 'Castle Gardens (Not Moat)', If Pedestal Items is enabled: 'Sanctuary Pedestal'.
    """
    display_name = "Small Keys"

    option_start_with = 0
    option_vanilla = 1
    option_own_dungeons = 2
    option_own_region = 3
    option_any_dungeons = 4
    option_any_region = 5
    option_own_world = 6
    option_any_world = 7

    default = 1

class TheMinishCapBigKey(Choice):
    """
    - Start With: Big keys are given to you from the start.
    - Vanilla: Big keys are in the same places they appear in the vanilla game.
    - Own Dungeon: Big keys are randomized to locations in the dungeon they are used in.
    - Own Region: Big keys are randomized inside and in the vicinity of their own dungeon.
    - Any Dungeon: Big keys are randomized inside all dungeons.
    - Any Region: Big keys are randomized inside and in the vicinity of all dungeons.
    - Own World: Big keys are randomized to any location in the world.
    - Any World: Big keys are randomized to any location in any world.
    DWS Region: 'Minish Village', 'Belari's House', 'Chest near Belari', 'Minish Cave near Belari'.
    CoF Region: 'Melari's Mines', 'Melari's Mines Outside Path', 'Pre Melari Block Puzzle Chest'.
    FOW Region: 'Wind Ruins'.
    TOD Region: 'Nothing'.
    RC Region: 'Graveyard (Not Dampe)'.
    POW Region: If Red Fusions are Removed: 'Wind Tribe', Otherwise: 'Upper Wind Tribe'.
    DHC Region: 'Castle Gardens (Not Moat)', If Pedestal Items is enabled: 'Sanctuary Pedestal'.
    """
    display_name = "Big keys"

    option_start_with = 0
    option_vanilla = 1
    option_own_dungeons = 2
    option_own_region = 3
    option_any_dungeons = 4
    option_any_region = 5
    option_own_world = 6
    option_any_world = 7

    default = 1

class TheMinishCapGoal(Choice):
    """
    Dark Hyrule Castle is the last dungeon in the game, it has the final boss Vaati.
    - Never Open: A barrier is placed at the front of the dungeon, The game ends when you visit the sanctuary after completing all the requirements.
    - After Requirements: A barrier is placed at the front of the dungeon, This barrier is removed when you visit the sanctuary after completing ALL the requirements. The game ends when you defeat Vaati.
    - Always Open: There is no barrier at the front of the dungeon, the game ends when you defeat Vaati.
    """
    display_name = "Dark Hyrule Castle Opens"

    option_never_open = 0
    option_after_requirements = 1
    option_always_open = 2

    default = 2
    
class TheMinishCapRequirementReward(Choice):
    """
    An item that the player receives once they meet the selected requirements.
    - Disabled: No extra item is awarded for requirement completion.
    - DHC Big Key: The DHC Big Key is instantly awarded to the player once they meet the selected requirements. Overrides whatever the general Big Key setting is.
    - Random Item: An item from the random item pool is instantly awarded to the player once they meet the selected requirements.
    """
    display_name = "Requirement Reward"

    option_disable = 0
    option_dhc_big_key = 1
    option_random_item = 2

    default = 1
        
class TheMinishCapRequiredDungeons(Range):
    """
    The number of dungeons that have to be beaten to activate the Sanctuary. 
    If you select a number of dungeons higher that what are available given the other settings chosen, then this will be lowered to the total number of accessible dungeons.
    There are 6 dungeons in the game that count:
    Deepwood Shrine
    Cave of Flames
    Fortress of Winds
    Temple of Droplets
    Royal Crypt
    Palace of Winds
    """
    display_name = "Dungeons Requirement"
    range_start = 0
    range_end = 6
    default = 0
        
class TheMinishCapSwordSetting(Choice):
    """
   The level of sword that needs to be collected to activate the Sanctuary
   """
    display_name = "Sword Requirement"

    option_no_sword = 0
    option_smith_sword = 1
    option_white_sword = 2
    option_red_sword = 3
    option_blue_sword = 4
    option_four_sword = 5

    default = 5
   
class TheMinishCapRequiredElement(Range):
    """
    The number of Elements that need to be collected to activate the Sanctuary
    """
    display_name = "Element Requirement"
    range_start = 0
    range_end = 4
    default = 4
    
class TheMinishCapFigurineHunt(DefaultOnToggle):
    """
    Carlov's Figurine pieces have been scattered into the world, collect enough of them to 
    be able to activate the Sanctuary, this is way better than a gacha game!
    Don't forget to visit Carlov's Machine to view the figurines you have collected so far.
    """
    display_name = "Figurine Hunt"

       
class TheMinishCapRequiredFigurineTotal(Range):
    """
    The total number of Figurines that get added to the item pool, the maximum amount is 136.
    """
    display_name = "Figurines in world"
    range_start = 0
    range_end = 136
    default = 0

class TheMinishCapRequiredFigurineCount(Range):
    """
    The number of Figurines required to activate the Sanctuary, do not raise this to higher than the total number of Figurines or you won't be able to beat the game silly.
    """
    display_name = "Figurines required"
    range_start = 0
    range_end = 136
    default = 0

class TheMinishCapDojo(Choice):
    """
    Dojo Swordmasters -	Dojo Swordmasters have Scrolls as their rewards.
    - Vanilla Scrolls: Dojo Swordmasters offer their vanilla rewards, this overrides Progressive Scrolls.
    - Randomized Scrolls: Scrolls are shuffled between the Dojo Swordmasters.
    - Any Item: Dojo Swordmasters are shuffled into the main pool.
    """
    display_name = " Dojo Swordmasters"

    option_vanilla_scrolls = 0
    option_randomized_scrolls = 1
    option_any_item = 2

    default = 2

class TheMinishCapCucco(Range):
    """
    How many rounds of the Cucco Minigame are playable and have an item.
    """
    display_name = "Cucco Minigame"
    range_start = 0
    range_end = 10
    default = 1
    
class TheMinishCapGoronMerchant(Range):
    """
    How many sets of Goron Merchant items are included in the random item pool.
    Each set consists of 3 items, and all 3 must be bought to advance to the next set.
    There are 5 sets in total.
    The remaining sets will be filled with junk items.
    """
    display_name = "Goron Merchant"
    range_start = 0
    range_end = 5
    default = 0

class TheMinishCapHeartRando(DefaultOnToggle):
    """
    If enabled will shuffle Heart Pieces and Heart Containers into the pool, otherwise Heart Pieces and Containers will always be found in their vanilla location. This makes any items randomized to Heart Piece locations visible prior to collecting them.
    """
    display_name = "Heart Pieces and Containers"

class TheMinishCapRupee(DefaultOnToggle):
    """
    If enabled will shuffle any free standing Rupees normally found in the world that are one off collectable, this adds a lot of extra money in the pool and certain locations will be very item dense.
    """
    display_name = "Rupees"

class TheMinishCapSpecialPots(DefaultOnToggle):
    """
    If enabled will shuffle items found is special pots around the world that contain one off collectables. This setting does not affect the LonLonRanch Key Item which will always shuffled, however if this setting is off then the pot in the ranch will always contain junk.
    """
    display_name = "Special Pots"

class TheMinishCapDigSpots(DefaultOnToggle):
    """
    If enabled will shuffle items found at special digging locations around the world that are one off collectables, Use the mitts on a patch of ground to dig up an item.
    """
    display_name = "Dig spots"

class TheMinishCapUnderwaterSpots(DefaultOnToggle):
    """
    If enabled will shuffle items found when swimming underwater at special locations (Mostly near waterfalls).
    The Locations that normally contain a Heart Piece found underwater in the lake and the Small Key found underwater in Temple of Droplets will always be junk if this setting is disabled, unless Hearts are not shuffled or Small Keys are set to Vanilla respectively.
    """
    display_name = "Underwater spots"

class TheMinishCapGoldenEnemies(DefaultOnToggle):
    """
    If enabled will shuffle items dropped by Golden Enemies once then are defeated. There are 3 kinds of Golden Enemy: "Golden Octo", "Golden Tektite" and "Golden Rope".
    These Enemies are spawned by completing certain Kinstone Fusions in the game, if you remove certain kinstone colors then those enemies made innaccessible will not have items.
    These enemies have a lot of health but are not invulnerable, Keep hitting them
    """
    display_name = "Golden Enemies"

class TheMinishCapSanctuaryPedestal(DefaultOnToggle):
    """
    This setting is force disabled when playing on any DHC setting other than 'Always Open'.
    If enabled will shuffle 3 items onto the pedestal found in the Sanctuary, these can be collected when the pedestal is visited with 2 elements, 3 elements and 4 elements respectively.
   """
    display_name = "Sanctuary Pedestal"
    
class TheMinishCapOpenWorld(Choice):
    """
    Does not affect Key Doors, Fusions, Wind Crests and Dungeon Warps.
    Open: Opens every permanently solvable obstacle in the game: Every cut tree, cracked block, bomb wall, boulder shortcut, non key door, bean vine, switch, lever, chest spawn and extendable bridge.
    """
    display_name = "World obstacles"

    option_open = 0
    option_standard = 1

    default = 1

class TheMinishCapDungeonEntrance(Choice):
    """
    The 6 Dungeons that can hold elements may have their entrances shuffled. These are always coupled entrance swaps which means when you leave a shuffled dungeon you will always go back to the place you originally came from.
    Dark Hyrule Castle is not currently shuffled.
    Vanilla: Dungeon entrances are not shuffled.
    Shuffled: All Dungeon entrances are shuffled between each other, these are the following dungeons that are shuffled:
        Deepwood Shrine
        Cave of Flames
        Fortress of Winds
        Temple of Droplets
        Royal Crypt
        Palace of Winds
    """
    display_name = "Dungeon Entrances"

    option_vanilla = 0
    option_shuffle = 1

    default = 0


class TheMinishCapGoldFusions(Choice):
    """
    Golden Kinstones come in 3 shapes: 5 for Cloud Tops, 3 for Castor Wilds (Swamp), and 1 for Veil Falls (A Crown) for 9 in Total.
    The fusions that require Golden Kinstones lock major areas of the game.
    - Removed: All the Gold Kinstones are removed from the pool, and the fusions are unable to be completed. This prevents Fortress of Winds from being reachable, and without the Open Wind Tribe setting this will prevent Palace of Winds from being reachable.
    - Vanilla: This shuffles the 3 different shaped Golden Kinstones into the pool (9 total: 5/3/1), the locations of the fusions and what shape they ask for are not shuffled.
    - Combined: This converts the different shaped Golden Kinstones into a single Golden shape. 9 of these are shuffled into the world, the locations of the fusions are not shuffled and all ask for the same shape.
    - Completed: All the Golden Kinstones are removed from the pool, and all the fusions are already completed.
    """
    display_name = "Gold Fusions"

    option_removed = 0
    option_vanilla = 1
    # option_combined = 2
    # option_completed = 3

    default = 1

class TheMinishCapRedFusions(Choice):
    """
    Red Kinstones come in 3 shapes, Fusions can be found everywhere but are mostly from unique individuals.
    There are 24 Fusions in total, There are more Kinstones in the pool than fusions available just to be generous.
    - Removed: All the Red Kinstones are removed from the pool, and the fusions are unable to be completed.
    - Vanilla: This shuffles the 3 different shaped Red Kinstones into the pool, the exact amount needed to do every available fusion, the locations of the fusions and what shape they ask for are not shuffled.
    - Combined: This converts the different shaped Red Kinstones into a single Red shape. The locations of the fusions are not shuffled and all ask for the same shape.
    - Completed: All the Red Kinstones are removed from the pool, and all the fusions are already completed.
    """
    display_name = "Red Fusions"

    option_removed = 0
    option_vanilla = 1
    # option_combined = 2
    # option_completed = 3

    default = 1



class TheMinishCapBlueFusions(Choice):
    """
    Blue Kinstones come in 2 shapes, Fusions can be found everywhere but are mostly from Walls or unique individuals.
    There are 18 Fusions in total, There are more Kinstones in the pool than fusions available just to be generous.
    - Removed: All the Blue Kinstones are removed from the pool, and the fusions are unable to be completed.
    - Vanilla: This shuffles the 2 different shaped Blue Kinstones into the pool, the exact amount needed to do every available fusion, the locations of the fusions and what shape they ask for are not shuffled.
    - Combined: This converts the different shaped Blue Kinstones into a single Blue shape. The locations of the fusions are not shuffled and all ask for the same shape.
    - Completed: All the Blue Kinstones are removed from the pool, and all the fusions are already completed.
    """
    display_name = "Blue Fusions"

    option_removed = 0
    option_vanilla = 1
    # option_combined = 2
    # option_completed = 3

    default = 1


class TheMinishCapGreenFusions(Choice):
    """
    Green Kinstones come in 3 shapes, Fusions can be found everywhere and a large amount are shared between many people.
    There are 49 Fusions in total, There are more Kinstones in the pool than fusions available just to be generous.
    - Removed: All the Green Kinstones are removed from the pool, and the fusions are unable to be completed.
    - Vanilla: This shuffles the 3 different shaped Green Kinstones into the pool, the exact amount needed to do every available fusion, the locations of the fusions and what shape they ask for are not shuffled.
    - Combined: This converts the different shaped Green Kinstones into a single Green shape. The locations of the fusions are not shuffled and all ask for the same shape.
    - Completed: All the Green Kinstones are removed from the pool, and all the fusions are already completed.
    """
    display_name = "Green Fusions"

    option_removed = 0
    option_vanilla = 1
    # option_combined = 2
    # option_completed = 3

    default = 1

class TheMinishCapOrderSharedFusions(DefaultOnToggle):
    """
    There is a Pool of 18 Shared Fusions in the Game: 16 Green, 1 Blue and 1 Red. These Fusions are randomly selected by an NPC who offers Shared Fusions when you enter the room they are in.
    If this setting is enabled then the seed generates a listed order these NPCs offer the Fusions in. This makes different people playing the same seed have the same Fusions available which is useful for races.
    """
    display_name = "Order Shared Fusions"

class TheMinishCapDefickleFusers(DefaultOnToggle):
    """
    Many NPCs who offer fusions are considered 'Fickle', this means they can randomly decide to NOT offer their fusion.
    Enable this to make them ALWAYS offer a fusion.
    """
    display_name = "Defickle Fusers"

class TheMinishCapGreenFusions(Choice):
    """
    When doing a Kinstone Fusion you get a cutscene aftewards to show you what the fusion activated, and then a Map indicator spawns.
    - Never: The cutscene is never able to be skipped by the player.
    - Choose: If you hold a button prior to the start of the cutscene, then the cutscene is skipped, otherwise the cutscene plays normally.
        If 'Show Map' is enabled then only the cutscene is skipped, but the map screen is still shown.
    - Always: The cutscene is always skipped without player input.
        If 'Show Map' is enabled then it will always show the map screen.
    """
    display_name = "Skip Fusion Cutscenes"

    option_never = 0
    option_choose = 1
    option_always = 2

    default = 2

class TheMinishCapWindTribeTower(DefaultOnToggle):
    """
    If enabled, Wind Tribe Tower will act like it has already been entered from Cloud Tops from the start of the game. This unlocks the upper floors, Gregal's 2nd item and the main exit to Cloud tops early.\nCertain combinations of settings may allow for a softlock when going to Cloud tops without the Tornado being completed, Homewarp will always be available in these situations.\n\nIf disabled, Wind Tribe will stay in its initial state until the player enters the building from Cloud Tops.
    """
    display_name = "Wind Tribe Tower"

class TheMinishCapTingleBrothers(DefaultOnToggle):
    """
    If enabled, will spawn Tingle's brothers Knuckle, Ankle and David Jr. from the start of the game.\nIf disabled, the Tingle brothers will only spawn after talking to Tingle twice in a row.
    """
    display_name = "Tingle Brothers"

class TheMinishCapWindCrestsMtCrenel(DefaultOnToggle):
    """
If enabled, will activate the wind crest in Mt Crenel from the start of the game.
    """
    display_name = "Wind Crests (Mt Crenel)"
class TheMinishCapWindCrestsVeilFalls(DefaultOnToggle):
    """
    If enabled, will activate the wind crest in Veil Falls from the start of the game.
    """
    display_name = "Wind Crests (Veil Falls)"

class TheMinishCapWindCrestsCloudTops(DefaultOnToggle):
    """
    If enabled, will activate the wind crest in Cloud Tops from the start of the game.
    """
    display_name = "Wind Crests (Cloud Tops)"

class TheMinishCapWindCrestsHyruleTown(DefaultOnToggle):
    """
    If enabled, will activate the wind crest in Hyrule Town from the start of the game.
    Note: This is always enabled if Homewarp is disabled.
    """
    display_name = "Wind Crests (Hyrule Town)"

class TheMinishCapWindCrestsSwamp(DefaultOnToggle):
    """
    If enabled, will activate the wind crest in Swamp from the start of the game.
    """
    display_name = "Wind Crests (Swamp)"

class TheMinishCapWindCrestsLinkHouse(DefaultOnToggle):
    """
    If enabled, will activate the wind crest near Link's House from the start of the game.
    """
    display_name = "Wind Crests (Link's House)"

class TheMinishCapWindCrestsMinishWoods(DefaultOnToggle):
    """
    If enabled, will activate the wind crest in Minish Woods from the start of the game.
    """
    display_name = "Wind Crests (Minish Woods)"
    
class TheMinishCapDungeonWarpsDWSBlue(DefaultOnToggle):
    """
    If enabled, will activate the DeepwoodShrine Blue Warp from the start of the game.
    """
    display_name = "Dungeon Warps (DWS Blue)"

class TheMinishCapDungeonWarpsDWSRed(DefaultOnToggle):
    """
    If enabled, will activate the DeepwoodShrine Red Warp from the start of the game.
    """
    display_name = "Dungeon Warps (DWS Red)"

class TheMinishCapDungeonWarpsCoFBlue(DefaultOnToggle):
    """
    If enabled, will activate the Cave of Flames Blue Warp from the start of the game.
    """
    display_name = "Dungeon Warps (CoF Blue)"

class TheMinishCapDungeonWarpsCoFRed(DefaultOnToggle):
    """
    If enabled, will activate the Cave of Flames Red Warp from the start of the game.
    """
    display_name = "Dungeon Warps (CoF Red)"

class TheMinishCapDungeonWarpsFoWBlue(DefaultOnToggle):
    """
    If enabled, will activate the Fortress of Winds Blue Warp from the start of the game.
    """
    display_name = "Dungeon Warps (FoW Blue)"

class TheMinishCapDungeonWarpsFoWRed(DefaultOnToggle):
    """
    If enabled, will activate the Fortress of Winds Red Warp from the start of the game.
    """
    display_name = "Dungeon Warps (FoW Red)"

class TheMinishCapDungeonWarpsToDBlue(DefaultOnToggle):
    """
    If enabled, will activate the Temple of Droplets Blue Warp from the start of the game.
    """
    display_name = "Dungeon Warps (ToD Blue)"

class TheMinishCapDungeonWarpsToDRed(DefaultOnToggle):
    """
    If enabled, will activate the Temple of Droplets Red Warp from the start of the game.
    """
    display_name = "Dungeon Warps (ToD Red)"

class TheMinishCapDungeonWarpsPoWBlue(DefaultOnToggle):
    """
    If enabled, will activate the Palace of Winds Blue Warp from the start of the game.
    """
    display_name = "Dungeon Warps (PoW Blue)"

class TheMinishCapDungeonWarpsPoWRed(DefaultOnToggle):
    """
    If enabled, will activate the Palace of Winds Red Warp from the start of the game.
    """
    display_name = "Dungeon Warps (PoW Red)"

class TheMinishCapDungeonWarpsDHCBlue(DefaultOnToggle):
    """
    If enabled, will activate the Dark Hyrule Castle Blue Warp from the start of the game.
    """
    display_name = "Dungeon Warps (DHC Blue)"

class TheMinishCapDungeonWarpsDHCRed(DefaultOnToggle):
    """
    If enabled, will activate the Dark Hyrule Castle Red Warp from the start of the game.
    """
    display_name = "Dungeon Warps (DHC Red)"
    
# class TheMinishCapLogicRules(DefaultOnToggle):
    # """
    # Items can go anywhere without regard to logic.
    # LIKELY RESULTS IN UNBEATABLE SEEDS
    # """
    # display_name = "No Logic"


class TheMinishCapAccessibility(Choice):
    """
    Determines which items and locations are guaranteed to be reachable.
    - All Locations: All enabled locations are reachable.
    - All NonKeys: Like 'All Locations', except keys can lock themselves.
    - Only the Goal: Only the goal is guaranteed to be reachable. Some locations and items may be inaccessible. If DHC setting is set to 'Never Open' then the goal is the pedestal requirements, otherwise the goal is Defeat Vaati.

    """
    display_name = "Reachable"

    option_all_location = 0
    option_all_non_Key = 1
    option_goal = 2

    default = 0

class TheMinishCapGrabbable(Choice):
    """
    Items can be collected from a distance with either Gust Jar, Boomerang, or even a Sword Slash.
    - Not Allowed: Items cannot be grabbed from a distance.
    - Allowed: Items can be grabbed from a distance, but this will never be required by logic.
    - Require: Items can be grabbed from a distance and logic can require grabbing them when they are obviously grabbable.
    - Require Hard: Items can be grabbed from a distance, and logic can require some very difficult Boomerang throws to be able to collect these items.\nMany of these involve throwing the Boomerang in an arc behind or to the side of the items before making Link run in the opposite direction to get the Boomerang to grab the item on the return journey to Link.
    """
    display_name = "Grabbable"

    option_not_allowed = 0
    option_allowed = 1
    option_require = 2
    option_require_hard = 3

    default = 0


class TheMinishCapBombWeapon(Choice):
    """
    Bombs can damage nearly every enemy, Bombs are never considered for Simon Simulations, and Golden Enemies.
    - none: Bombs are not considered as Weapons.
    - allowed: Bombs are considered as weapons for most regular enemy fights.
    allowed + boss: Bombs are considered as weapons for most enemy fights. Fighting Green/Blu Chu, Madderpillars and Darknuts require only 10 bomb bag. Gleerok, Mazaal and Scissor Beetles require at least 30 bomb bag. Octo and Gyorg cannot be defeated with bombs.
    """
    display_name = "Bomb Weapon"

    option_none= 0
    option_allowed = 1
    option_allowed_boss = 2

    default = 0

class TheMinishCapBowWeapon(Choice):
    """
    Bow can damage most enemies, many enemies are very resiliant to damage. Chu Bosses and Darknuts are Immune.
    - none: Bows are not considered as Weapons.
    - allowed: Bows are considered as weapons for most enemy fights. Bows are never considered for Chu Bossfights, Darknuts, Scissor Beetles, Madderpillar, Wizrobes, Simon Simulations, and Golden Enemies.
    allowed + boss: Bows are considered as weapons for most enemy fights, but can also be solely required to defeat Gleerok and Mazaal.
    """
    display_name = "Bows Weapon"

    option_none= 0
    option_allowed = 1
    option_allowed_boss = 2

    default = 0

class TheMinishCapGustJarWeapon(Choice):
    """
    Gust Jar can suck up various enemies like Ghini(Ghosts) and Beetles (The things that grab onto link). It can also grab objects and fire them like projectiles to kill enemies, some enemies or parts of enemies can be used as projectiles such as Helmasaurs and Stalfos.
    - none: Gust Jar is never considered for killing enemies.
    - allowed: Gust Jar is considered as weapons for all enemies that get sucked up by it, you are never expected to use objects as projectiles to kill enemies.
    """
    display_name = "Gust Jar Weapon"

    option_none= 0
    option_allowed = 1

    default = 0


class TheMinishCapLanternWeapon(Choice):
    """
    The lit Lantern can instantly kill wizrobes by walking through them.
    - none: Lantern is not considered as a Weapon.
    - allowed: Lantern is considered as a weapon for fighting Wizrobes.
    """
    display_name = "Lantern Weapon"

    option_none= 0
    option_allowed = 1

    default = 0


class TheMinishCapMittsMoney(Choice):
    """
    Mole Mitts farm Infinite Rupees
    Low Difficulty:
    single spot outside of Link's house can be dug to find a 20 Rupee that respawns every time you leave link's house.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You may be required to farm rupees outside link's house to afford purchasing items if Mitts are acquired.
    """
    display_name = "Mole Mitts Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapBlowdust(Choice):
    """
    Bombs blow away dust
    Low Difficulty:
    Dust piles can be found that can be blown away to what is underneath.
    - none: Gust Jar will always be required to blow away dust piles.
    - allowed: Bombs may be required to blow away dust piles instead of Gust Jar. 
    """
    display_name = "Bombs blow"

    option_none= 0
    option_allowed = 1

    default = 0
--
class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1
--
    default = 0

class TheMinishCapCrenelMushroom(Choice):
    """
    Crenel mushroom grab with Gust jar
    Low Difficulty:
    Half way up Mt Crenel across the wooden bridge, the mushroom on the ledge above can be grabbed with the Gust Jar to continue climbing up the mountain.\nThis only matters when playing with 'OpenWorld' enabled, since reaching this area requires either Bombs or Grip ring.
    - none: You will always be expected to have Bombs or Grip Ring to continue up the mountain.
    - allowed: You may be required to use the Gust Jar to grab the mushroom to continue up the mountain.
    """
    display_name = "Crenel mushroom"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
Light Arrows break objects
    Low Difficulty:
Fully charged Light Arrow shots can break pots, bushes, and small trees.
    - none: Light Arrows will never be required to break objects.
    - allowed: Some obstacles may require Light Arrows to destroy.
    """
    display_name = "Light Arrows"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0

class TheMinishCapGuaranteedBarlov(Choice):
    """
    Barlov farm Infinite Rupees
    Low Difficulty:
    Changes the gambling game ran by Barlov in town so no matter what chest you pick you will always win. Does not current affect logic.
    - none: You will always require finding enough rupees in the item pool before you have to buy items.
    - allowed: You will be required to farm rupees from the Barlov game in town to afford purchasing items.
    """
    display_name = "Barlov Money"

    option_none= 0
    option_allowed = 1

    default = 0
@dataclass
class TheMinishCapOptions(PerGameCommonOptions):
	DungeonsMap: TheMinishCapDungeonsMap
	Compass: TheMinishCapCompass
	SmallKeys: TheMinishCapSmallKeys
	BigKey: TheMinishCapBigKey
    Goal: TheMinishCapGoal
    RequirementReward: TheMinishCapRequirementReward
    RequiredDungeons: TheMinishCapRequiredDungeons
    SwordSetting: TheMinishCapSwordSetting
    RequiredElement: TheMinishCapRequiredElement
    FigurineHunt: TheMinishCapFigurineHunt
    RequiredFigurineTotal: TheMinishCapRequiredFigurineTotal
    RequiredFigurineCount: TheMinishCapRequiredFigurineCount
    Dojo: TheMinishCapDojo
    Cucco: TheMinishCapCucco
    GoronMerchant: TheMinishCapGoronMerchant
    HeartRando: TheMinishCapHeartRando
    Rupee: TheMinishCapRupee
    SpecialPots: TheMinishCapSpecialPots
    DigSpots: TheMinishCapDigSpots
    UnderwaterSpots: TheMinishCapUnderwaterSpots
    GoldenEnemies: TheMinishCapGoldenEnemies
    SanctuaryPedestal: TheMinishCapSanctuaryPedestal
    OpenWorld: TheMinishCapOpenWorld
    DungeonEntrance: TheMinishCapDungeonEntrance
    GoldFusions: TheMinishCapGoldFusions
    RedFusions: TheMinishCapRedFusions
    BlueFusions: TheMinishCapBlueFusions
    GreenFusions: TheMinishCapGreenFusions
    OrderSharedFusions: TheMinishCapOrderSharedFusions
    DefickleFusers: TheMinishCapDefickleFusers
    GreenFusions: TheMinishCapGreenFusions
    WindTribeTower: TheMinishCapWindTribeTower
    TingleBrothers: TheMinishCapTingleBrothers
    WindCrestsMtCrenel: TheMinishCapWindCrestsMtCrenel
    WindCrestsVeilFalls: TheMinishCapWindCrestsVeilFalls
    WindCrestsCloudTops: TheMinishCapWindCrestsCloudTops
    WindCrestsHyruleTown: TheMinishCapWindCrestsHyruleTown
    WindCrestsSwamp: TheMinishCapWindCrestsSwamp
    WindCrestsLinkHouse: TheMinishCapWindCrestsLinkHouse
    WindCrestsMinishWoods: TheMinishCapWindCrestsMinishWoods
    DungeonWarpsDWSBlue: TheMinishCapDungeonWarpsDWSBlue
    DungeonWarpsDWSRed: TheMinishCapDungeonWarpsDWSRed
    DungeonWarpsCoFBlue: TheMinishCapDungeonWarpsCoFBlue
    DungeonWarpsCoFRed: TheMinishCapDungeonWarpsCoFRed
    DungeonWarpsFoWBlue: TheMinishCapDungeonWarpsFoWBlue
    DungeonWarpsFoWRed: TheMinishCapDungeonWarpsFoWRed
    DungeonWarpsToDBlue: TheMinishCapDungeonWarpsToDBlue
    DungeonWarpsToDRed: TheMinishCapDungeonWarpsToDRed
    DungeonWarpsPoWBlue: TheMinishCapDungeonWarpsPoWBlue
    DungeonWarpsPoWRed: TheMinishCapDungeonWarpsPoWRed
    DungeonWarpsDHCBlue: TheMinishCapDungeonWarpsDHCBlue
    DungeonWarpsDHCRed: TheMinishCapDungeonWarpsDHCRed
#    LogicRules: TheMinishCapLogicRules
    Accessibility: TheMinishCapAccessibility
    Grabbable: TheMinishCapGrabbable
    BombWeapon: TheMinishCapBombWeapon
    BowWeapon: TheMinishCapBowWeapon
    GustJarWeapon: TheMinishCapGustJarWeapon
    LanternWeapon: TheMinishCapLanternWeapon
    MittsMoney: TheMinishCapMittsMoney
    GuaranteedBarlov: TheMinishCapGuaranteedBarlov