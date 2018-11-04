/* ------------------------------------------------------------------------------
 *
 *  # Ace code editor
 *
 *  Demo JS code for editor_code.html page
 *
 * ---------------------------------------------------------------------------- */


// Setup module
// ------------------------------

var Ace = function() {


    //
    // Setup module components
    //

    // Ace editor
    var _componentAce = function() {
        if (typeof ace == 'undefined') {
            console.warn('Warning - ace.js is not loaded.');
            return;
        }

        // Javascript editor
        var js_editor = ace.edit('javascript_editor');
            js_editor.setTheme('ace/theme/monokai');
            js_editor.getSession().setMode('ace/mode/javascript');
            js_editor.setShowPrintMargin(false);
    };


    //
    // Return objects assigned to module
    //

    return {
        init: function() {
            _componentAce();
        }
    }
}();


// Initialize module
// ------------------------------

document.addEventListener('DOMContentLoaded', function() {
    Ace.init();
});
