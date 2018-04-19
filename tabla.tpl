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
            table .amarillo {
                background-color:yellow;
            }
            table .verde {
                background-color:green;
            }
            
        </style>
    </head>
    <body bgcolor=#f1f1c1>
        <table style="width:100%">
            <tr>
                <th>Empresa</th>
                <th>Sucursal</th> 
                <th>Fecha de Vigencia</th>
                <th>Cantidad de Precios</th>
            </tr>
            
             % from datetime import datetime
             % fmt = '%d/%m/%y %H:%M:%S'
             % ultVigencia = UltAct[0]['fVigencia']
             % d1 = datetime.strptime(ultVigencia,fmt) #Ultima vigencia
             
            %for elemento in Empresas:
                
               
                % eltoVigencia = elemento['fVigencia']                
                % d2=datetime.strptime(eltoVigencia,fmt)   #Elemento vigencia
                % diffseg= ((d1-d2).seconds)/3600.0  
                % diffdias= (d1-d2).days
                
                %if diffseg > 24 or diffdias > 0 :
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
                    <tr class="amarillo">
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
