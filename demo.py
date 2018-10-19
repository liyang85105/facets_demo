#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8086, help="run on the given port")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]

        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), 'template'),
            static_path = os.path.join(os.path.dirname(__file__), 'static'),
            debug = True,
        )

        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",)

    def post(self):
        import time
        title = self.get_argument('title', None)
        content = self.get_argument('content', None)
        self.redirect('/')

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
