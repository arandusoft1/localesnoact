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
	tabla = "|   Nombre local   |       Fecha de Vigencia         |  Cantidad de Producto  |"
	
	for elemento in leer:
		tabla = tabla + "\n" + "|" + elemento['NomLocal'] + "  "*(15-len(elemento['NomLocal'])) + "|" + elemento['fVigencia'] + "  "*(30-len(elemento['NomLocal'])) + "|" + elemento['NomLocal'] + "  "*(21-len(str(elemento['CantidadPro']))) + "|"
			
	return tabla

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
