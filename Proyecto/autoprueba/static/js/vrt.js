$( document ).ready(function() {

    $("#agregarFila").click( function () {
        var html = '<hr><div class="row mt-2" >' + $("#fila").html() + '</div>';
        $('#contenido').append( html );
    });

    $("#ejecutarVrtCypress").click( function(){
        location.href = "/vrt/resemble"
    });

    $("#btn_compare").click( function(){
        $('#img_vrt').attr("src","../../static/data/vrt/cypress/dolibar/listaterceros(1).png")
        $('#resultado_img').attr("src","../../static/data/vrt/resemble/diff_listaterceros.png")
        $('#fechavrt').html("2018-13-05")
    });


});