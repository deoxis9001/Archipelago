{{generated_comment | indent("# ", True)}}

import typing
from BaseClasses import Location, Region

# Types of Check
CHECK_ELEMENT = 1
CHECK_CHEST = 2
CHECK_EVENT = 3
CHECK_SHOP = 4
CHECK_QUEST = 5

class AccessInformation(typing.NamedTuple):
    region: str
    cond: typing.List[typing.Tuple[str, int]] = []

class LocationData(typing.NamedTuple):
    name: str
    code: int
    access: typing.Dict[str, AccessInformation]
    clearance: str = "Default"
    kind: int = CHECK_CHEST

class CrossCodeLocation(Location):
    game: str = "CrossCode"
    data: LocationData
    access: AccessInformation

    def __init__(self, player: int, data: LocationData, mode, region_dict: dict[str, Region]):
        super(CrossCodeLocation, self).__init__(
            player,
            data.name,
            data.code,
            region_dict[data.access[mode].region]
        )

        self.data = data
        self.event = False
        self.access = data.access[mode]

# GENERATED CODE
# DO NOT TOUCH
locations_data = [
    {{locations_data | indent(4)}}
]
