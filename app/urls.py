# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy import Rule

rules = [
    Rule('/', name='hello-world', handler='hello_world.handlers.HelloWorldHandler'),
]
