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
        </style>
    </head>
    <body>
        <table style="width:100%">
            <tr>
                <th>Empresa</th>
                <th>Sucursal</th> 
                <th>Fecha de Vigencia</th>
                <th>Cantidad de Precios</th>
            </tr>
            
            %for elemento in Empresas:
                % if elemento['fVigencia'] == "Tue, 02 Nov 2010 18:24:52 GMT":
                    <tr class="rojo">
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
            
        </table>

    </body>
</html>
