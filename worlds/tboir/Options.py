import typing
from Options import Option, DefaultOnToggle, Range, Choice


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


class ItemPickupStep(Range):
    """Number of items to pick up before an AP Check is completed.
    Setting to 1 means every other pickup.
    Setting to 2 means every third pickup. So on..."""
    display_name = "Item Pickup Step"
    range_start = 1
    range_end = 5
    default = 1


tobir_options: typing.Dict[str, type(Option)] = {
    "total_locations": TotalLocations,
    "required_locations": RequiredLocationsPercent,
    "goal": Goal,
    "item_pickup_step": ItemPickupStep
}
