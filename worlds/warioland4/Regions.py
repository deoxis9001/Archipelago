import typing

from BaseClasses import MultiWorld, Region, Entrance

from .Locations import WarioLand4Location, all_locations
from .Names import LocationName, ItemName, RegionName


def create_regions(world: MultiWorld, player: int):
    menu_region = create_region(world, player, "Menu")
    map_region = create_region(world, player, RegionName.map)

    entry_passage = create_region(world, player, RegionName.entry_passage)
    hall_of_hieroglyphs = create_region(
        world,
        player,
        RegionName.hall_of_hieroglyphs,
        [*LocationName.hall_of_hieroglyphs.jewels, LocationName.hall_of_hieroglyphs.fullhealth],
    )
    spoiled_rotten = create_region(
        world,
        player,
        RegionName.spoiled_rotten,
        (LocationName.spoiled_rotten,),
    )

    emerald_passage = create_region(world, player, RegionName.emerald_passage)
    palm_tree_paradise = create_region(
        world,
        player,
        RegionName.palm_tree_paradise,
        LocationName.palm_tree_paradise.default_locations(),
    )
    wildflower_fields = create_region(
        world,
        player,
        RegionName.wildflower_fields,
        LocationName.wildflower_fields.default_locations(),
    )
    mystic_lake = create_region(
        world,
        player,
        RegionName.mystic_lake,
        LocationName.mystic_lake.default_locations(),
    )
    monsoon_jungle = create_region(
        world,
        player,
        RegionName.monsoon_jungle,
        LocationName.monsoon_jungle.default_locations(),
    )
    cractus = create_region(
        world,
        player,
        RegionName.cractus,
        (LocationName.cractus,),
    )

    ruby_passage = create_region(world, player, RegionName.ruby_passage)
    curious_factory = create_region(
        world,
        player,
        RegionName.curious_factory,
        LocationName.curious_factory.default_locations(),
    )
    toxic_landfill = create_region(
        world,
        player,
        RegionName.toxic_landfill,
        LocationName.toxic_landfill.default_locations(),
    )
    forty_below_fridge = create_region(
        world,
        player,
        RegionName.forty_below_fridge,
        LocationName.forty_below_fridge.default_locations(),
    )
    pinball_zone = create_region(
        world,
        player,
        RegionName.pinball_zone,
        LocationName.pinball_zone.default_locations(),
    )
    cuckoo_condor = create_region(
        world,
        player,
        RegionName.cuckoo_condor,
        (LocationName.cuckoo_condor,),
    )

    topaz_passage = create_region(world, player, RegionName.topaz_passage)
    toy_block_tower = create_region(
        world,
        player,
        RegionName.toy_block_tower,
        LocationName.toy_block_tower.default_locations(),
    )
    big_board = create_region(
        world,
        player,
        RegionName.big_board,
        LocationName.big_board.default_locations(),
    )
    doodle_woods = create_region(
        world,
        player,
        RegionName.doodle_woods,
        LocationName.doodle_woods.default_locations(),
    )
    domino_row = create_region(
        world,
        player,
        RegionName.domino_row,
        LocationName.domino_row.default_locations(),
    )
    aerodent = create_region(
        world,
        player,
        RegionName.aerodent,
        (LocationName.aerodent,),
    )

    sapphire_passage = create_region(world, player, RegionName.sapphire_passage)
    crescent_moon_village = create_region(
        world,
        player,
        RegionName.crescent_moon_village,
        LocationName.crescent_moon_village.default_locations(),
    )
    arabian_night = create_region(
        world,
        player,
        RegionName.arabian_night,
        LocationName.arabian_night.default_locations(),
    )
    fiery_cavern = create_region(
        world,
        player,
        RegionName.fiery_cavern,
        LocationName.fiery_cavern.default_locations(),
    )
    hotel_horror = create_region(
        world,
        player,
        RegionName.hotel_horror,
        LocationName.hotel_horror.default_locations(),
    )
    catbat = create_region(
        world,
        player,
        RegionName.catbat,
        (LocationName.catbat,),
    )

    golden_pyramid = create_region(world, player, RegionName.golden_pyramid)
    golden_passage = create_region(
        world,
        player,
        RegionName.golden_passage,
        LocationName.golden_passage.jewels,
    )
    golden_diva = create_region(
        world,
        player,
        RegionName.golden_diva,
        (LocationName.golden_diva,),
    )

    world.regions += [
        menu_region,
        map_region,
        entry_passage,
        hall_of_hieroglyphs,
        spoiled_rotten,
        emerald_passage,
        palm_tree_paradise,
        wildflower_fields,
        mystic_lake,
        monsoon_jungle,
        cractus,
        ruby_passage,
        curious_factory,
        toxic_landfill,
        forty_below_fridge,
        pinball_zone,
        cuckoo_condor,
        topaz_passage,
        toy_block_tower,
        big_board,
        doodle_woods,
        domino_row,
        aerodent,
        sapphire_passage,
        crescent_moon_village,
        arabian_night,
        fiery_cavern,
        hotel_horror,
        catbat,
        golden_pyramid,
        golden_passage,
        golden_diva,
    ]


