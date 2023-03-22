import json
import pickle
import os


def read_json(path):
    with open(path, 'r') as file:
        data = json.load(file.read())
        return data

def read_all_json_files(path):
    with open(path, 'r') as file:


