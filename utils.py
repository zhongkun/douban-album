# -*- coding: utf-8 -*-

from consts import *

def auth():
    return client.authorize_url

def auth_with_code(code):
    client.auth_with_code(code)

def get_token():
    return client.client.token
