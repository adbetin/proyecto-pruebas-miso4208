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
        cy.get('div').then($links => {
            var randomLink = $links.get(getRandomInt(0, $links.length));
            if(!Cypress.dom.isHidden(randomLink)) {
                cy.wrap(randomLink).click({force: true});
                monkeysLeft = monkeysLeft - 1;		
            }
            //setTimeout(randomClick, 1000, monkeysLeft);
		cy.wait(10);
		randomClick( monkeysLeft );
        });


    }   
}
