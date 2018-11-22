$( document ).ready(function() {

    $("#ejecutar").click( function () {

        var numEvent = $('#numEvent').val() == "" ? 100 : $('#numEvent').val();
        var package = $('#app').select().val() == "" ? 100 : $('#app').select().val() ;

        $.ajax({
          type: "GET",
          url: "/tester_android/"+numEvent+"/"+package,

          dataType: 'html',
          success: function ( data ) {
              alert( "Prueba realizada");
          },
          error : function ( error ) {
              alert( error );
          }
        });

           });


});