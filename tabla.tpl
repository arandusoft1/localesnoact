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
                
            % for post in posts:
            <tr> 
                <th>{{post[0]}}</th>
                <th>{{post[1]}}</th>
                <th>{{post[2]}}</th>
                <th>{{post[3]}}</th>
            </tr> 
            % end            
            
        </table>

    </body>
</html>
