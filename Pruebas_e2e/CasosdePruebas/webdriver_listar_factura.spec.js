var assert = require('assert');
describe('Dolibarr ', function() {
    it('Listar facturas ', function () {
		
        browser.url('http://dolibarr-pruebas.herokuapp.com/index.php');        			
        browser.waitForVisible('#login_line2', 10000);	
		browser.element('input[id="username"]').click().keys('admin');
		browser.element('input[id="password"]').click().keys('123456');
        browser.click('input[type="submit"]');
		browser.waitForVisible('#mainmenua_billing', 10000);	
		browser.click('#mainmenua_billing');
		browser.waitForVisible('.menu_contenu_compta_facture_list', 10000);
		var menu = browser.element('.menu_contenu_compta_facture_list');		
		menu.click('a[class="vsmenu"]');			
    });
});
