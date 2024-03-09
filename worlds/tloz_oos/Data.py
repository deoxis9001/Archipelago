from typing import Dict, List
from BaseClasses import Item
from .data import BASE_LOCATION_ID, LOCATIONS_DATA, BASE_ITEM_ID, ITEMS_DATA


def build_location_name_to_id_dict() -> Dict[str, int]:
    location_name_to_id: Dict[str, int] = {}
    current_index = BASE_LOCATION_ID
    for loc_name in LOCATIONS_DATA:
        location_name_to_id[loc_name] = current_index
        current_index += 1
    return location_name_to_id


def build_item_name_to_id_dict() -> Dict[str, int]:
    item_name_to_id: Dict[str, int] = {}
    current_index = BASE_ITEM_ID
    for item_name in ITEMS_DATA.keys():
        item_name_to_id[item_name] = current_index
        current_index += 1
    return item_name_to_id


def build_item_id_to_name_dict() -> Dict[int, str]:
    item_id_to_name: Dict[int, str] = {}
    current_index = BASE_ITEM_ID
    for item_name in ITEMS_DATA.keys():
        item_id_to_name[current_index] = item_name
        current_index += 1
    return item_id_to_name


def find_patcher_name_for_location(pretty_name: str):
    for loc_name, data in LOCATIONS_DATA.items():
        if loc_name == pretty_name:
            return data["patcher_name"] if "patcher_name" in data else ""
    raise "Could not find patcher name for unknown location '" + pretty_name + "'"
