from BaseClasses import CollectionState
from worlds.tloz_oos.data.Constants import DUNGEON_NAMES, SEASON_ITEMS, ESSENCES


# Items predicates ############################################################

def oos_has_sword(state: CollectionState, player: int):
    return state.has("Progressive Sword", player)


def oos_has_noble_sword(state: CollectionState, player: int):
    return state.has("Progressive Sword", player, 2)


def oos_has_shield(state: CollectionState, player: int):
    return state.has("Wooden Shield", player) or state.has("Iron Shield", player)


def oos_has_fools_ore(state: CollectionState, player: int):
    return state.has("Fool's Ore", player)


def oos_has_feather(state: CollectionState, player: int):
    return state.has("Progressive Feather", player)


def oos_has_cape(state: CollectionState, player: int):
    return state.has("Progressive Feather", player, 2)


def oos_has_satchel(state: CollectionState, player: int):
    return state.has("Seed Satchel", player)


def oos_has_slingshot(state: CollectionState, player: int):
    return state.has("Progressive Slingshot", player)


def oos_has_hyper_slingshot(state: CollectionState, player: int):
    return state.has("Progressive Slingshot", player, 2)


def oos_has_boomerang(state: CollectionState, player: int):
    return state.has("Progressive Boomerang", player)


def oos_has_magic_boomerang(state: CollectionState, player: int):
    return state.has("Progressive Boomerang", player, 2)


def oos_has_bracelet(state: CollectionState, player: int):
    return state.has("Bracelet", player)


def oos_has_shovel(state: CollectionState, player: int):
    return state.has("Shovel", player)


def oos_has_flippers(state: CollectionState, player: int):
    return state.has("Flippers", player)


def oos_has_season(state: CollectionState, player: int, season: str):
    return state.has(SEASON_ITEMS[season], player)


def oos_has_summer(state: CollectionState, player: int):
    return state.has(SEASON_ITEMS["summer"], player)


def oos_has_spring(state: CollectionState, player: int):
    return state.has(SEASON_ITEMS["spring"], player)


def oos_has_winter(state: CollectionState, player: int):
    return state.has(SEASON_ITEMS["winter"], player)


def oos_has_autumn(state: CollectionState, player: int):
    return state.has(SEASON_ITEMS["autumn"], player)


def oos_has_flute(state: CollectionState, player: int):
    return state.has("Flute", player)


def oos_has_magnet_gloves(state: CollectionState, player: int):
    return state.has("Magnet Gloves", player)


def oos_has_ember_seeds(state: CollectionState, player: int):
    return state.has("Ember Seeds", player) or state.multiworld.worlds[player].default_seed == "Ember Seeds"


def oos_has_scent_seeds(state: CollectionState, player: int):
    return state.has("Scent Seeds", player) or state.multiworld.worlds[player].default_seed == "Scent Seeds"


def oos_has_pegasus_seeds(state: CollectionState, player: int):
    return state.has("Pegasus Seeds", player) or state.multiworld.worlds[player].default_seed == "Pegasus Seeds"


def oos_has_mystery_seeds(state: CollectionState, player: int):
    return state.has("Mystery Seeds", player) or state.multiworld.worlds[player].default_seed == "Mystery Seeds"


def oos_has_gale_seeds(state: CollectionState, player: int):
    return state.has("Gale Seeds", player) or state.multiworld.worlds[player].default_seed == "Gale Seeds"


def oos_has_small_keys(state: CollectionState, player: int, dungeon_id: int, amount: int = 1):
    return state.has(f"Small Key ({DUNGEON_NAMES[dungeon_id]})", player, amount)


def oos_has_boss_key(state: CollectionState, player: int, dungeon_id: int):
    return state.has(f"Boss Key ({DUNGEON_NAMES[dungeon_id]})", player)


# Options and generation predicates ###########################################

def oos_option_medium_logic(state: CollectionState, player: int):
    return state.multiworld.worlds[player].options.logic_difficulty in ["medium", "hard"]


def oos_option_hard_logic(state: CollectionState, player: int):
    return state.multiworld.worlds[player].options.logic_difficulty == "hard"


def oos_option_allow_warp_to_start(state: CollectionState, player: int):
    return state.multiworld.worlds[player].options.warp_to_start.value


