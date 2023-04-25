import typing

from BaseClasses import Location, MultiWorld

from .Names import LocationName

class WL4Location(Location):
    game: str = "Wario Land 4"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


# Locations correspond to their location in memory, offset from 0x801E328
#
# Each location type has its own table, which is then indexed with
# (passage * 4) + level
# 
# These location IDs are then prefixed with 0xEC, which is
# Wario Land 4's checksum.

def location_id(passage, level, checktype):
    return 0xEC00 | (checktype * 6 + passage) * 4 + level

box_location_table = {
    # Entry Passage
    LocationName.hall_of_hieroglyphs.jewels.ne: location_id(0, 0, 0),
    LocationName.hall_of_hieroglyphs.jewels.se: location_id(0, 0, 1),
    LocationName.hall_of_hieroglyphs.jewels.sw: location_id(0, 0, 2),
    LocationName.hall_of_hieroglyphs.jewels.nw: location_id(0, 0, 3),
    #
    # Emerald Passage
    LocationName.palm_tree_paradise.jewels.ne: location_id(1, 0, 0),
    LocationName.palm_tree_paradise.jewels.se: location_id(1, 0, 1),
    LocationName.palm_tree_paradise.jewels.sw: location_id(1, 0, 2),
    LocationName.palm_tree_paradise.jewels.nw: location_id(1, 0, 3),
    LocationName.palm_tree_paradise.cd_box:    location_id(1, 0, 4),
    #
    LocationName.wildflower_fields.jewels.ne: location_id(1, 1, 0),
    LocationName.wildflower_fields.jewels.se: location_id(1, 1, 1),
    LocationName.wildflower_fields.jewels.sw: location_id(1, 1, 2),
    LocationName.wildflower_fields.jewels.nw: location_id(1, 1, 3),
    LocationName.wildflower_fields.cd_box:    location_id(1, 1, 4),
    #
    LocationName.mystic_lake.jewels.ne: location_id(1, 2, 0),
    LocationName.mystic_lake.jewels.se: location_id(1, 2, 1),
    LocationName.mystic_lake.jewels.sw: location_id(1, 2, 2),
    LocationName.mystic_lake.jewels.nw: location_id(1, 2, 3),
    LocationName.mystic_lake.cd_box:    location_id(1, 2, 4),
    #
    LocationName.monsoon_jungle.jewels.ne: location_id(1, 3, 0),
    LocationName.monsoon_jungle.jewels.se: location_id(1, 3, 1),
    LocationName.monsoon_jungle.jewels.sw: location_id(1, 3, 2),
    LocationName.monsoon_jungle.jewels.nw: location_id(1, 3, 3),
    LocationName.monsoon_jungle.cd_box:    location_id(1, 3, 4),
    #
    # Ruby Passage
    LocationName.curious_factory.jewels.ne: location_id(2, 0, 0),
    LocationName.curious_factory.jewels.se: location_id(2, 0, 1),
    LocationName.curious_factory.jewels.sw: location_id(2, 0, 2),
    LocationName.curious_factory.jewels.nw: location_id(2, 0, 3),
    LocationName.curious_factory.cd_box:    location_id(2, 0, 4),
    #
    LocationName.toxic_landfill.jewels.ne: location_id(2, 1, 0),
    LocationName.toxic_landfill.jewels.se: location_id(2, 1, 1),
    LocationName.toxic_landfill.jewels.sw: location_id(2, 1, 2),
    LocationName.toxic_landfill.jewels.nw: location_id(2, 1, 3),
    LocationName.toxic_landfill.cd_box:    location_id(2, 1, 4),
    #
    LocationName.forty_below_fridge.jewels.ne: location_id(2, 2, 0),
    LocationName.forty_below_fridge.jewels.se: location_id(2, 2, 1),
    LocationName.forty_below_fridge.jewels.sw: location_id(2, 2, 2),
    LocationName.forty_below_fridge.jewels.nw: location_id(2, 2, 3),
    LocationName.forty_below_fridge.cd_box:    location_id(2, 2, 4),
    #
    LocationName.pinball_zone.jewels.ne: location_id(2, 3, 0),
    LocationName.pinball_zone.jewels.se: location_id(2, 3, 1),
    LocationName.pinball_zone.jewels.sw: location_id(2, 3, 2),
    LocationName.pinball_zone.jewels.nw: location_id(2, 3, 3),
    LocationName.pinball_zone.cd_box:    location_id(2, 3, 4),
    #
    # Topaz Passage
    LocationName.toy_block_tower.jewels.ne: location_id(3, 0, 0),
    LocationName.toy_block_tower.jewels.se: location_id(3, 0, 1),
    LocationName.toy_block_tower.jewels.sw: location_id(3, 0, 2),
    LocationName.toy_block_tower.jewels.nw: location_id(3, 0, 3),
    LocationName.toy_block_tower.cd_box:    location_id(3, 0, 4),
    #
    LocationName.big_board.jewels.ne: location_id(3, 1, 0),
    LocationName.big_board.jewels.se: location_id(3, 1, 1),
    LocationName.big_board.jewels.sw: location_id(3, 1, 2),
    LocationName.big_board.jewels.nw: location_id(3, 1, 3),
    LocationName.big_board.cd_box:    location_id(3, 1, 4),
    #
    LocationName.doodle_woods.jewels.ne: location_id(3, 2, 0),
    LocationName.doodle_woods.jewels.se: location_id(3, 2, 1),
    LocationName.doodle_woods.jewels.sw: location_id(3, 2, 2),
    LocationName.doodle_woods.jewels.nw: location_id(3, 2, 3),
    LocationName.doodle_woods.cd_box:    location_id(3, 2, 4),
    #
    LocationName.domino_row.jewels.ne: location_id(3, 3, 0),
    LocationName.domino_row.jewels.se: location_id(3, 3, 1),
    LocationName.domino_row.jewels.sw: location_id(3, 3, 2),
    LocationName.domino_row.jewels.nw: location_id(3, 3, 3),
    LocationName.domino_row.cd_box:    location_id(3, 3, 4),
    #
    # Sapphire Passage
    LocationName.crescent_moon_village.jewels.ne: location_id(4, 0, 0),
    LocationName.crescent_moon_village.jewels.se: location_id(4, 0, 1),
    LocationName.crescent_moon_village.jewels.sw: location_id(4, 0, 2),
    LocationName.crescent_moon_village.jewels.nw: location_id(4, 0, 3),
    LocationName.crescent_moon_village.cd_box:    location_id(4, 0, 4),
    #
    LocationName.arabian_night.jewels.ne: location_id(4, 1, 0),
    LocationName.arabian_night.jewels.se: location_id(4, 1, 1),
    LocationName.arabian_night.jewels.sw: location_id(4, 1, 2),
    LocationName.arabian_night.jewels.nw: location_id(4, 1, 3),
    LocationName.arabian_night.cd_box:    location_id(4, 1, 4),
    #
    LocationName.fiery_cavern.jewels.ne: location_id(4, 2, 0),
    LocationName.fiery_cavern.jewels.se: location_id(4, 2, 1),
    LocationName.fiery_cavern.jewels.sw: location_id(4, 2, 2),
    LocationName.fiery_cavern.jewels.nw: location_id(4, 2, 3),
    LocationName.fiery_cavern.cd_box:    location_id(4, 2, 4),
    #
    LocationName.hotel_horror.jewels.ne: location_id(4, 3, 0),
    LocationName.hotel_horror.jewels.se: location_id(4, 3, 1),
    LocationName.hotel_horror.jewels.sw: location_id(4, 3, 2),
    LocationName.hotel_horror.jewels.nw: location_id(4, 3, 3),
    LocationName.hotel_horror.cd_box:    location_id(4, 3, 4),
    #
    # Golden Pyramid
    LocationName.golden_passage.jewels.ne: location_id(5, 0, 0),
    LocationName.golden_passage.jewels.se: location_id(5, 0, 1),
    LocationName.golden_passage.jewels.sw: location_id(5, 0, 2),
    LocationName.golden_passage.jewels.nw: location_id(5, 0, 3),
}

