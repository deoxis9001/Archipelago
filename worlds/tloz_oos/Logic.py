from BaseClasses import MultiWorld
from worlds.tloz_oos.data.logic.dungeons import (make_d0_logic, make_d1_logic, make_d2_logic, make_d3_logic,
                                                 make_d4_logic, make_d5_logic, make_d6_logic, make_d7_logic,
                                                 make_d8_logic)
from worlds.tloz_oos.data.logic.holodrum import make_holodrum_logic
from worlds.tloz_oos.data.logic.subrosia import make_subrosia_logic


def create_connections(multiworld: MultiWorld, player: int):
    dungeon_entrances = []
    for reg1, reg2 in multiworld.worlds[player].dungeon_entrances.items():
        dungeon_entrances.append([reg1, reg2, True, None])

    portal_connections = []
    for reg1, reg2 in multiworld.worlds[player].portal_connections.items():
        portal_connections.append([reg1, reg2, True, None])

    all_logic = [
        make_holodrum_logic(player),
        make_subrosia_logic(player),
        make_d0_logic(player),
        make_d1_logic(player),
        make_d2_logic(player),
        make_d3_logic(player),
        make_d4_logic(player),
        make_d5_logic(player),
        make_d6_logic(player),
        make_d7_logic(player),
        make_d8_logic(player),
        dungeon_entrances,
        portal_connections,
    ]

    # Create connections
    for logic_array in all_logic:
        for entrance_desc in logic_array:
            region_1 = multiworld.get_region(entrance_desc[0], player)
            region_2 = multiworld.get_region(entrance_desc[1], player)
            is_two_way = entrance_desc[2]
            rule = entrance_desc[3]

            region_1.connect(region_2, None, rule)
            if is_two_way:
                region_2.connect(region_1, None, rule)
