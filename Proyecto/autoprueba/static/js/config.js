$( document ).ready(function() {
        $('#btnAgregarAppWeb').on('click',function(){
                $('#tablaAppWeb tbody').append('<tr>'+$('.filaWeb').html() +'</tr>');
        });

        $('#btnAgregarAppMovil').on('click',function(){
                $('#tablaAppMovil tbody').append('<tr>'+$('.filaMovil').html() +'</tr>');
        });

        $('#tablaAppWeb tbody' ).on('click','.btnEliminarAppWeb',function(){
             if( $('.btnEliminarAppWeb').length > 1) {
                        $(this).parents('tr').remove();
             }
        });

        $('#tablaAppMovil tbody' ).on('click','.btnEliminarAppMovil',function(){
             if( $('.btnEliminarAppMovil').length > 1) {
                        $(this).parents('tr').remove();
             }
        });

        $("#agregarFilaConfig").click( function () {
            var html = '<hr><div class="row mt-2" >' + $("#filaConfig").html() + '</div>';
            $('#contenidoConfig').append( html );
        });

        $("#checkScript").on('click', function() {
        if( $(this).is(':checked') ){
            $("#contenidoConfigArchivo").show();
            $("#contenidoConfig").hide();
        }else{
            $("#contenidoConfigArchivo").hide();
            $("#contenidoConfig").show();
        }
        });
    // do something
});