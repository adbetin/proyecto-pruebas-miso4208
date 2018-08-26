describe('Generar reporte', function() {
    it('Generar reporte', function() {
      cy.visit('http://dolibarr-pruebas.herokuapp.com/index.php')
    //  cy.get('.demothumbtext').first().click({force:true})
      cy.get('.login_table').find('input[id="username"]').click().type("admin")
      cy.get('.login_table').find('input[id="password"]').click().type("123456")
      cy.get('input[type="submit"]').click()
      cy.get('.billing').click({force:true})
      cy.get('.menu_contenu_compta_paiement_rapport').find('a[class="vsmenu"]').click({force:true});
      cy.get('input[value=Create]')

    })
})
