"""Handle Facebook authentication."""

import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_long_lived_token() -> str:
    """Exchange short lived with long lived token."""
    url: str = os.path.join(os.getenv("FACEBOOK_ENDPOINT"), "oauth", "access_token")
    param = dict()

    param["grant_type"] = "fb_exchange_token"
    param["client_id"] = os.getenv("FACEBOOK_APP_ID")
    param["client_secret"] = os.getenv("FACEBOOK_SECRET")
    param["fb_exchange_token"] = os.getenv("FACEBOOK_ACCESS_TOKEN")

    response = requests.get(url=url, params=param)

    response = response.json()
    long_lived_token = response["access_token"]

    return long_lived_token
