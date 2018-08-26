var assert = require('assert');
describe('Dolibarr ', function() {
    it('Listar terceros ', function () {
		
        browser.url('http://dolibarr-pruebas.herokuapp.com/index.php');        			
        browser.waitForVisible('#login_line2', 10000);	
		browser.element('input[id="username"]').click().keys('admin');
		browser.element('input[id="password"]').click().keys('123456');
        browser.click('input[type="submit"]');
		browser.waitForVisible('#mainmenutd_companies', 10000);	
		browser.click('#mainmenutd_companies');
		browser.waitForVisible('.menu_contenu_societe_list', 10000);
		var menu = browser.element('.menu_contenu_societe_list');		
		menu.click('a[class="vsmenu"]');					
		browser.waitForVisible('.tagtable', 10000);		
		var table = browser.element('.tagtable'); 
		var td = table.element( ".tdoverflowmax200:nth-child(1)" );	
		td.click('a:nth-child(1)');
    });
});