def oos_option_shuffled_dungeons(state: CollectionState, player: int):
    return state.multiworld.worlds[player].options.shuffle_dungeons != "vanilla"


def oos_is_companion_ricky(state: CollectionState, player: int):
    return state.multiworld.worlds[player].options.animal_companion.value == "Ricky"


def oos_is_companion_moosh(state: CollectionState, player: int):
    return state.multiworld.worlds[player].options.animal_companion.value == "Moosh"


def oos_is_companion_dimitri(state: CollectionState, player: int):
    return state.multiworld.worlds[player].options.animal_companion.value == "Dimitri"


def oos_get_default_season(state: CollectionState, player: int, area_name: str):
    return state.multiworld.worlds[player].default_seasons[area_name]


def oos_can_remove_season(state: CollectionState, player: int, season: str):
    # Test if player has any other season than the one we want to remove
    return any(
        [state.has(item_name, player) for season_name, item_name in SEASON_ITEMS.items() if season_name != season])


def oos_has_essences(state: CollectionState, player: int, target_count: int):
    essence_count = [state.has(essence, player) for essence in ESSENCES].count(True)
    return essence_count >= target_count


def oos_has_needed_essences(state: CollectionState, player: int):
    return oos_has_essences(state, player, state.multiworld.worlds[player].options.required_essences)


def oos_can_reach_lost_woods_pedestal(state: CollectionState, player: int):
    world = state.multiworld.worlds[player]
    return all([
        any([
            world.options.lost_woods_item_sequence == "vanilla",
            all([
                oos_can_use_ember_seeds(state, player),
                state.has("Phonograph", player)
            ])
        ]),
        "winter" not in world.lost_woods_item_sequence or oos_has_winter(state, player),
        "spring" not in world.lost_woods_item_sequence or oos_has_spring(state, player),
        "summer" not in world.lost_woods_item_sequence or oos_has_summer(state, player),
        "autumn" not in world.lost_woods_item_sequence or oos_has_autumn(state, player)
    ])


# Various item predicates ###########################################

def oos_has_rupees(state: CollectionState, player: int, amount: int):
    if oos_can_farm_rupees(state, player):
        return True

    rupees = state.count("Rupees (1)", player)
    rupees += state.count("Rupees (5)", player) * 5
    rupees += state.count("Rupees (10)", player) * 10
    rupees += state.count("Rupees (20)", player) * 20
    rupees += state.count("Rupees (50)", player) * 50
    rupees += state.count("Rupees (100)", player) * 100

    if state.has("_reached_d2_rupee_room", player):
        rupees += 150
    if state.has("_reached_d6_rupee_room", player):
        rupees += 90

    # TODO: Count spendings by subtracting the price of all shop locations currently containing a progression item?

    return rupees >= amount


def oos_can_farm_rupees(state: CollectionState, player: int):
    # Farming rupees is not *that* hard by itself, but it's just really boring most of the time if you don't know how
    # to optimize it efficiently doing RNG manips and such, so we let it in the hard logic domain for now
    return oos_option_hard_logic(state, player) and oos_has_shovel(state, player)


def oos_can_date_rosa(state: CollectionState, player: int):
    return state.has("_reached_rosa", player) and state.has("Ribbon", player)


def oos_can_farm_ore(state: CollectionState, player: int):
    return any([
        oos_has_shovel(state, player),
        oos_has_sword(state, player),
        oos_has_magic_boomerang(state, player),
        state.has("_reached_subrosian_dance_hall", player)
    ])


def oos_can_trigger_far_switch(state: CollectionState, player: int):
    return any([
        oos_has_boomerang(state, player),
        oos_has_bombs(state, player),
        oos_has_slingshot(state, player),
        all([
            oos_option_hard_logic(state, player),
            oos_has_sword(state, player),
            state.has("Energy Ring", player)
        ])
        # TODO: Regular beams?
    ])


def oos_has_rod(state: CollectionState, player: int):
    return any([
        oos_has_winter(state, player),
        oos_has_summer(state, player),
        oos_has_spring(state, player),
        oos_has_autumn(state, player)
    ])


