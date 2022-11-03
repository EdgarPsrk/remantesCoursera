const express = require('express');
const router = express.Router();
const bicicletaController = require('../../controllers/API/controllerApi.js');

router.get('/', bicicletaController.bicicletas_list);
router.post('/create', bicicletaController.bicicleta_create);
router.delete('/delete', bicicletaController.bicicleta_delete);

router.get('/pru', bicicletaController.mensaje);

module.exports = router;