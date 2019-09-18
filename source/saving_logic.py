import json


def save_data_to_file(filepath, dictionary_name):
    with open(filepath, "w") as f:
        json.dump(dictionary_name, f)