def oos_has_bombs(state: CollectionState, player: int):
    return any([
        all([
            state.has("Bombs (10)", player),
            # [shovel, bracelet, break flower, flute] TODO: Handling refill?
        ]),
        all([
            # With hard logic, player is expected to know they can get free bombs
            # from D2 moblin room even if they never had bombs before
            oos_option_hard_logic(state, player),
            state.has("_reached_d2_bracelet_room", player),
            any([
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player)
            ]),
        ])
    ])


def oos_can_summon_ricky(state: CollectionState, player: int):
    return oos_is_companion_ricky(state, player) and oos_has_flute(state, player)


def oos_can_summon_moosh(state: CollectionState, player: int):
    return oos_is_companion_moosh(state, player) and oos_has_flute(state, player)


def oos_can_summon_dimitri(state: CollectionState, player: int):
    return oos_is_companion_dimitri(state, player) and oos_has_flute(state, player)


# Jump-related predicates ###########################################

def oos_can_jump_1_wide_liquid(state: CollectionState, player: int, can_summon_companion: bool):
    return any([
        oos_has_feather(state, player),
        all([
            oos_option_medium_logic(state, player),
            can_summon_companion,
            oos_can_summon_ricky(state, player)
        ])
    ])


def oos_can_jump_2_wide_liquid(state: CollectionState, player: int):
    return any([
        oos_has_cape(state, player),
        all([
            oos_has_feather(state, player),
            oos_can_use_pegasus_seeds(state, player)
        ]),
        all([
            # Hard logic expects bomb jumps over 2-wide liquids
            oos_option_hard_logic(state, player),
            oos_has_feather(state, player),
            oos_has_bombs(state, player)
        ])
    ])


def oos_can_jump_3_wide_liquid(state: CollectionState, player: int):
    return any([
        oos_has_cape(state, player),
        all([
            oos_option_hard_logic(state, player),
            oos_has_feather(state, player),
            oos_can_use_pegasus_seeds(state, player),
            oos_has_bombs(state, player),
        ])
    ])


def oos_can_jump_4_wide_liquid(state: CollectionState, player: int):
    return all([
        oos_has_cape(state, player),
        any([
            oos_can_use_pegasus_seeds(state, player),
            all([
                # Hard logic expects player to be able to cape bomb-jump above 4-wide liquids
                oos_option_hard_logic(state, player),
                oos_has_bombs(state, player)
            ])
        ])
    ])


def oos_can_jump_5_wide_liquid(state: CollectionState, player: int):
    return all([
        oos_has_cape(state, player),
        oos_can_use_pegasus_seeds(state, player),
    ])


def oos_can_jump_6_wide_liquid(state: CollectionState, player: int):
    return all([
        oos_has_cape(state, player),
        oos_can_use_pegasus_seeds(state, player),
    ])


def oos_can_jump_1_wide_pit(state: CollectionState, player: int, can_summon_companion: bool):
    return any([
        oos_has_feather(state, player),
        all([
            can_summon_companion,
            any([
                oos_can_summon_moosh(state, player),
                oos_can_summon_ricky(state, player)
            ])
        ])
    ])


def oos_can_jump_2_wide_pit(state: CollectionState, player: int):
    return any([
        oos_has_cape(state, player),
        all([
            oos_has_feather(state, player),
            any([
                # Medium logic expects player to be able to jump above 2-wide pits without pegasus seeds
                oos_option_medium_logic(state, player),
                oos_can_use_pegasus_seeds(state, player)
            ])
        ])
    ])


def oos_can_jump_3_wide_pit(state: CollectionState, player: int):
    return any([
        oos_has_cape(state, player),
        all([
            oos_option_medium_logic(state, player),
            oos_has_feather(state, player),
            oos_can_use_pegasus_seeds(state, player),
        ])
    ])


def oos_can_jump_4_wide_pit(state: CollectionState, player: int):
    return all([
        oos_has_cape(state, player),
        any([
            oos_option_medium_logic(state, player),
            oos_can_use_pegasus_seeds(state, player),
        ])
    ])


def oos_can_jump_5_wide_pit(state: CollectionState, player: int):
    return all([
        oos_has_cape(state, player),
        oos_can_use_pegasus_seeds(state, player),
    ])


def oos_can_jump_6_wide_pit(state: CollectionState, player: int):
    return all([
        oos_has_cape(state, player),
        oos_can_use_pegasus_seeds(state, player),
    ])


