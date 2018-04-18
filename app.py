#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import bottle
import json
from bottle import route,run

bottle.debug(True)

@route('/')
def index():
	leer = json.loads(open('locales.json').read())	
	return leer

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
