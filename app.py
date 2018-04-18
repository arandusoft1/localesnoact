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
	tabla = "<style> table, th, td { border: 1px solid black; border-collapse: collapse; } th, td { padding: 5px; } th { text-align: left; } </style> <table style=" + '"width:100%"'+ "> <tr> <th>Firstname</th> <th>Lastname</th> <th>Age</th> </tr> <tr> <td>Jill</td> <td>Smith</td> <td>50</td> </tr> </table> "
	
		
	return tabla

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
