describe('Prueba de monkey con cypress click en cualquier lado ', function() {
    it('Monkey and cypress', function() {
	//acceder a la pagina de pruebas
        cy.visit('http://dolibarr-pruebas.herokuapp.com/')
	//llenar campos de inicio sesion
      	cy.get('.login_table').find('input[name="username"]').click().type("admin")
      	cy.get('.login_table').find('input[name="password"]').click().type("123456")
      	cy.get('.login_table').contains('Login').click()

	cy.wait(1000);
        randomClick(10);
	})
})

function randomClick(monkeysLeft) {

    function getRandomInt(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min)) + min;
    };

    var monkeysLeft = monkeysLeft;
    if(monkeysLeft > 0) {
	cy.get( '.tmenu' ).children().then(function($body){
		var randomElement = $body.get(getRandomInt(0, $body.length));
		if(!Cypress.dom.isHidden(randomElement)) {					
			cy.wrap(randomElement).click({force: true});
			monkeysLeft = monkeysLeft - 1;				
		}
		cy.wait(50);
		randomClick( monkeysLeft );
	})
    }   
}
