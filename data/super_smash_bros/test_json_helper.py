import os
import json_helper


def test_read_all_json_files():
    dir_path = 'test_directory'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file1 = os.path.join(dir_path, 'file1.json')
    with open(file1, 'w') as f:
        json.dump({'name': 'Mario', 'game': 'Super Mario Bros.'}, f)
    file2 = os.path.join(dir_path, 'file2.json')
    with open(file2, 'w') as f:
        json.dump({'name': 'Link', 'game': 'The Legend of Zelda'}, f)
    expected = [{'name': 'Mario', 'game': 'Super Mario Bros.'}, {'name': 'Link', 'game': 'The Legend of Zelda'}]
    actual = json_helper.read_all_json_files(dir_path)
    assert actual == expected, f"Expected {expected}, but got {actual}"

    # clean up
    os.remove(file1)
    os.remove(file2)
    os.rmdir(dir_path)