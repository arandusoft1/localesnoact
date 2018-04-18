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
	tabla = " <h2>Collapsed Borders</h2> <p>If you want the borders to collapse into one border, add the CSS border-collapse property.</p> <table style="width:100%">   <tr>     <th>Firstname</th>     <th>Lastname</th>      <th>Age</th>   </tr>   <tr>     <td>Jill</td>     <td>Smith</td>     <td>50</td>   </tr>   <tr> <td>Eve</td>     <td>Jackson</td>     <td>94</td>   </tr>   <tr>     <td>John</td>     <td>Doe</td>     <td>80</td>  </tr> </table> "
	
		
	return tabla

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
