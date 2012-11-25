import tornado.ioloop
import tornado.web
from page  import *
        
settings = {
    'cookie_secret' : '61oETzKXQAGaYdkL5gEmGeJJFuYh7JFAI398302JXzk/Vo=',
    'login_url' : '/login',
}
application = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/login", LoginHandler),
    ], **settings)

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

