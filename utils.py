# -*- coding: utf-8 -*-

from consts import *
from douban_client import DoubanClient
def auth():
    if isinstance(client, DoubanClient):
        dir(client)
        return client.authorize_url
#    if not isinstance(client, AccessToken)

def auth_with_code(code):
    client.auth_with_code(code)

def get_token():
    return client.client.token
