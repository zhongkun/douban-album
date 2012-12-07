import tornado.ioloop
import tornado.web
import os
from page  import *
        
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    'cookie_secret' : '61oETzKXQAGaYdkL5gEmGeJJFuYh7JFAI398302JXzk/Vo=',
    'login_url' : '/login',
}
application = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/index", IndexHandler),
    (r"/login", LoginHandler),
    (r"/proxy", ProxyHandler),
	(r"/photos", PhotosHandler), 
    ], **settings)

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

