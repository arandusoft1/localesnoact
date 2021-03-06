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
	con.execute("select * from Empresas;")
	rows = con.fetchall()
	empresas= []
	fmt = '%d/%m/%y %H:%M:%S'
	ultact = "01/01/01 00:00:00"
	d2 = datetime.strptime(ultact,fmt)	
	
	for row in rows:
		empresas.append({"Empresa": row[1],"Sucursal": row[2],"fVigencia": row[3],"CantPrecio": row[4]})
		#fvig.append({"fVigencia": row[3]})
		d1 = datetime.strptime(row[3],fmt)		
		diffhora= ((d1-d2).seconds)/3600.0
		diffdias= (d1-d2).days
		
		if diffdias > 0:
			d2 = d1
			ultact = row[3]
		elif diffdias == 0:
			if diffhora > 0:
				d2 = d1
				ultact = row[3]
		
				
			

			
	
	#return repr(fvig)
	
	leer = {"Empresas":  empresas , "UltAct": [{"fVigencia": ultact }]}
		

	#leer = json.loads(open('locales.json').read())	
	return template('tabla.tpl', leer)

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
