<html>
    <head>
        <h1>Estado de Vigencia de Empresas</h1>
        <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th, td {
                padding: 5px;
            }
            th {
                text-align: left;
            }
            table .rojo {
                background-color:red;
            }
            table .verde {
                background-color:green;
            }
            
        </style>
    </head>
    <body>
        <table style="width:100%">
            <tr>
                <th>UltAct[0]['fVigencia']['Fecha']</th>
                <th>Sucursal</th> 
                <th>Fecha de Vigencia</th>
                <th>Cantidad de Precios</th>
            </tr>
            
             % from datetime import datetime
             % fmt = '%d/%m/%y %H:%M:%S'
             % ultVigencia = '05/03/18 00:00:00' #UltAct[0]['fVigencia']['Fecha'] + ' ' + UltAct[0]['fVigencia']['Hora']
             % d1 = datetime.strptime(ultVigencia,fmt) #Ultima vigencia
             
            %for elemento in Empresas:
                
               
                % eltoVigencia = elemento['fVigencia']                
                % d2=datetime.strptime(eltoVigencia,fmt)   #Elemento vigencia
                % diff= ((d1-d2).seconds)/3600.0          
                
                %if diff > 24 :
                    <tr class="rojo">
                        <td>{{elemento['Empresa']}}</td> 
                        <td>{{elemento['Sucursal']}}</td> 
                        <td>{{elemento['fVigencia']}}</td> 
                        <td>{{elemento['CantPrecio']}}</td> 
                    </tr>
                %elif elemento['fVigencia'] == UltAct[0]['fVigencia']:
                    <tr class="verde">
                        <td>{{elemento['Empresa']}}</td> 
                        <td>{{elemento['Sucursal']}}</td> 
                        <td>{{elemento['fVigencia']}}</td> 
                        <td>{{elemento['CantPrecio']}}</td> 
                    </tr>             
                %else:
                    <tr>
                        <td>{{elemento['Empresa']}}</td> 
                        <td>{{elemento['Sucursal']}}</td> 
                        <td>{{elemento['fVigencia']}}</td> 
                        <td>{{elemento['CantPrecio']}}</td> 
                    </tr>
                 %end   
                        
            %end 
            
        </table>

    </body>
</html>
