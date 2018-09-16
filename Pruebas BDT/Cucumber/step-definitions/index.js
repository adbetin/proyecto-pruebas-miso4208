//Complete siguiendo las instrucciones del taller

var {defineSupportCode} = require('cucumber');
var {expect} = require('chai');

defineSupportCode(({Given, When, Then}) => {
		
	When(/^I fill with (.*) and (.*)$/ , (user, password) => {				
		browser.element('input[id="username"]').click().keys( user );
		browser.element('input[id="password"]').click().keys( password );
		
	});

	  Given('I go to dolibar home screen', () => {
		browser.url('http://dolibarr-pruebas.herokuapp.com/index.php?mainmenu=home&leftmenu=home');   
	  });

	  When('I open the login screen', () => {
		browser.waitForVisible('#login_line2', 10000);	
	  });
	 
	 When('I go to detalletercero', () => {
		//browser.waitForVisible('#login_line2', 10000);	
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
	  
	  When('I go to listaterceros', () => {
		//browser.waitForVisible('#login_line2', 10000);	
		browser.waitForVisible('#mainmenutd_companies', 10000);	
		browser.click('#mainmenutd_companies');
		browser.waitForVisible('.menu_contenu_societe_list', 10000);
		var menu = browser.element('.menu_contenu_societe_list');				
	  });

	  When('I try to login', () => {
		browser.click('input[type="submit"]');
	  });

	  Then('I expect to see {string}', msg => {
		//browser.waitForVisible('.aviso.alert.alert-danger', 5000);
	  });
});
