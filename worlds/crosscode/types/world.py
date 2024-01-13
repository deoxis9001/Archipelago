from dataclasses import dataclass, field
import typing

from .items import ItemData
from .locations import AccessInfo, LocationData
from .regions import RegionsData

@dataclass
class WorldData:
    region_packs: dict[str, RegionsData]
    modes: list[str] = field(init=False)

    locations_data: dict[str, tuple[LocationData, AccessInfo]]
    events_data: dict[str, tuple[LocationData, AccessInfo]]
    num_needed_items: dict[str, int]

    items_dict: dict[tuple[str, int], tuple[ItemData, dict[str, int]]]

    def __post_init__(self):
        self.modes = list(self.region_packs.keys())
