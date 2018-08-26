describe('Creacion de tercero logibarr', function() {
    it('Visits los dolibarr and login', function() {
	//acceder a la pagina de pruebas
        cy.visit('http://dolibarr-pruebas.herokuapp.com/')

	//llenar campos de inicio sesion
      	cy.get('.login_table').find('input[name="username"]').click().type("admin")
      	cy.get('.login_table').find('input[name="password"]').click().type("123456")
      	cy.get('.login_table').contains('Login').click()

	cy.get('.tmenudiv').find('#mainmenutd_companies').click()
	cy.get('.blockvmenu.blockvmenupair.blockvmenufirst:first').contains('New Third Party').click()

	//se llenan los campos relacionados con el tercero
	cy.get('.tabBar.tabBarWithBottom').find('input[name="name"]').click({ force: true }).type("Test Tercero")
	cy.get('.tabBar.tabBarWithBottom').find('input[name="name_alias"]').click({ force: true }).type("Alias Test Tercero")
	cy.get('.tabBar.tabBarWithBottom').find('select[name="client"]').select("Customer", { force: true })
	cy.get('.tabBar.tabBarWithBottom').find('select[name="fournisseur"]').select("Yes", { force: true })
	cy.get('.tabBar.tabBarWithBottom').find('textarea[name="address"]').click({ force: true }).type("Direccion Test Tercero")
	cy.get('.tabBar.tabBarWithBottom').find('input[name="email"]').click({ force: true }).type("email@tercero.com")
	cy.get('.tabBar.tabBarWithBottom').find('input[name="phone"]').click({ force: true }).type("1234567")
	cy.get('.center').find('input[name="create"]').click({ force: true })
    })
})
