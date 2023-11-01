import json

with open(".\\config\\environment.json", "r") as json_file:
    data = json.load(json_file)


def get_environment_url(env):
    base_url = data["login_creds"][env]["base_url"]
    return base_url


def get_user_name(env):
    user_name = data["login_creds"][env]["user_name"]
    return user_name


def get_pass_word(env):
    password = data["login_creds"][env]["pass_word"]
    return password