def connect_regions(world, player):
    names: typing.Dict[str, int] = {}

    connect(world, player, names, "Menu", RegionName.entry_passage)
    connect(world, player, names, RegionName.entry_passage, RegionName.hall_of_hieroglyphs)
    connect(world, player, names, RegionName.hall_of_hieroglyphs, RegionName.spoiled_rotten,
        lambda state: all(state.has(piece, player) for piece in ItemName.entry_passage_jewel))
    connect(world, player, names, RegionName.spoiled_rotten, RegionName.map)

    connect(world, player, names, RegionName.map, RegionName.emerald_passage)
    connect(world, player, names, RegionName.emerald_passage, RegionName.palm_tree_paradise)
    connect(world, player, names, RegionName.palm_tree_paradise, RegionName.wildflower_fields)
    connect(world, player, names, RegionName.wildflower_fields, RegionName.mystic_lake)
    connect(world, player, names, RegionName.mystic_lake, RegionName.monsoon_jungle)
    connect(world, player, names, RegionName.monsoon_jungle, RegionName.cractus,
        lambda state: all(state.has(piece, player, 4) for piece in ItemName.emerald_passage_jewel))

    connect(world, player, names, RegionName.map, RegionName.ruby_passage)
    connect(world, player, names, RegionName.ruby_passage, RegionName.curious_factory)
    connect(world, player, names, RegionName.curious_factory, RegionName.toxic_landfill)
    connect(world, player, names, RegionName.toxic_landfill, RegionName.forty_below_fridge)
    connect(world, player, names, RegionName.forty_below_fridge, RegionName.pinball_zone)
    connect(world, player, names, RegionName.pinball_zone, RegionName.cuckoo_condor,
        lambda state: all(state.has(piece, player, 4) for piece in ItemName.ruby_passage_jewel))

    connect(world, player, names, RegionName.map, RegionName.topaz_passage)
    connect(world, player, names, RegionName.topaz_passage, RegionName.toy_block_tower)
    connect(world, player, names, RegionName.toy_block_tower, RegionName.big_board)
    connect(world, player, names, RegionName.big_board, RegionName.doodle_woods)
    connect(world, player, names, RegionName.doodle_woods, RegionName.domino_row)
    connect(world, player, names, RegionName.domino_row, RegionName.aerodent,
        lambda state: all(state.has(piece, player, 4) for piece in ItemName.topaz_passage_jewel))

    connect(world, player, names, RegionName.map, RegionName.sapphire_passage)
    connect(world, player, names, RegionName.sapphire_passage, RegionName.crescent_moon_village)
    connect(world, player, names, RegionName.crescent_moon_village, RegionName.arabian_night)
    connect(world, player, names, RegionName.arabian_night, RegionName.fiery_cavern)
    connect(world, player, names, RegionName.fiery_cavern, RegionName.hotel_horror)
    connect(world, player, names, RegionName.hotel_horror, RegionName.catbat,
        lambda state: all(state.has(piece, player, 4) for piece in ItemName.sapphire_passage_jewel))

    connect(world, player, names, RegionName.map, RegionName.golden_pyramid,
        lambda state: (state.has(ItemName.defeated_boss, player, 5)))
    connect(world, player, names, RegionName.golden_pyramid, RegionName.golden_passage)
    connect(world, player, names, RegionName.golden_passage, RegionName.golden_diva,
        lambda state: all(state.has(piece, player) for piece in ItemName.golden_pyramid_jewel))


def create_region(
    world: MultiWorld, player: int, name: str, locations: typing.Sequence[str] = ()
):
    region = Region(name, player, world)
    for location in locations:
        id = all_locations[location]
        region.locations.append(WarioLand4Location(player, location, id, region))
    return region


def connect(
    world: MultiWorld,
    player: int,
    used_names: typing.Dict[str, int],
    source: str,
    target: str,
    rule: typing.Optional[typing.Callable] = None,
):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

    if target not in used_names:
        used_names[target] = 1
        name = target
    else:
        used_names[target] += 1
        name = target + (' ' * used_names[target])
    
    connection = Entrance(player, name, source_region)

    if rule:
        connection.access_rule = rule
    
    source_region.exits.append(connection)
    connection.connect(target_region)
