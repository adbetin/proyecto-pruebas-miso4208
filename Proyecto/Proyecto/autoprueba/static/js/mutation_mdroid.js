$(function () {
    $("#execute").click( function (e) {
        e.preventDefault();
        var editor = ace.edit("javascript_editor");
        var code_content = editor.getValue();

        var application = $("#application").val();
        var multithread = $("#multithread").val();

        $.ajax({
          type: "POST",
          url: upload_file_url,
          data: {
              code_content : code_content,
              application: application,
              multithread : multithread,
              csrfmiddlewaretoken : csrf_token
          },
          dataType: 'html',
          success: function ( data ) {
              console.log("Ejecutado correctamente", data);
              alert("Se le enviará un correo al finalizar el análisis de la suite de pruebas");
          },
          error : function ( error ) {
              alert( 'Error al ejecutar el script' );
          }
        });
    });

});