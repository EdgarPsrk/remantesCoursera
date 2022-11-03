var Bicicleta = require('../../models/bicicleta.js');

exports.bicicletas_list = (req, res) => res.status(200).json({bicicletas:Bicicleta.allBicis});

exports.bicicleta_create = (req, res) => 
{
    var bici = new Bicicleta(req.body.id, req.body.color, req.body.modelo);
    bici.ubicacion = [req.body.lat, req.body.lng];
    // var bici = new Bicicleta(4, 'gris', 'urbana');
    // bici.ubicacion = [19.370376, -99.290559];

    Bicicleta.add(bici);
    console.log(bici);
    res.status(200).json({ bicicleta: bici})
}

exports.bicicleta_delete = (req, res) =>
{
    Bicicleta.removeById(req.body.id);
    res.status(204).send();
}

exports.mensaje = (req, res) => res.status(200).json({ nota: "jala"});


// {
//     "id": 4,
//     "color": "gris",
//     "modelo": "urbano",
//     "lat": 19.370376, 
//     "lng": -99.290559
// }