# Seed-related predicates ###########################################

def oos_can_use_seeds(state: CollectionState, player: int):
    return oos_has_slingshot(state, player) or oos_has_satchel(state, player)


def oos_can_use_ember_seeds(state: CollectionState, player: int):
    return all([
        oos_can_use_seeds(state, player),
        any([
            oos_has_ember_seeds(state, player),
            all([
                # Medium logic expects the player to know they can use mystery seeds
                # to randomly get the ember effect
                oos_option_medium_logic(state, player),
                oos_has_mystery_seeds(state, player),
            ])
        ])
    ])


def oos_can_use_scent_seeds(state: CollectionState, player: int):
    return all([
        oos_can_use_seeds(state, player),
        oos_has_scent_seeds(state, player)
    ])


def oos_can_use_pegasus_seeds(state: CollectionState, player: int):
    return all([
        # Unlike other seeds, pegasus only have an interesting effect with the satchel
        oos_has_satchel(state, player),
        oos_has_pegasus_seeds(state, player)
    ])


def oos_can_warp_using_gale_seeds(state: CollectionState, player: int):
    return all([
        oos_has_satchel(state, player),
        oos_has_gale_seeds(state, player)
    ])


def oos_can_use_gale_seeds_offensively(state: CollectionState, player: int):
    return all([
        oos_has_gale_seeds(state, player),
        any([
            all([
                oos_option_medium_logic(state, player),
                oos_has_slingshot(state, player)
            ]),
            all([
                oos_option_hard_logic(state, player),
                oos_has_satchel(state, player)
            ]),
        ])
    ])


def oos_can_warp(state: CollectionState, player: int):
    return oos_can_warp_using_gale_seeds(state, player) or oos_option_allow_warp_to_start(state, player)


def oos_can_use_mystery_seeds(state: CollectionState, player: int):
    return all([
        oos_can_use_seeds(state, player),
        oos_has_mystery_seeds(state, player)
    ])


# Break / kill predicates ###########################################

def oos_can_break_bush(state: CollectionState, player: int, can_summon_companion: bool = False):
    return any([
        oos_has_sword(state, player),
        oos_has_magic_boomerang(state, player),
        oos_has_bracelet(state, player),
        (can_summon_companion and oos_has_flute(state, player)),
        all([
            # Consumables need at least medium logic, since they need a good knowledge of the game
            # not to be frustrating
            oos_option_medium_logic(state, player),
            any([
                oos_has_bombs(state, player),
                oos_can_use_ember_seeds(state, player),
                oos_can_use_gale_seeds_offensively(state, player),
            ])
        ]),
    ])


def oos_can_break_mushroom(state: CollectionState, player: int, can_use_companion: bool):
    return any([
        oos_has_bracelet(state, player),
        all([
            oos_option_medium_logic(state, player),
            any([
                oos_has_magic_boomerang(state, player),
                can_use_companion and oos_can_summon_dimitri(state, player)
            ])
        ]),
    ])


def oos_can_break_pot(state: CollectionState, player: int):
    return any([
        oos_has_bracelet(state, player),
        oos_has_noble_sword(state, player)
    ])


def oos_can_break_flowers(state: CollectionState, player: int, can_summon_companion: bool):
    return any([
        oos_has_sword(state, player),
        oos_has_magic_boomerang(state, player),
        oos_has_bombs(state, player),
        oos_can_use_ember_seeds(state, player),
        (oos_has_slingshot(state, player) and oos_has_gale_seeds(state, player)),
        (can_summon_companion and oos_has_flute(state, player))
    ])


def oos_can_break_crystal(state: CollectionState, player: int):
    return any([
        oos_has_sword(state, player),
        oos_has_bombs(state, player),
        oos_has_bracelet(state, player),
        # state.has("expert's ring", player)
    ])


def oos_can_harvest_tree(state: CollectionState, player: int, can_use_companion: bool):
    return all([
        oos_can_use_seeds(state, player),
        any([
            oos_has_sword(state, player),
            oos_has_fools_ore(state, player),
            oos_has_rod(state, player),
            oos_can_punch(state, player),
            all([
                can_use_companion,
                oos_option_medium_logic(state, player),
                oos_can_summon_dimitri(state, player)
            ])
        ])
    ])


