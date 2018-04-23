#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import bottle
import json
from bottle import route,run,Bottle,template
from datetime import datetime
import psycopg2, psycopg2.extras

bottle.debug(True)

@route('/')
def index():
	conn = psycopg2.connect(database='d3fkm1msg7kiub',user='wdtetudvoejjev',password='b7fefda1a504e80018b763ba3d8bcb94804c54dfff9a3372b4a70ee042dadf22', host='ec2-54-83-1-94.compute-1.amazonaws.com')
	con = conn.cursor()
	con.execute("select * from Empresas")
	rows = con.fetchall()
	#empresas= []
	
	for row in rows:
		# empresas.append({"Empresa": row[1],"Sucursal": row[2],"fVigencia": row[3],"CantPrecio": row[4]})
		print row
	
	#leer = {"Empresas": [ empresas ], "UltAct": [{"fVigencia": "05/03/18 00:00:00"}]}
	
		
	leer = json.loads(open('locales.json').read())	
	return template('tabla.tpl', leer)

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
