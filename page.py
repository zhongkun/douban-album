# -*- coding: utf-8 -*-
import tornado.web
from consts import *
from utils import *
from proxy import *
import os
import mako
from mako.template import Template
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

class LoginHandler(BaseHandler):
	def get(self):
		code = self.get_argument('code', None)
		print 'the code is===================='
		print code
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
			self.redirect('/static/img/proxy/'+name)


class IndexHandler(BaseHandler):
	@tornado.web.authenticated    
	def get(self):
		name = tornado.escape.xhtml_escape(self.current_user)
		print "======== IndexHandler ============"
		client.auth_with_token(name)
		album = client.album.liked_list(client.user.me['id'])
		self.render("index.html", title = u'豆瓣相册', items = album['albums'])
