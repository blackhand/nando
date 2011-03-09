# -*- coding: utf-8 -*-
"""
Initial Nando Handlers (views in Django parlance
"""


from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin


class HelloWorldHandler(RequestHandler):
    def get(self):
        """Simply returns a rendered template with an enigmatic salutation."""
        context = {
            'message': 'Hello, World!',
        }
        return self.render_response('hello_world.html', **context)
