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
	tabla = "|&nbsp;&nbsp;&nbsp;Nombre local&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fecha de Vigencia&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;Cantidad de Producto&nbsp;&nbsp;|"
	
	for elemento in leer:
		tabla = tabla + '<br />\n' + "|&nbsp;" + elemento["NomLocal"] + "&nbsp;"*(21-len(elemento["NomLocal"])) + "|&nbsp;" + elemento["fVigencia"] + "&nbsp;"*(30-len(elemento["fVigencia"])) + "|&nbsp;" + str(elemento["CantidadPro"]) + "&nbsp;"*(21-len(str(elemento["CantidadPro"]))) + "|"
			
	return tabla

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
