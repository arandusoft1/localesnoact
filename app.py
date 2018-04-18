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
	tabla = "<style> table, th, td { border: 1px solid black; border-collapse: collapse; } th, td { padding: 5px; text-align: left; background-color: #f1f1c1;} </style> <table style=" + '"width:100%"'+ "> <tr> <th>Empresa</th> <th>Sucursal</th> <th>Fecha de Vigencia</th> <th>Cantidad de Precios</th> </tr>"
	
	for elemento in leer:
		tabla = tabla + "<tr> <td>"+ elemento["Empresa"] +"</td> <td>"+elemento["Sucursal"]+"</td> <td>"+elemento["fVigencia"]+"</td> <td>"+ str(elemento["CantPrecio"])+" </td> </tr> "
		
	tabla = tabla +  "</table> "
			
	return tabla

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
