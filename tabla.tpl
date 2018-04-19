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
                %for i in range(1):
                    <tr>
                        %for r in elemento:
                            <td>{{elemento[r][i]}}</td>
                        %end
                    </tr>
                %end                   
            %end 
            
        </table>

    </body>
</html>
