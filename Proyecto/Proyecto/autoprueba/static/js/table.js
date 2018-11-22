  $(document).ready(function(){
        $(".add-row").click(function(){

            var markup = " <tr> <td> <select class='form-control' id='event' name='evento[]'> <option>click</option> <option>wait</option> <option>press</option><option>fill input</option> </select> </td> <td> <select class='form-control' id='type' name='type[]'> <option>button</option> <option>input</option> <option>link text</option> </select> </td> <td> <input type='text' class='form-control' id='finder' placeholder='Buscador' name='finder[]'> </td> <td> <input type='text' class='form-control' id='value' placeholder='Valor' name='value[]'> </td> </tr>";
            $("table").append(markup);
        });

          $(".add-column").click(function(){
            console.log("fdsf");
            var markup = "<tr> <td> <select class='form-control' id='event' name='column[]'> <option>Alfanumérico</option> <option>Autoincremento</option> <option>Booleano</option> <option>CVV</option> <option>Ciudad</option> <option>Compañias</option> <option>Paises</option> <option>Fecha</option> <option>Nombre Masculino</option> <option>Nombre Femenino</option> <option>Apellido</option> <option>Correo</option> </select> </td> <td> <input type='text' class='form-control' id='nombreColumna' placeholder='Nombre columna' name='nombreColumna[]'> </td> </tr>";
            $("table").append(markup);
        });

        $(".add-reg").click(function(){
          console.log("fdsf");
          var markup = "<tr> <td> <select class='form-control' id='event' name='type[]'> <option>Alfanumérico</option> <option>Autoincremento</option> <option>Booleano</option> <option>CVV</option> <option>Ciudad</option> <option>Compañias</option> <option>Paises</option> <option>Fecha</option> <option>Nombre Masculino</option> <option>Nombre Femenino</option> <option>Apellido</option> <option>Correo</option> </select> </td> <td> <input type='text' class='form-control' id='nombreColumna' placeholder='Nombre variable' name='nombreVariable[]'> </td> </tr>";
          $("table").append(markup);
      });

        // Find and remove selected table rows
        $(".delete-row").click(function(){
            $("table tbody").find('input[name="record"]').each(function(){
                if($(this).is(":checked")){
                    $(this).parents("tr").remove();
                }
            });
        });
    });
