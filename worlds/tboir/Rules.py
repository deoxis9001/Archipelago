from BaseClasses import MultiWorld, CollectionState
from worlds.generic.Rules import set_rule, add_rule


def set_rules(world: MultiWorld, player: int):
    total_locations = world.total_locations[player]  # total locations for current player

    set_rule(world.get_location("Victory", player),
             lambda state: state.can_reach(f"ItemPickup{total_locations}", "Location", player))

    world.completion_condition[player] = lambda state: state.has("Victory", player)
