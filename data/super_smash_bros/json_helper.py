import json
import pickle
import os


def read_json(file_path):
    with open(file_path, 'r') as f:
        json_object = json.load(f)
    return json_object


def read_all_json_files(dir_path):
    json_objects = []
    for file in os.listdir(dir_path):
        if file.endswith('.json'):
            json_path = os.path.join(dir_path, file)
            json_object = read_json(json_path)
            json_objects.append(json_object)
    return json_objects


def write_pickle(file_path, data):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)


def load_pickle(file_path):
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data


file_path = 'super_smash_characters.pickle'
data = load_pickle(file_path)
print(data)
