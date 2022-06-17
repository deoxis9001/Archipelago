import string
from .Items import TheBindingOfIsaacRebirthItem, item_table, default_weights, default_junk_items_weights, \
    default_trap_items_weights
from .Locations import location_table, TheBindingOfIsaacRebirthLocation, base_location_table
from .Rules import set_rules

from BaseClasses import Region, Entrance, Item, MultiWorld, Tutorial, ItemClassification
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

    item_name_to_id = {name: data.id for name, data in item_table.items()}
    location_name_to_id = location_table

    data_version = 3
    web = TheBindingOfIsaacRebirthWeb()

    def generate_basic(self):

        # Generate item pool
        itempool = []

        junk_item_count = round(
            self.world.total_locations[self.player] * (self.world.junk_percentage[self.player] / 100))
        collectable_item_count = self.world.total_locations[self.player] - junk_item_count

        if self.world.item_weights[self.player] == 1:
            item_weights = {name: val for name, val in self.world.custom_item_weights[self.player].value.items()}
        else:
            item_weights = default_weights

        # Fill non-junk items
        itempool += self.world.random.choices(list(item_weights.keys()), weights=list(item_weights.values()),
                                              k=collectable_item_count)

        trap_item_count = round(junk_item_count * (self.world.trap_percentage[self.player] / 100))
        junk_item_count = junk_item_count - trap_item_count

        trap_weights = {name: val for name, val in self.world.trap_item_weights[self.player].value.items()}
        junk_weights = {name: val for name, val in self.world.custom_junk_item_weights[self.player].value.items()}

        # Fill traps
        itempool += self.world.random.choices(list(trap_weights.keys()), weights=list(trap_weights.values()),
                                              k=trap_item_count)

        # Fill remaining items with randomly generated junk
        itempool += self.world.random.choices(list(junk_weights.keys()), weights=list(junk_weights.values()),
                                              k=junk_item_count)

        assert len(itempool) == self.world.total_locations[self.player]

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
            "seed": "".join(self.world.slot_seeds[self.player].choice(string.digits) for _ in range(16)),
            "totalLocations": self.world.total_locations[self.player].value,
            "requiredLocations": self.world.required_locations[self.player].value,
            "goal": self.world.goal[self.player].value,
            "additionalBossRewards": self.world.additional_boss_rewards[self.player].value,
            "deathLink": self.world.death_link[self.player].value,
            "teleportTrapCanError": self.world.teleport_trap_can_error[self.player].value
        }

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = TheBindingOfIsaacRebirthItem(name, item_data.classification, item_data.id, self.player)
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
