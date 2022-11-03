const bicicleta_list = require("../controllers/bicicleta");

var Bicicleta = function(id, color, modelo, ubicacion) 
{
    this.id = id;
    this.color = color;
    this.modelo = modelo;
    this.ubicacion = ubicacion;
};

Bicicleta.prototype.toString = () =>
{
    return 'id: ' + this.id + 'color: ' + this.color
}

Bicicleta.allBicis = [];
Bicicleta.add = (bici) => Bicicleta.allBicis.push(bici);

Bicicleta.findById = (aBiciId) =>
{
    var aBici = Bicicleta.allBicis.find( x => x.id == aBiciId);
    if(aBici)
        return aBici
    else
        throw new Error(`No existe una bicicleta con el id ${aBiciId}`);    

}


Bicicleta.removeById = (aBiciId) =>
{
    for(let i = 0; i<Bicicleta.allBicis.length; i++)
    {
        if(Bicicleta.allBicis[i].id == aBiciId)
        {
            Bicicleta.allBicis.splice(i, 1);
            break;
        }
    }

}

var biciA = new Bicicleta(1, 'Roja', 'urbana', [19.3834, -99.2995]);
var biciB = new Bicicleta(2, 'Verde', 'urbana', [19.3558, -99.3045]);

Bicicleta.add(biciA);
Bicicleta.add(biciB);



module.exports = Bicicleta; 