import json


def save_data_to_file(filepath, dictionary_name):
    with open(filepath, "w") as f:
        json.dump(dictionary_name, f)


def load_data_to_dict(filepath):
    with open(filepath, "r") as f:
        return_dict = json.load(f)
    return return_dict
