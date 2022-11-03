var dato = [859.20, 546.89, 348.45, 320];
var iva = 0.16;
var cantidad = 10;
var dat0 = 0;
var longitud = dato.length;
var cambiao = 0;
var resultados = [];

function imp(coso)
{
    console.log(coso);
}



// function operacion(dato)
// {
//     resultado = dato * iva;
//     return resultado
// }
// function iterado()
// {
//     for (cambiao in range (longitud))
//     {
//         dato2 = operacion(dato[cambiao]);
//         console.log(dato2);
//         resultados.push(dato2);
//     }
// }
// if ( cantidad != 0)
// {
//     console.log("podemos operar");
//     dat0 = operacion();
//     console.log(dat0);
    
// }
// else
// {
//     console.log("nesesitamos otro numero");
// }

for (let cambiao; cambiao < longitud; cambiao++ )
{
    console.log(dato[cambiao]);
}
console.log(dato[1]);
imp(longitud);
 