def oos_can_push_enemy(state: CollectionState, player: int):
    return any([
        oos_has_rod(state, player),
        oos_has_shield(state, player)
    ])


def oos_can_kill_normal_enemy(state: CollectionState, player: int, pit_available: bool = False):
    # If a pit is avaiable nearby, it can be used to put the enemies inside using
    # items that are usually non-lethal
    if pit_available and oos_can_push_enemy(state, player):
        return True

    return any([
        oos_has_sword(state, player),
        oos_has_fools_ore(state, player),
        oos_can_kill_normal_using_satchel(state, player),
        oos_can_kill_normal_using_slingshot(state, player),
        oos_can_punch(state, player)
    ])


def oos_can_kill_normal_using_satchel(state: CollectionState, player: int):
    return all([
        oos_has_satchel(state, player),
        any([
            oos_has_ember_seeds(state, player),
            all([
                oos_option_medium_logic(state, player),
                any([
                    oos_has_scent_seeds(state, player),
                    oos_has_gale_seeds(state, player),
                ])
            ])
        ])
    ])


def oos_can_kill_normal_using_slingshot(state: CollectionState, player: int):
    return all([
        oos_has_slingshot(state, player),
        any([
            oos_has_ember_seeds(state, player),
            oos_has_scent_seeds(state, player),
            all([
                oos_option_medium_logic(state, player),
                oos_has_gale_seeds(state, player),
            ])
        ])
    ])


def oos_can_kill_armored_enemy(state: CollectionState, player: int):
    return any([
        oos_has_sword(state, player),
        oos_has_fools_ore(state, player),
        all([
            oos_has_scent_seeds(state, player),
            any([
                oos_has_slingshot(state, player),
                all([
                    oos_option_medium_logic(state, player),
                    oos_has_satchel(state, player)
                ])
            ])
        ]),
        oos_can_punch(state, player)
    ])


def oos_can_kill_stalfos(state: CollectionState, player: int):
    return any([
        oos_can_kill_normal_enemy(state, player),
        all([
            oos_option_medium_logic(state, player),
            oos_has_rod(state, player)
        ])
    ])


def oos_can_punch(state: CollectionState, player: int):
    # TODO: expert's ring OR fist ring, but there's a difference?
    return False


def oos_can_trigger_lever(state: CollectionState, player: int):
    return any([
        oos_can_trigger_lever_from_minecart(state, player),
        all([
            oos_option_medium_logic(state, player),
            oos_has_shovel(state, player)
        ])
    ])


def oos_can_trigger_lever_from_minecart(state: CollectionState, player: int):
    return any([
        oos_has_sword(state, player),
        oos_has_fools_ore(state, player),
        oos_has_boomerang(state, player),
        oos_has_rod(state, player),

        # TODO: Test that to ensure our understanding is right
        oos_can_use_scent_seeds(state, player),
        oos_can_use_mystery_seeds(state, player),
        oos_has_slingshot(state, player),  # any seed works using slingshot

        oos_can_punch(state, player)
    ])


def oos_can_kill_d2_hardhat(state: CollectionState, player: int):
    return any([
        oos_has_sword(state, player),
        oos_has_fools_ore(state, player),
        oos_has_boomerang(state, player),
        oos_can_push_enemy(state, player),
        all([
            oos_option_medium_logic(state, player),
            any([
                oos_has_slingshot(state, player),
                all([
                    oos_option_hard_logic(state, player),
                    oos_has_satchel(state, player),
                ])
            ]),
            any([
                oos_has_scent_seeds(state, player),
                oos_has_gale_seeds(state, player),
            ])
        ]),
        all([
            oos_option_hard_logic(state, player),
            oos_has_shovel(state, player)
        ])
    ])


def oos_can_kill_d2_far_moblin(state: CollectionState, player: int):
    return any([
        oos_has_sword(state, player),
        oos_has_fools_ore(state, player),
        oos_can_kill_normal_using_slingshot(state, player),
        all([
            oos_has_feather(state, player),
            oos_can_push_enemy(state, player),
        ]),
        all([
            oos_option_hard_logic(state, player),
            any([
                oos_can_use_ember_seeds(state, player),
                oos_can_punch(state, player)
            ])
        ])
    ])


