import json

def dump_to_file(path: str, data):
    with open(path, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_json_file(path: str):
    with open(path, 'r', encoding="utf-8") as f:
        data = json.load(f)

    return data
