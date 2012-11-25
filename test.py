# -*- coding:utf-8 -*- ＃
import unittest
from utils import * 
from consts import *

class TestModel(unittest.TestCase):

    def setUp(self):
#        print 'url:%s' % client.authorize_url
        client.auth_with_token('24735e9cc8ccfc936d5a1bd65a66f5b9')
        print 'heards %s' % client.client.headers
        
    def test_build_album(self):
#        login()
        album = client.album.liked_list(client.user.me['id'])
        print 'album %s' % album
        print 'token:%s' % client.client.token
 
        print 'guess:%s' % dir(client.guess)
        
    def test_get_user(self):
        ret = client.user.me['id']
        print ret
if __name__ == "__main__":
    unittest.main()
