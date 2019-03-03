# create a virtual environment
# pip install virtualenv (pip3 if on unix/mac)
# virtualenv env
# Windows env\scripts\activate
# Unix source env/bin/activate
# pip install -r requirements.txt
# learn more about requests - http://docs.python-requests.org/en/master/

import requests
import json
import os

# iterate through json data
def for_json(data):
    json_list = []
    for i in data:
        json_list.append(i["full_name"])

    save_json(json_list)

    return "done"


def save_json(data):
    file_path = (os.path.abspath("tmp/data.json"))
    with open(file_path, "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)

    return "done"


def save_all_json(data):
    file_path = (os.path.abspath("tmp/all_data.json"))
    with open(file_path, "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)

    return "done"


def call_api(url):
    r = requests.get(url)
    # print(r.status_code)
    data = r.json()
    # Parse JSON data and save to file
    result = for_json(data)
    # Save full JSON response and save to file
    save_all_json(data)

    # Print result of JSON parse
    print(result)


url = "https://api.github.com/users/octokit/repos"


if __name__ == "__main__":
    call_api(url)
