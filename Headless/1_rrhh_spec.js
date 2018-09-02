describe('Login', function() {
    it('Visita el login', function() {
        cy.visit('http://dolibarr-pruebas.herokuapp.com/index.php')
      cy.get('.login_table').find('input[id="username"]').click().type("admin")
      cy.get('.login_table').find('input[id="password"]').click().type("123456")
      cy.get('input[type="submit"]').click()
      cy.contains('SuperAdmin')
    })
})

