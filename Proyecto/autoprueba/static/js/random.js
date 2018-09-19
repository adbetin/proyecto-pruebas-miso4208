$( document ).ready(function() {

    $("#ejecutar").click( function () {

        alert( $('#app').select() );
        $.ajax({
          type: "POST",
          url: "/tester_android/",
          data: { cantidadEvento : 10 , appp : $('#app').select() },
          dataType: 'html',
          success: function ( data ) {
              alert( data ,"Ingreso aca");
          },
          error : function ( error ) {
              alert( error );
          }
        });
    });

});