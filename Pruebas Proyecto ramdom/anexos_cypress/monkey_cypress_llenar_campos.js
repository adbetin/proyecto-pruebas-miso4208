describe('Prueba de monkey con cypress llenar campos ', function() {
    it('Monkey and cypress', function() {
	//acceder a la pagina de pruebas
        cy.visit('http://dolibarr-pruebas.herokuapp.com/')
	//llenar campos de inicio sesion
      	cy.get('.login_table').find('input[name="username"]').click().type("admin")
      	cy.get('.login_table').find('input[name="password"]').click().type("123456")
      	cy.get('.login_table').contains('Login').click()
	
	cy.get('.tmenudiv').find('#mainmenutd_companies').click()
	cy.get('.blockvmenu.blockvmenupair.blockvmenufirst:first').contains('New Third Party').click()

	cy.wait(1000);
        randomLlenar(20);
	})
})


function randomLlenar(monkeysLeft) {

    function getRandomInt(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min)) + min;
    };

	function randomString(len) {
	    var charSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
	    var randomString = '';
	    for (var i = 0; i < len; i++) {
		var randomPoz = Math.floor(Math.random() * charSet.length);
		randomString += charSet.substring(randomPoz,randomPoz+1);
	    }
	    return randomString;
	}

    var monkeysLeft = monkeysLeft;
    if(monkeysLeft > 0) {
	cy.get( '.tabBar.tabBarWithBottom' ).children().then(function($body){
		var lenght = $body.find('input[type=text]').length
		var randomElement = $body.find('input[type=text]').eq( getRandomInt(0 , lenght ) );
		if(!Cypress.dom.isHidden(randomElement)) {					
			cy.wrap(randomElement).click({force: true}).type( randomString(20) );
			monkeysLeft = monkeysLeft - 1;				
		}			
		cy.wait(50);
		randomLlenar( monkeysLeft );
	})
    }    
}
