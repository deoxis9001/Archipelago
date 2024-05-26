from BaseClasses import CollectionState
from worlds.tloz_tmc.data.Constants import DUNGEON_NAMES

#options
def tmc_options_bomb_helper(state: CollectionState, player: int):
    if self.options.sword_availability == "yes"
        return state.has("BombBag", player)
    elif self.options.sword_availability == "boss"
        return state.has("BombBag", player, 2)
    else
        return 0
 
 
# logic
def tmc_has_sword(state: CollectionState, player: int):
    return any([
        state.has("SmithSword", player),
        state.has("GreenSword", player),
        state.has("RedSword", player),
        state.has("BlueSword", player),
        state.has("FourSword", player)
    ])

def tmc_has_white_sword(state: CollectionState, player: int):
    return any([
        state.has("GreenSword", player),
        state.has("RedSword", player),
        state.has("BlueSword", player),
        state.has("FourSword", player)
    ])

def tmc_has_spin(state: CollectionState, player: int):
    return state.has("SpinAttack", player)

def tmc_can_split2(state: CollectionState, player: int):
    return all([
        state.has("RedSword", player),
        tmc_has_spin(state, player)
    ])

def tmc_can_split3(state: CollectionState, player: int):
    return all([
        state.has("BlueSword", player),
        tmc_has_spin(state, player)
    ])

def tmc_can_split4(state: CollectionState, player: int):
    return all([
        state.has("FourSword", player),
        tmc_has_spin(state, player)
    ])

def tmc_has_bottle(state: CollectionState, player: int):
    return state.has("SpinAttack", player)

def tmc_has_bow(state: CollectionState, player: int):
    return any([
        state.has("Bow", player),
        state.has("LightArrow", player)
    ])

def tmc_has_light_arrow(state: CollectionState, player: int):
    return state.has("LightArrow", player)

def tmc_has_boomerang(state: CollectionState, player: int):
    return any([
        state.has("Boomerang", player),
        state.has("MagicBoomerang", player)
    ])

def tmc_has_magic_boomerang(state: CollectionState, player: int):
    return state.has("MagicBoomerang", player)
    
def tmc_has_shield(state: CollectionState, player: int):
    return any([
        state.has("Boomerang", player),
        state.has("MagicBoomerang", player)
    ])
    
def tmc_sword_beam(state: CollectionState, player: int):
    return all([
        state.has("SwordBeam", player),
        tmc_has_bottle(state,player)
    ])
    
def tmc_has_beam(state: CollectionState, player: int):
    return all([
        tmc_has_sword(state, player),
        any([
            tmc_sword_beam(state, player),
            state.has("PerilBeam", player)
        ])
    ])
        
def tmc_can_down_thrust(state: CollectionState, player: int):
    return all([
        tmc_has_sword(state, player),
        any([
            state.has("DownThrust", player),
            state.has("RocsCape", player)
        ])
    ])
    