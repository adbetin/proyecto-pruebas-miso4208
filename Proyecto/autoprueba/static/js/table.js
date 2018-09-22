  $(document).ready(function(){
        $(".add-row").click(function(){

            var markup = " <tr> <td> <select class='form-control' id='event' name='evento[]'> <option>click</option> <option>wait</option> <option>press</option><option>fill input</option> </select> </td> <td> <select class='form-control' id='type' name='type[]'> <option>button</option> <option>input</option> <option>link text</option> </select> </td> <td> <input type='text' class='form-control' id='finder' placeholder='Buscador' name='finder[]'> </td> <td> <input type='text' class='form-control' id='value' placeholder='Valor' name='value[]'> </td> </tr>";
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