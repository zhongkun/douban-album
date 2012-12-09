# -*- coding: utf-8 -*-
from pyoauth2 import AccessToken
from consts import *
from douban_client import DoubanClient
def auth():
    if not isinstance(client, AccessToken):
        dir(client)
        return client.authorize_url
#    if not isinstance(client, AccessToken)

def auth_with_code(code):
    client.auth_with_code(code)

def get_token():
    return client.client.token

def isLogin():
    if isinstance(client, AccessToken) and client.client.token:
        return True

    return False
