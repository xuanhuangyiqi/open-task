import tornado.web
from views import *

URL = [
    (r"/task/(.*)/", TaskHandler),
    (r"/statics/(.*)", tornado.web.StaticFileHandler, {"path": "./statics/"}),
    (r"/", MainHandler),
    ]

