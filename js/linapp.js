var express = require('express');

var app = express();

app.all( '/', function(peticion, respuesta)
{
    respuesta.send('Trapeton el show');
});

var server = app.listen(3000, function()
{
    console.log("Aplicacion ejemplo, escuchando el puerto 3000 !");
});