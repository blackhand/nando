# -*- coding: utf-8 -*-
"""
Initial Nando Handlers (views in Django parlance)
"""

from common import RequestHandler


class HomePage(RequestHandler):
    def get(self):
        return self.render_response('home.html')
