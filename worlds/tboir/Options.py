import typing
from Options import Option, DefaultOnToggle, Range, Choice, AssembleOptions, DeathLink


class TotalLocations(Range):
    """Number of location checks which are added."""
    display_name = "Total Locations"
    range_start = 10
    range_end = 500
    default = 20


class RequiredLocationsPercent(Range):
    """Number of location checks which are required to beat the game."""
    display_name = "Total Locations"
    range_start = 1
    range_end = 100
    default = 80


class Goal(Choice):
    """Goal to finish the run"""
    display_name = "Goal"
    option_mom = 0
    option_moms_heart = 1
    option_isaac_satan = 2
    option_isaac = 3
    option_satan = 4
    option_blue_baby_lamb = 5
    option_blue_baby = 6
    option_lamb = 7
    option_mega_satan = 8
    option_boss_rush = 9
    option_hush = 10
    option_dogma = 11
    option_beast = 12
    option_mother = 13
    option_delirium = 14
    option_required_locations = 15


class ItemPickupStep(Range):
    """Number of items to pick up before an AP Check is completed.
    Setting to 1 means every other pickup.
    Setting to 2 means every third pickup. So on..."""
    display_name = "Item Pickup Step"
    range_start = 1
    range_end = 5
    default = 1

class AdditonalBossRewards(DefaultOnToggle):
    """If enabled all goal bosses will reward additional checks.
    The amount of checks if determined on how deep the boss in the run:
    Mom = 1
    Mom's Heart/Boss Rush = 2
    Isaac/Satan/Hush = 3
    Blue Baby/The Lamb = 4
    Mega Satan/Mother/Beast/Delirium = 5
    exception:
    Dogma = 0
    """
    display_name = "Additional Boss Rewards"

class TrapPercentage(Range):
    """Replaces a percentage of junk items with traps"""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 0

class ItemChanceMeta(AssembleOptions):
    def __new__(mcs, name, bases, attrs):
        if 'item_name' in attrs:
            attrs["display_name"] = f"{attrs['item_name']} Chance"
        attrs["range_start"] = 0
        attrs["range_end"] = 100

        return super(ItemChanceMeta, mcs).__new__(mcs, name, bases, attrs)


class TrapChance(Range, metaclass=ItemChanceMeta):
    item_name: str
    default = 20


class TrapChanceTrollBombs(TrapChance):
    """Sets the chance/ratio of troll bombs traps"""
    item_name = "Troll Bombs Trap"

class TrapChanceTeleport(TrapChance):
    """Sets the chance/ratio of teleport traps"""
    item_name = "Teleport Trap"

class TeleportTrapCanError(DefaultOnToggle):
    """Can a teleport trap teleport to an Error Room?"""
    display_name = "Teleport Trap can teleport to Error Room"

class TrapChanceRetroVision(TrapChance):
    """Sets the chance/ratio of retro vision traps"""
    item_name = "Retro Vision Trap"

class TrapChanceCurse(TrapChance):
    """Sets the chance/ratio of curse traps"""
    item_name = "Curse Trap"


tobir_options: typing.Dict[str, type(Option)] = {
    "total_locations": TotalLocations,
    "required_locations": RequiredLocationsPercent,
    "goal": Goal,
    "item_pickup_step": ItemPickupStep,
    "additional_boss_rewards": AdditonalBossRewards,
    "death_link": DeathLink,
}
