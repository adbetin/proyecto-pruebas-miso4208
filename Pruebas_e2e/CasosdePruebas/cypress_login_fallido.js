describe('Creacion de tercero logibarr', function() {
    it('Visits los dolibarr and login', function() {
	//acceder a la pagina de pruebas
        cy.visit('http://dolibarr-pruebas.herokuapp.com/')

	//llenar campos de inicio sesion
      	cy.get('.login_table').find('input[name="username"]').click().type("usuarioprueba")
      	cy.get('.login_table').find('input[name="password"]').click().type("claveprueba")
      	cy.get('.login_table').contains('Login').click()

	cy.contains('Bad value for login or password')
	
    })
})
