"""Automation for commenting on posts."""

import os
import requests
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

load_dotenv()


def get_page_id(user_id):
    url = os.path.join(os.getenv("FACEBOOK_ENDPOINT"), user_id ,"accounts")
    param = dict()
    
    param["access_token"] = os.getenv("FACEBOOK_APP_TOKEN")
    response = requests.get(url=url, params=param)
    response = response.json()

    print(response)
    
    return ""


def get_user_id(handle: str):
    url: str = os.path.join(os.getenv("FACEBOOK_ENDPOINT"), handle)
    params = {"access_token": os.getenv("FACEBOOK_APP_TOKEN")}

    response = requests.get(url, params=params)
    return response.json()


def upload_comment(account):
    pass
