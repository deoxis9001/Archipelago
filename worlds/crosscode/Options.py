from Options import AssembleOptions, Choice, DefaultOnToggle, Toggle
import typing

class VTShadeLock(DefaultOnToggle):
    """
    If enabled, adds a locked gate before the final dungeon that only opens when all four shades are collected and all four bosses are beaten.
    """
    display_name = "Vermillion Tower Shade Lock"

class VTSkip(DefaultOnToggle):
    """
    If enabled, Vermillion Tower will not need to be completed; instead, the player will skip through it to the final boss.
    """
    display_name = "Skip Vermillion Tower"

class QuestRando(Toggle):
    """
    If enabled, all quests will be randomized along with chests and cutscene locations.
    """
    display_name = "Quest Randomization"

class HiddenQuestRewardMode(Choice):
    """
    Some quests hide their rewards until they are completed.
    [Vanilla] Behavior is unchanged from the base game.
    [Show All] Show all rewards regardless of whether they're hidden in the base game.
    [Hide All] Hide all rewards regardless of whether they're hidden in the base game.
    """
    display_name = "Show Hidden Quest Rewards"

    option_vanilla = 0
    option_show_all = 1
    option_hide_all = 2

    default = 0

class HiddenQuestObfuscationLevel(Choice):
    """
    For quests with hidden rewards, this option controls the level to which rewards are obscured.
    [Hide Item] Only hides the item name. The icon and receiving player are still accurate.
    [Hide Text] Obscures item name and receiving player. The icon will still be accurate.
    [Hide All] The item name and receiving player will all be hidden and the icon will be replaced with a generic archipelago logo.
    """
    display_name = "Hidden Quest Obfuscation Level"

    option_hide_item = 0
    option_hide_text = 1
    option_hide_all = 2

    default = 0

class QuestDialogHints(DefaultOnToggle):
    """
    If enabled, upon viewing the quest dialog for a quest with rewards that are not hidden, corresponding hints are sent to the archipelago server.
    """
    display_name = "Quest Dialog Hints"

class StartWithGreenLeafShade(DefaultOnToggle):
    """
    If enabled, the player will start with the green leaf shade, unlocking Autumn's Fall. This makes the early game far more open.
    """
    display_name = "Start with Green Leaf Shade"

class StartWithChestDetector(DefaultOnToggle):
    """
    If enabled, the player will start with the chest detector item, which will notify them of the chests in the room.
    """
    display_name = "Start with Chest Detector"

class Reachability(Choice):
    option_own_world = 0
    option_different_world = 1
    option_any_world = 2

    default = 2

class ShadeLocations(Reachability):
    """
    Where shades will appear.
    """
    display_name = "Shade Locations"

class ElementLocations(Reachability):
    """
    Where elements will appear.
    """
    display_name = "Element Locations"

crosscode_options_pairs = [
    ("vt_shade_lock", VTShadeLock),
    ("vt_skip", VTSkip),
    ("quest_rando", QuestRando),
    ("hidden_quest_reward_mode", HiddenQuestRewardMode),
    ("hidden_quest_obfuscation_level", HiddenQuestObfuscationLevel),
    ("quest_dialog_hints", QuestDialogHints),
    ("start_with_green_leaf_shade", StartWithGreenLeafShade),
    ("start_with_chest_detector", StartWithChestDetector),
    ("shade_locations", ShadeLocations),
    ("element_locations", ElementLocations),
]

addon_options = ["vt_shade_lock", "quest_rando"]

try:
    from .GeneratedOptions import LogicMode
    crosscode_options_pairs.insert(0, ("logic_mode", LogicMode))
except ImportError:
    pass

crosscode_options: typing.Dict[str, AssembleOptions] = dict(crosscode_options_pairs)
