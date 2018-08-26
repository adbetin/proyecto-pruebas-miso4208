describe('Creacion de tercero logibarr', function() {
    it('Visits los dolibarr and login', function() {
	//acceder a la pagina de pruebas
        cy.visit('http://dolibarr-pruebas.herokuapp.com/')

	//llenar campos de inicio sesion
      	cy.get('.login_table').find('input[name="username"]').click().type("admin")
      	cy.get('.login_table').find('input[name="password"]').click().type("123456")
      	cy.get('.login_table').contains('Login').click()
	})
})
