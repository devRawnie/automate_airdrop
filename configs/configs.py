import json


def get_configs(filename='configs/configs.json'):
    # TODO: check if file exists
    with open(filename, 'r') as f:
        return json.load(f)