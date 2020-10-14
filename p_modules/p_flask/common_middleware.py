#  -*- coding: UTF-8 –*-
#  Copyright (c) 2020.
#  author: Liu Yingpeng

class MyMiddleWare(object):

    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        def custom_start_response(status, headers):
            # do something
            return start_response(status, headers)
        return self.wsgi_app(environ, custom_start_response)