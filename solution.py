from pprint import pprint


def get_existing_map_or_create(target_map: dict, key: str):
    existing_map = target_map.get(key, {})
    target_map[key] = existing_map
    return existing_map


def insert_simple_type(schema_type: str, target_map: dict):
    target_map[schema_type] = True


def insert_list(target_map: dict, list_value: list):
    existing_map = get_existing_map_or_create(target_map, "list")
    if list_value:
        # since lists can only contain values of one type, pick the first one
        first_value = list_value[0]
        insert_any(target_map=existing_map, value=first_value)


def insert_record(target_map: dict, record_value: dict):
    existing_map = get_existing_map_or_create(target_map, "record")
    insert_record_values(existing_map, record_value)


def insert_record_values(target_map: dict, record: dict):
    for (key, value) in record.items():
        existing_map = get_existing_map_or_create(target_map, key)
        insert_any(target_map=existing_map, value=value)


def insert_any(target_map: dict, value: int or str or list or dict):
    if isinstance(value, int):
        insert_simple_type("int", target_map)
    elif isinstance(value, str):
        insert_simple_type("str", target_map)
    elif isinstance(value, list):
        insert_list(target_map, value)
    elif isinstance(value, dict):
        insert_record(target_map, value)


def solution(input_list: list):
    result = {}
    for record in input_list:
        insert_record_values(result, record)
    pprint(result)


if __name__ == '__main__':
    records = [
        {"a": 1, "b": 2},
        {"a": [4]},
        {"a": ["hi"]},
        {"a": {"b": "hello"}, "b": 1}
    ]
    solution(records)
