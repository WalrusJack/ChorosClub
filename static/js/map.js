$(() => {
    let map = L.map('map').setView([0, 0], 1);
    let marker = null;
    let place = null;

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    $('#place-search').on('click', search);

    $('#place-list').on('change', updateMarker);

    function search(e) {
        let url = 'https://nominatim.openstreetmap.org/search?format=json&q=' + $('#place-text').val();
        $.ajax({
            url: url,
            dataType: 'json',
            success: (data) => {
                place = data;
                const placeList = $('#place-list');
                placeList.empty();
                for (let i = 0; i < data.length; i++)
                    placeList.append(`<option value="${i}">${place[i].display_name}</option>`);
                updateMarker();
            }
        });
        e.preventDefault();
        e.stopPropagation();
    }

    function updateMarker() {
        let selectedIndex = $('#place-list :selected').index();
        let name = place[selectedIndex].display_name;
        let coord = [place[selectedIndex].lat, place[selectedIndex].lon];

        $('#place').attr('value', name);
        if (marker === null)
            marker = L.marker(coord).addTo(map);
        else
            marker.setLatLng(coord);
        map.setView(coord);
    }
});