def oos_can_flip_spiked_beetle(state: CollectionState, player: int):
    return any([
        oos_has_shield(state, player),
        oos_has_shovel(state, player)
    ])


def oos_can_kill_spiked_beetle(state: CollectionState, player: int):
    return any([
        all([  # Regular flip + kill
            oos_can_flip_spiked_beetle(state, player),
            any([
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player),
                oos_can_kill_normal_using_satchel(state, player),
                oos_can_kill_normal_using_slingshot(state, player)
            ])
        ]),
        all([  # Instant kill using Gale Seeds
            oos_has_gale_seeds(state, player),
            any([
                oos_has_slingshot(state, player),
                all([
                    oos_option_medium_logic(state, player),
                    oos_has_satchel(state, player)
                ])
            ])
        ])
    ])


def oos_can_kill_magunesu(state: CollectionState, player: int):
    return any([
        oos_has_sword(state, player),
        oos_has_fools_ore(state, player),
        # state.has("expert's ring", player)
    ])


# Action predicates ###########################################

def oos_can_remove_snow(state: CollectionState, player: int, can_summon_companion: bool):
    return oos_has_shovel(state, player) or (can_summon_companion and oos_has_flute(state, player))


def oos_can_swim(state: CollectionState, player: int, can_summon_companion: bool):
    return oos_has_flippers(state, player) or (can_summon_companion and oos_can_summon_dimitri(state, player))


def oos_can_remove_rockslide(state: CollectionState, player: int, can_summon_companion: bool):
    return oos_has_bombs(state, player) or (can_summon_companion and oos_can_summon_ricky(state, player))


# Season in region predicates ##########################################

def oos_season_in_spool_swamp(state: CollectionState, player: int, season: str):
    if oos_get_default_season(state, player, "SPOOL_SWAMP") == season:
        return True
    return oos_has_season(state, player, season) and state.has("_reached_spool_stump", player)


def oos_season_in_eyeglass_lake(state: CollectionState, player: int, season: str):
    if oos_get_default_season(state, player, "EYEGLASS_LAKE") == season:
        return True
    return oos_has_season(state, player, season) and state.has("_reached_eyeglass_stump", player)


def oos_season_in_temple_remains(state: CollectionState, player: int, season: str):
    if oos_get_default_season(state, player, "TEMPLE_REMAINS") == season:
        return True
    return oos_has_season(state, player, season) and state.has("_reached_remains_stump", player)


def oos_season_in_north_horon(state: CollectionState, player: int, season: str):
    if oos_get_default_season(state, player, "NORTH_HORON") == season:
        return True
    return oos_has_season(state, player, season) and state.has("_reached_ghastly_stump", player)


def oos_season_in_western_coast(state: CollectionState, player: int, season: str):
    if oos_get_default_season(state, player, "WESTERN_COAST") == season:
        return True
    return oos_has_season(state, player, season) and state.has("_reached_coast_stump", player)


def oos_season_in_eastern_suburbs(state: CollectionState, player: int, season: str):
    return (oos_get_default_season(state, player, "EASTERN_SUBURBS") == season
            or oos_has_season(state, player, season))


def oos_season_in_sunken_city(state: CollectionState, player: int, season: str):
    return (oos_get_default_season(state, player, "SUNKEN_CITY") == season
            or oos_has_season(state, player, season))


def oos_season_in_woods_of_winter(state: CollectionState, player: int, season: str):
    return (oos_get_default_season(state, player, "WOODS_OF_WINTER") == season
            or oos_has_season(state, player, season))


def oos_season_in_central_woods_of_winter(state: CollectionState, player: int, season: str):
    if oos_get_default_season(state, player, "WOODS_OF_WINTER") == season:
        return True
    return oos_has_season(state, player, season) and state.has("_reached_d2_stump", player)


def oos_season_in_mt_cucco(state: CollectionState, player: int, season: str):
    if oos_get_default_season(state, player, "SUNKEN_CITY") == season:
        return True
    return oos_has_season(state, player, season)


def oos_season_in_tarm_ruins(state: CollectionState, player: int, season: str):
    if oos_get_default_season(state, player, "TARM_RUINS") == season:
        return True
    return oos_has_season(state, player, season)
