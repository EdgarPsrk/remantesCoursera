var mymap = L.map('mapid').setView([19.4346, -99.1413], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

// L.marker([19.409367, -99.172796]).addTo(mymap);
// L.marker([19.412682, -99.166473]).addTo(mymap);

$.ajax({
    dataType: 'json',
    url: 'API/bicicletas',
    success: (result) =>
    {
        console.log(result);
        result.bicicletas.forEach( (bici) => L.marker(bici.ubicacion, {title: bici.id}).addTo(mymap) );
    }
})