boss_location_table = {
    LocationName.spoiled_rotten: None,
    LocationName.cractus: None,
    LocationName.cuckoo_condor: None,
    LocationName.aerodent: None,
    LocationName.catbat: None,
    LocationName.golden_diva: None,
}

s_hard_full_health_boxes = {
    LocationName.hall_of_hieroglyphs.fullhealth: location_id(0, 0, 5),
    LocationName.palm_tree_paradise.fullhealth:  location_id(1, 0, 5),
    LocationName.mystic_lake.fullhealth:         location_id(1, 2, 5),
    LocationName.monsoon_jungle.fullhealth:      location_id(1, 3, 5),
    LocationName.pinball_zone.fullhealth:        location_id(2, 3, 5),
}

hard_full_health_boxes = {
    **s_hard_full_health_boxes,
    LocationName.toy_block_tower.fullhealth: location_id(3, 0, 5),
    LocationName.big_board.fullhealth:       location_id(3, 1, 5),
}

normal_full_health_boxes = {
    **hard_full_health_boxes,
    LocationName.wildflower_fields.fullhealth: location_id(1, 1, 5),
    LocationName.toxic_landfill.fullhealth:    location_id(2, 1, 5),
}

gold_crowns = {
    LocationName.hall_of_hieroglyphs.crowns.gold:   location_id(0, 0, 6),
    LocationName.palm_tree_paradise.crowns.gold:    location_id(1, 0, 6),
    LocationName.wildflower_fields.crowns.gold:     location_id(1, 1, 6),
    LocationName.mystic_lake.crowns.gold:           location_id(1, 2, 6),
    LocationName.monsoon_jungle.crowns.gold:        location_id(1, 3, 6),
    LocationName.curious_factory.crowns.gold:       location_id(2, 0, 6),
    LocationName.toxic_landfill.crowns.gold:        location_id(2, 1, 6),
    LocationName.forty_below_fridge.crowns.gold:    location_id(2, 2, 6),
    LocationName.pinball_zone.crowns.gold:          location_id(2, 3, 6),
    LocationName.toy_block_tower.crowns.gold:       location_id(3, 0, 6),
    LocationName.big_board.crowns.gold:             location_id(3, 1, 6),
    LocationName.doodle_woods.crowns.gold:          location_id(3, 2, 6),
    LocationName.domino_row.crowns.gold:            location_id(3, 3, 6),
    LocationName.crescent_moon_village.crowns.gold: location_id(4, 0, 6),
    LocationName.arabian_night.crowns.gold:         location_id(4, 1, 6),
    LocationName.fiery_cavern.crowns.gold:          location_id(4, 2, 6),
    LocationName.hotel_horror.crowns.gold:          location_id(4, 3, 6),
    LocationName.golden_passage.crowns.gold:        location_id(5, 0, 6),
}

