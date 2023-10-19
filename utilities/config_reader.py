import json

with open(".\\config\\environment.json", "r") as json_file:
    data = json.load(json_file)


def get_environment_url(env):
    base_url = data["login_creds"][env]["base_url"]
    return base_url

