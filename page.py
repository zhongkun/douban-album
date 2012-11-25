# -*- coding: utf-8 -*-
import tornado.web
from consts import *
from utils import*

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("album-token")

class LoginHandler(BaseHandler):
    def get(self):
        code = self.get_argument('code', None)
        print 'jj'
        if code:
            auth_with_code(code)
            self.set_secure_cookie('album-token', get_token())
            self.redirect('/')
        else:
            self.redirect(auth())

class IndexHandler(BaseHandler):
    @tornado.web.authenticated    
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        client.auth_with_token(name)
        print client.user.me
#        CLIENT.album.like_list
        album = client.album.liked_list(client.user.me['id'])

        print album
        self.write("Hello, " + name)
        