silver_crowns = {
    LocationName.hall_of_hieroglyphs.crowns.silver:   location_id(0, 0, 7),
    LocationName.palm_tree_paradise.crowns.silver:    location_id(1, 0, 7),
    LocationName.wildflower_fields.crowns.silver:     location_id(1, 1, 7),
    LocationName.mystic_lake.crowns.silver:           location_id(1, 2, 7),
    LocationName.monsoon_jungle.crowns.silver:        location_id(1, 3, 7),
    LocationName.curious_factory.crowns.silver:       location_id(2, 0, 7),
    LocationName.toxic_landfill.crowns.silver:        location_id(2, 1, 7),
    LocationName.forty_below_fridge.crowns.silver:    location_id(2, 2, 7),
    LocationName.pinball_zone.crowns.silver:          location_id(2, 3, 7),
    LocationName.toy_block_tower.crowns.silver:       location_id(3, 0, 7),
    LocationName.big_board.crowns.silver:             location_id(3, 1, 7),
    LocationName.doodle_woods.crowns.silver:          location_id(3, 2, 7),
    LocationName.domino_row.crowns.silver:            location_id(3, 3, 7),
    LocationName.crescent_moon_village.crowns.silver: location_id(4, 0, 7),
    LocationName.arabian_night.crowns.silver:         location_id(4, 1, 7),
    LocationName.fiery_cavern.crowns.silver:          location_id(4, 2, 7),
    LocationName.hotel_horror.crowns.silver:          location_id(4, 3, 7),
    LocationName.golden_passage.crowns.silver:        location_id(5, 0, 7),
}

bronze_crowns = {
    LocationName.hall_of_hieroglyphs.crowns.bronze:   location_id(0, 0, 8),
    LocationName.palm_tree_paradise.crowns.bronze:    location_id(1, 0, 8),
    LocationName.wildflower_fields.crowns.bronze:     location_id(1, 1, 8),
    LocationName.mystic_lake.crowns.bronze:           location_id(1, 2, 8),
    LocationName.monsoon_jungle.crowns.bronze:        location_id(1, 3, 8),
    LocationName.curious_factory.crowns.bronze:       location_id(2, 0, 8),
    LocationName.toxic_landfill.crowns.bronze:        location_id(2, 1, 8),
    LocationName.forty_below_fridge.crowns.bronze:    location_id(2, 2, 8),
    LocationName.pinball_zone.crowns.bronze:          location_id(2, 3, 8),
    LocationName.toy_block_tower.crowns.bronze:       location_id(3, 0, 8),
    LocationName.big_board.crowns.bronze:             location_id(3, 1, 8),
    LocationName.doodle_woods.crowns.bronze:          location_id(3, 2, 8),
    LocationName.domino_row.crowns.bronze:            location_id(3, 3, 8),
    LocationName.crescent_moon_village.crowns.bronze: location_id(4, 0, 8),
    LocationName.arabian_night.crowns.bronze:         location_id(4, 1, 8),
    LocationName.fiery_cavern.crowns.bronze:          location_id(4, 2, 8),
    LocationName.hotel_horror.crowns.bronze:          location_id(4, 3, 8),
    LocationName.golden_passage.crowns.bronze:        location_id(5, 0, 8),
}

all_locations = {
    **box_location_table,
    **boss_location_table,
    **normal_full_health_boxes,
    **gold_crowns,
    **silver_crowns,
    **bronze_crowns,
}

location_table = {}


def setup_locations(world: MultiWorld, player: int):
    location_table = {
        **box_location_table,
        **boss_location_table
    }

    if world.difficulty[player].value == 0:
        location_table.update({**normal_full_health_boxes})
    elif world.difficulty[player].value == 1:
        location_table.update({**hard_full_health_boxes})
    else:
        location_table.update({**s_hard_full_health_boxes})

    if world.crown_shuffle[player].value == 1:
        location_table.update({**gold_crowns})
    elif world.crown_shuffle[player].value == 2:
        location_table.update({**silver_crowns})
    elif world.crown_shuffle[player].value == 3:
        location_table.update({**bronze_crowns})
    elif world.crown_shuffle[player].value == 4:
        location_table.update({**gold_crowns, **silver_crowns, **bronze_crowns})
        
    return location_table


lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in all_locations.items()}
