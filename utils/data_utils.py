import json


def load_test_data() -> dict:
    with open("./data/test_data.json", encoding="utf-8") as f:
        return json.load(f)
