import json


def get_configs(filename):
    # TODO: check if file exists
    with open(filename, 'r') as f:
        return json.load(f)