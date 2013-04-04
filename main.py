#coding: utf-8
#Created By Htedsv

import tornado.ioloop
import tornado.autoreload
import tornado.httpserver
from urls import URL
import configs

settings = dict(
    title = 'OpenTask',
    login_url = '/login/',
    template_path = configs.TEMPLATE_PATH,
    static_path = configs.STATIC_PATH,
    cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    debug = True,
)

application = tornado.web.Application(URL, **settings)

if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(application)
    server.listen(configs.PORT)
    instance = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(instance)
    instance.start()
