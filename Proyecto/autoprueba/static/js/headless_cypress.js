$(function () {
    $("#execute").click( function (e) {
        e.preventDefault();
        var editor = ace.edit("javascript_editor");
        var code_content = editor.getValue();

        $.ajax({
          type: "POST",
          url: upload_file_url,
          data: { code_content : code_content , csrfmiddlewaretoken : csrf_token },
          dataType: 'html',
          success: function ( data ) {
              console.log("Ejecutado correctamente", data);
              alert( data ,"Ejecutado correctamente");
          },
          error : function ( error ) {
              alert( error );
          }
        });
    });

});