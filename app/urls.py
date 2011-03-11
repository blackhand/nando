# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy import Rule

rules = [
    Rule('/', name='homepage', handler='nando.handlers.HomePage'),
]
