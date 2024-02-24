from worlds.tloz_oos.data.logic.LogicPredicates import *


def make_subrosia_logic(player: int):
    return [
        # Portals ###############################################################

        ["subrosia portal 1", "subrosia temple sector", True, None],
        ["subrosia portal 2", "subrosia market sector", True, None],
        ["subrosia portal 3", "subrosia hide and seek sector", True, lambda state: oos_has_feather(state, player)],
        ["subrosia portal 4", "subrosia pirates sector", True, None],
        ["subrosia portal 5", "subrosia furnace sector", True, None],
        ["subrosia portal 6", "subrosia volcano sector", True, None],
        ["subrosia portal 7", "d8 entrance", True, None],

        ["subrosia pirates sector", "western coast after ship", False, lambda state: state.has("Pirate's Bell", player)],

        # Regions ###############################################################

        ["subrosia temple sector", "subrosia market sector", True, lambda state: oos_has_feather(state, player)],
        
        ["subrosia market sector", "subrosia temple sector", False, lambda state: oos_can_date_rosa(state, player)],
        ["subrosia market sector", "subrosia east junction", True, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_can_jump_4_wide_pit(state, player),
            all([
                # As it is a "diagonal" pit, it is considered as a 4-wide in easy and as a 3-wide in medium+
                oos_option_medium_logic(state, player),
                oos_can_jump_3_wide_pit(state, player)
            ])
        ])],
        ["subrosia east junction", "subrosia market sector", False, lambda state: all([
            # This backwards route adds itself on top of the two-way route right above this one, adding the option
            # to remove the rock using the bracelet to turn this pit into a 2-wide jump
            oos_has_bracelet(state, player),
            oos_can_jump_2_wide_pit(state, player)
        ])],

        ["subrosia temple sector", "subrosia bridge sector", True, lambda state: oos_has_feather(state, player)],
        ["subrosia volcano sector", "subrosia bridge sector", False, lambda state: all([
            oos_has_bracelet(state, player),
            oos_can_jump_3_wide_liquid(state, player)
        ])],
        ["subrosia volcano sector", "bomb temple remains", False, lambda state: oos_has_bombs(state, player)],

        ["subrosia hide and seek sector", "subrosia market sector", False, lambda state: all([
            oos_has_bracelet(state, player),
            oos_has_feather(state, player),
            any([
                oos_can_jump_2_wide_liquid(state, player),
                oos_has_magnet_gloves(state, player)
            ])
        ])],
        ["subrosia hide and seek sector", "subrosia temple sector", True, lambda state: oos_can_jump_4_wide_liquid(state, player)],
        ["subrosia hide and seek sector", "subrosia pirates sector", True, lambda state: oos_has_feather(state, player)],

        ["subrosia east junction", "subrosia furnace sector", True, lambda state: oos_has_feather(state, player)],

        # Locations ###############################################################

        ["subrosia temple sector", "subrosian dance hall", False, None],
        ["subrosia temple sector", "subrosian smithy ore", False, lambda state: state.has("Hard Ore", player)],
        ["subrosia temple sector", "subrosian smithy bell", False, lambda state: state.has("Rusty Bell", player)],
        ["subrosia temple sector", "temple of seasons", False, None],
        ["subrosia temple sector", "tower of winter", False, lambda state: any([
            oos_has_feather(state, player),
            oos_can_trigger_far_switch(state, player)
        ])],
        ["subrosia temple sector", "tower of summer", False, lambda state: all([
            oos_can_date_rosa(state, player),
            oos_has_bracelet(state, player),
        ])],
        ["subrosia temple sector", "tower of autumn", False, lambda state: all([
            oos_has_feather(state, player),
            state.has("Bomb Flower", player)
        ])],

        ["subrosia market sector", "subrosia seaside", False, lambda state: oos_has_shovel(state, player)],
        ["subrosia market sector", "subrosia market, 1st item", False, lambda state: state.has("Star Ore", player)],
        ["subrosia market sector", "subrosia market, 2nd item", False, lambda state: all([
            oos_has_ember_seeds(state, player),
            oos_can_farm_ore(state, player)
        ])],
        ["subrosia market sector", "subrosia market, 5th item", False, lambda state: oos_can_farm_ore(state, player)],

        ["subrosia hide and seek sector", "tower of spring", False, lambda state: oos_has_feather(state, player)],
        ["subrosia hide and seek sector", "subrosian wilds chest", False, lambda state: all([
            oos_has_feather(state, player),
            any([
                oos_has_magnet_gloves(state, player),
                oos_can_jump_4_wide_pit(state, player)
            ])
        ])],
        ["subrosian wilds chest", "subrosian wilds digging spot", False, lambda state: all([
            any([
                oos_can_jump_3_wide_pit(state, player),
                oos_has_magnet_gloves(state, player)
            ]),
            oos_has_feather(state, player),
            oos_has_shovel(state, player)
        ])],

        ["subrosia hide and seek sector", "subrosian house", False, lambda state: oos_has_feather(state, player)],
        ["subrosia hide and seek sector", "subrosian 2d cave", False, lambda state: oos_has_feather(state, player)],

        ["subrosia bridge sector", "subrosia, open cave", False, None],
        ["subrosia bridge sector", "subrosia, locked cave", False, lambda state: all([
            oos_can_date_rosa(state, player),
            oos_has_feather(state, player)
        ])],
        ["subrosia bridge sector", "subrosian chef trade", False, lambda state: state.has("Iron Pot", player)],

        ["subrosia east junction", "subrosia village chest", False, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_can_jump_4_wide_pit(state, player),
            all([
                # TODO: Test if it's indeed possible
                oos_option_medium_logic(state, player),
                oos_can_jump_3_wide_pit(state, player)
            ])
        ])],

        ["subrosia furnace sector", "great furnace", False, lambda state: all([
            state.has("Red Ore", player),
            state.has("Blue Ore", player),
            state.has("_opened_tower_of_autumn", player)
        ])],
        ["subrosia furnace sector", "bomb flower", False, lambda state: all([
            oos_has_feather(state, player),
            oos_has_bracelet(state, player)
        ])],
    ]

