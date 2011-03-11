#!/usr/bin/python2.5

import os

join = os.path.join
base = os.getcwd()

import sys
sys.path[0:0] = [
    join(base, 'app'),
    join(base, 'app/lib'),
    join(base, 'app/lib/dist'),
    join(base, 'var/parts/google_appengine'),
    ]
