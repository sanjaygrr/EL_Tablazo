< script >
    $(document).ready(function() {
        $('#error').hide();

        $('#formulario').submit(function(event) {
            var mensaje = "";
            if ($('#run').val().trim().length == 7) {
                mensaje = "El run está en blanco";
            }
            if ($('#nombre').val().trim().length == 0) {
                mensaje = "El nombre está en blanco";
            }
            if ($('#edad').val().trim().length == 0) {
                mensaje = "edad está en blanco";
            }
            if ($('#email').val().trim().length == 0) {
                mensaje = "El email está en blanco";
            }
            if ($('#telefono').val().trim().length == 0) {
                mensaje = "El telefono está en blanco";
            }

            if ($('#motivo').val().trim().length == 0) {
                mensaje = "motivo está en blanco";
            }
            if ($('#comentario').val().trim().length == 0) {
                mensaje = "El comentario está en blanco";
            }

            if (mensaje != "") {
                $('#error').html(mensaje);
                $('#error').show();
                event.preventDefault();
            }
        });
    }); <
/script>


<
/div> <
div class = "mb-3" >
    <
    label
for = "run"
class = "form-label" > Run < /label> <
    input type = "number"
class = "form-control"
id = "run"
placeholder = "12345678-9" >
    <
    /div> <
    div class = "mb-3" >
    <
    label
for = "nombre"
class = "form-label" > Nombre < /label> <
    input type = "text"
class = "form-control"
id = "nombre"
placeholder = "Pedro Pablo Perez Pereira"
required >
    <
    /div> <
    div class = "mb-3" >
    <
    label
for = "edad"
class = "form-label" > Edad < /label> <
    input type = "number"
class = "form-control"
id = "edad"
placeholder = "99"
required >
    <
    /div> <
    div class = "mb-3" >
    <
    label
for = "correo"
class = "form-label" > Email < /label> <
    input type = "email"
class = "form-control"
id = "correo"
placeholder = "nombre@ejemplo.com"
required >
    <
    /div> <
    div class = "mb-3" >
    <
    label
for = "numero telefono"
class = "form-label" > Teléfono < /label> <
    input type = "telefono"
class = "form-control"
id = "telefono"
placeholder = "+569 98765432" >
    <
    /div> <
    div >
    <
    label
for = "motivo" > Motivo < /label> <
    select class = "form-select form-select-lg mb-3"
aria - label = ".form-select-lg example"
placeholder = "motivo"
required >
    <
    option value = "1" > Consulta < /option> <
    option value = "2" > Reclamo < /option> <
    option value = "3" > Sugerencia < /option> <
    option value = "4" > Otro < /option> <
    /select> <
    /div>