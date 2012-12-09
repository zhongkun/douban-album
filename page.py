# -*- coding: utf-8 -*-
import tornado.web
from consts import *
from utils import *
from proxy import *
import os
import mako
from mako.template import Template
import urllib2
from mako.lookup import TemplateLookup

class BaseHandler(tornado.web.RequestHandler):
    lookup = TemplateLookup(['./templates'])	
    def render(self, template_name, **kwargs):
        t = self.lookup.get_template(template_name)
        args = dict(
                handler=self,
                request=self.request,
                locale=self.locale,
                _=self.locale.translate,
                static_url=self.static_url,
                xsrf_form_html=self.xsrf_form_html,
                reverse_url=self.application.reverse_url,
                )
        args.update(kwargs)
        html = t.render(**args)
        self.finish(html)

    def get_current_user(self):
        return self.get_secure_cookie("album-token")

    def auth_with_token():
        name = tornado.escape.xhtml_escape(self.current_user)
        client.auth_with_token(name)

class LoginHandler(BaseHandler):
    def get(self):
        code = self.get_argument('code', None)
        if code:
            auth_with_code(code)
            token = get_token()
            print 'token %s' % token
            self.set_secure_cookie('album-token', token)
            self.redirect('/')
        else:
            self.redirect(auth())

class ProxyHandler(BaseHandler):
    def get(self):
        url =  self.get_argument('url', None)
        if url:
            name = download_image(url, os.getcwd()+"/static/img/proxy/")
            if name:
                self.redirect('/static/img/proxy/'+name)

class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html', title = u'豆瓣相册')

class StarHandler(BaseHandler):
    @tornado.web.authenticated    
    def get(self):
        self.auth_with_token()
        p = int(self.get_argument('page', 1))
        #album = client.album.liked_list(client.user.me['id'], 0, 30) 
        count = 15
        uid = '3825598'
        start = count * (p-1)
        end = count * p
        key = uid + str(start) + str(end)
        album = mc.get(key)
        if not album:
            album = client.album.list('3825598', count * (p-1), count * p)
            mc.set(key, album, 3600)
        self.render("hot.html", title = u'豆瓣相册', items = album['albums'], page = p+1, tab = 2)

class PhotosHandler(BaseHandler):
    @tornado.web.authenticated    
    def get(self):
        self.auth_with_token()
        photos = client.album.photos('32349140')
        self.render("photos.html", title = u'相册', items = photos['photos'])

class UseAlbumHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.auth_with_token()
        user_id = self.get_argument('user_id', None)

class FriendsAlbumHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.auth_with_token()
        user_id = self.get_argument('user_id', None)


