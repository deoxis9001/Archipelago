import string
from .Items import TheBindingOfIsaacRebirthItem, item_table
from .Locations import location_table, TheBindingOfIsaacRebirthLocation, base_location_table
from .Rules import set_rules

from BaseClasses import Region, Entrance, Item, MultiWorld, Tutorial
from .Options import tobir_options
from ..AutoWorld import World, WebWorld



class TheBindingOfIsaacRebirthWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the The Binding Of Isaac Rebirth integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Cyb3R"]
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
    web = TheBindingOfIsaacRebirthWeb()

    def generate_basic(self):
        item_wights_table = {
            # item (major)
            "Treasure Room Item": 100,
            "Shop Item": 100,
            "Boss Item": 80,
            "Devil Deal Item": 60,
            "Angle Deal Item": 60,
            "Secret Room Item": 80,
            "Library Item": 40,
            "Curse Room Item": 40,
            "Planetarium Item": 20,
            # item (expirimental)
            "Shell Game Item": 0,
            "Golden Chest Item": 60,
            "Red Chest Item": 60,
            "Beggar Item": 0,
            "Demon Baggar Item": 0,
            "Key Master Item": 0,
            "Battery Bum Item": 0,
            "Mom's Chest Item": 0,
            "Greed Treasure Room Item": 0,
            "Greed Boss Item": 0,
            "Greed Shop Item": 0,
            "Greed Devil Deal Item": 0,
            "Greed Angel Deal Item": 0,
            "Greed Curse Room Item": 0,
            "Greed Secret Room Item": 0,
            "Crane Game Item": 0,
            "Ultra Secret Room Item": 0,
            "Bomb Bum Item": 0,
            "Old Chest Item": 0,
            "Baby Shop Item": 0,
            "Wooden Chest Item": 0,
            "Rotten Beggar Item": 0,
            # other junk
            "Random Pickup": 0,
            "Random Heart": 100,
            "Random Coin": 100,
            "Random Bomb": 100,
            "Random Key": 100,
            "Random Card": 90,
            "Random Pill": 90,
            "Random Chest": 85,
            "Random Trinket": 80,
            # Traps
            "Troll Bomb Trap": 50,
            "Teleport Trap": 50,
            "Retro Vision Trap": 50,
            "Curse Trap": 50,
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
            "goal": self.world.goal[self.player].value,
            "additionalBossRewards": self.world.additional_boss_rewards[self.player].value,
            "deathLink": self.world.death_link[self.player].value
        }

    def create_item(self, name: str) -> Item:
        item_id = item_table[name]
        item = TheBindingOfIsaacRebirthItem(name, item_id not in range(78031, 78040) and
                                            item_id not in range(78772, 78775), item_id, self.player)
        if item_id in range(78772, 78775):
            item.trap = True
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
