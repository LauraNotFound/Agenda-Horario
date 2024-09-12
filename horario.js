var modal = document.getElementById("myModal");
var btn = document.getElementById("modal-btn");
var span = document.getElementsByClassName("btn-close")[0];
var save = document.getElementsByClassName("btn-guardar")[0];

btn.onclick = function () {
    modal.style.display = "block";
}

span.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

save.onclick = function () {
    modal.style.display = "none";
}

// Almacenar la actividad y luego mostrarla en la casilla correspondiente del horario

document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('myModal');
    const saveBtn = document.getElementById('saveActivity');

    document.getElementById('modal-btn').onclick = function () {
        modal.style.display = 'block';
    };

    document.querySelector('.btn-close').onclick = function () {
        modal.style.display = 'none';
    };

    saveBtn.onclick = function () {
        const dia = document.getElementById('dia').value;
        const hora = document.getElementById('hora').value;
        const color = document.getElementById('color').value;
        const actividad = document.getElementById('activity').value;

        const nuevaActividad = {
            dia: dia,
            hora: hora,
            color: color,
            actividad: actividad
        };

        fetch('http://localhost:3000/actividades', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(nuevaActividad)
        })
            .then(response => response.json())
            .then(data => {
                mostrarActividad(data);
                modal.style.display = 'none';
            })
            .catch(error => console.error('Error:', error));
    };

    function mostrarActividad(actividad) {
        const selector = `.casilla[data-dia="${actividad.dia}"][data-hora="${actividad.hora}"]`;
        const casilla = document.querySelector(selector);
        if (casilla) {
            casilla.innerHTML = `<span data-bs-toggle="tooltip" style="color: ${actividad.color}; margin: 0%; cursor:pointer"; title="${actividad.actividad}">${actividad.actividad}</span>`;
            var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
            var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
                return new bootstrap.Tooltip(tooltipTriggerEl)
            });
        }
    }

    function cargarActividades() {
        fetch('http://localhost:3000/actividades')
            .then(response => response.json())
            .then(data => {
                data.forEach(actividad => mostrarActividad(actividad));
            })
            .catch(error => console.error('Error:', error));
    }

    cargarActividades();
});
