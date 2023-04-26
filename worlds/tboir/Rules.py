from BaseClasses import MultiWorld, CollectionState
from worlds.generic.Rules import set_rule, add_rule


def set_rules(world: MultiWorld, player: int):
    set_rule(world.get_location("Run End", player),
             lambda state: state.has(f"Progression Item", player, world.progression_item_count * world.required_prog_item_factor)
                           and state.can_reach(world.get_location(f"ItemPickup{world.required_locations[player].value}", player).parent_region)
             )

    world.completion_condition[player] = lambda state: state.has("Victory", player)
