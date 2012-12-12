# -*- coding: utf-8 -*-
import tornado.web
from consts import *
from utils import *
from proxy import *
import os
import mako
from mako.template import Template
import urllib2
import time
from mako.lookup import TemplateLookup
from avatar_wall import *

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
        return self.get_secure_cookie("album-user")

    def handler_auth():
        name = tornado.escape.xhtml_escape(self.current_user)
        client.auth_with_token(name)

class LoginHandler(BaseHandler):
    def get(self):
        code = self.get_argument('code', None)
        if code:
            user = {}
            auth_with_code(code)
            token = get_token()
            print 'token %s' % token
            user['token'] = token
            user['userinfo'] = client.user.me
            self.set_secure_cookie('album-user', str(user))
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
        login(self)
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

class LikeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        login(self)
        user = eval(tornado.escape.xhtml_escape(self.current_user))
        p = int(self.get_argument('page', 1))
        count = 15
        start = count * (p-1)
        end = count * p
        uid = user['userinfo']['id']
        key = ('like_%s_%s_%s' % (uid, start, end)).encode('utf8')
        print key
        album = mc.get(str(key))
        if not album:
            album = client.album.liked_list(user['userinfo']['id'], start, end)
            mc.set(key, album, 1800)
        self.render('like.html', title = u'豆瓣相册', items = album['albums'], page = p+1, tab = 3)

class PhotosHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.handler_auth()
        photos = client.album.photos('32349140')
        self.render("photos.html", title = u'相册', items = photos['photos'])

class UseAlbumHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        login(self)
        user_id = self.get_argument('user_id', None)

class FriendsAlbumHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        login(self)
        user_id = self.get_argument('user_id', None)

class CompoundFollowAvatarHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        login(self)
        self.render('compound_picture')

class DoCompoundPictureHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        login(self)
        uid = self.get_argument('uid', None)
        album_id = self.get_argument('album_id', None)
        if uid != None:
           user_list = client.user.following(uid, count = 400)
           print user_list
           path = '%s/static/img/avatar_wall/%s/' % (os.getcwd(), uid)
           for item in user_list:
              url = item['large_avatar'].replace('ul', 'u')
              if 'site' in url:
                 continue
              download_image(url, path)
              time.sleep(1)
           compound_avatar(path)
        elif album_id != None:
            photos_list = client.album.photos(album_id)
        else:
            print 'input err'

def login(h):
    if not isLogin():
        name = eval(tornado.escape.xhtml_escape(h.current_user))
        client.auth_with_token(name['token'])

