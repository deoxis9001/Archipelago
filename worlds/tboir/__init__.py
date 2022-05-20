import string
from .Items import TheBindingOfIsaacRebirthItem, item_table
from .Locations import location_table, TheBindingOfIsaacRebirthLocation, base_location_table
from .Rules import set_rules

from BaseClasses import Region, Entrance, Item, MultiWorld, Tutorial
from .Options import tobir_options
from ..AutoWorld import World, WebWorld

client_version = 1


class TheBindingOfIsaacRebirthWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the The Binding Of Isaac Rebirth integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Ijwu"]
    )]


class TheBindingOfIsaacRebirthWorld(World):
    """
    todo
    """
    game: str = "The Binding of Isaac Rebirth"
    options = tobir_options
    topology_present = False

    item_name_to_id = item_table
    location_name_to_id = location_table

    data_version = 3
    forced_auto_forfeit = True
    web = TheBindingOfIsaacRebirthWeb()

    def generate_basic(self):
        item_wights_table = {
            "Treasure Room Item": 100,
            "Shop Item": 100,
            "Boss Item": 100,
            "Devil Deal Item": 100,
            "Angle Deal Item": 100,
            "Secret Room Item": 100,
            "Library Item": 100,
            "Curse Room Item": 100,
            "Planetarium Item": 100,
            # item (expirimental)
            "Shell Game Item": 100,
            "Golden Chest Item": 100,
            "Red Chest Item": 100,
            "Beggar Item": 100,
            "Demon Baggar Item": 100,
            "Key Master Item": 100,
            "Battery Bum Item": 100,
            "Mom's Chest Item": 100,
            "Greed Treasure Room Item": 100,
            "Greed Boss Item": 100,
            "Greed Shop Item": 100,
            "Greed Devil Deal Item": 100,
            "Greed Angel Deal Item": 100,
            "Greed Curse Room Item": 100,
            "Greed Secret Room Item": 100,
            "Crane Game Item": 100,
            "Ultra Secret Room Item": 100,
            "Bomb Bum Item": 100,
            "Old Chest Item": 100,
            "Baby Shop Item": 100,
            "Wooden Chest Item": 100,
            "Rotten Beggar Item": 100,
            # other
            "Random Pickup": 100,
            "Random Heart": 100,
            "Random Coin": 100,
            "Random Bomb": 100,
            "Random Key": 100,
            "Random Card": 100,
            "Random Pill": 100,
            "Random Chest": 100,
            "Random Trinket": 100,
        }

        # Generate item pool
        itempool = []

        # Fill remaining items with randomly generated junk
        itempool += self.world.random.choices(list(item_wights_table.keys()), weights=list(item_wights_table.values()),
                                              k=self.world.total_locations[self.player])

        # Convert itempool into real items
        itempool = list(map(lambda name: self.create_item(name), itempool))

        self.world.itempool += itempool

    def set_rules(self):
        set_rules(self.world, self.player)

    def create_regions(self):
        create_regions(self.world, self.player)
        create_events(self.world, self.player, int(self.world.total_locations[self.player]))

    def fill_slot_data(self):
        return {
            "itemPickupStep": self.world.item_pickup_step[self.player].value,
            "seed": "".join(self.world.slot_seeds[self.player].choice(string.digits) for i in range(16)),
            "totalLocations": self.world.total_locations[self.player].value,
            "requiredLocations": self.world.required_locations[self.player].value,
            "goal": self.world.goal[self.player].value
        }

    def create_item(self, name: str) -> Item:
        item_id = item_table[name]
        item = TheBindingOfIsaacRebirthItem(name, True, item_id, self.player)
        return item


def create_events(world: MultiWorld, player: int, total_locations: int):
    num_of_events = total_locations // 25
    if total_locations / 25 == num_of_events:
        num_of_events -= 1
    for i in range(num_of_events):
        event_loc = TheBindingOfIsaacRebirthLocation(player, f"Pickup{(i + 1) * 25}", None,
                                                     world.get_region('In Run', player))
        event_loc.place_locked_item(TheBindingOfIsaacRebirthItem(f"Pickup{(i + 1) * 25}", True, None, player))
        event_loc.access_rule(lambda state, i=i: state.can_reach(f"ItemPickup{((i + 1) * 25) - 1}", player))
        world.get_region('In Run', player).locations.append(event_loc)


# generate locations based on player setting
def create_regions(world, player: int):
    world.regions += [
        create_region(world, player, 'Menu', None, ['New Run']),
        create_region(world, player, 'In Run',
                      [location for location in base_location_table] +
                      [f"ItemPickup{i}" for i in range(1, 1 + world.total_locations[player])])
    ]

    world.get_entrance("New Run", player).connect(world.get_region("In Run", player))
    world.get_location("Victory", player).place_locked_item(TheBindingOfIsaacRebirthItem("Victory", True, None, player))


def create_region(world: MultiWorld, player: int, name: str, locations=None, exits=None):
    ret = Region(name, None, name, player)
    ret.world = world
    if locations:
        for location in locations:
            loc_id = location_table[location]
            location = TheBindingOfIsaacRebirthLocation(player, location, loc_id, ret)
            ret.locations.append(location)
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, exit, ret))

    return ret
