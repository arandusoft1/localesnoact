#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import bottle
import json
from bottle import route,run,Bottle,template

bottle.debug(True)

@route('/')
def index():
	leer = json.loads(open('locales.json').read())	
				
	return template('tabla.tpl', leer)

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
