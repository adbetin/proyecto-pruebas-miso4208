/*describe('Login', function() {
    it('Visita el login', function() {
        cy.visit('http://dolibarr-pruebas.herokuapp.com/index.php')
      cy.get('.login_table').find('input[id="username"]').click().type("admin")
      cy.get('.login_table').find('input[id="password"]').click().type("123456")
      cy.get('input[type="submit"]').click()
      cy.contains('SuperAdmin')
    })
})*/
describe('Crear factura', function() {
    it('Crear factura', function() {
      cy.visit('http://dolibarr-pruebas.herokuapp.com/index.php')
    //  cy.get('.demothumbtext').first().click({force:true})
    cy.get('.login_table').find('input[id="username"]').click().type("admin")
    cy.get('.login_table').find('input[id="password"]').click().type("123456")
      cy.get('input[type="submit"]').click()
      cy.get('.billing').click({force:true})
      cy.get('.menu_contenu_compta_facture_card').find('a[class="vsmenu"]').click({force:true});
      cy.wait(4000)
      cy.get('.ui-autocomplete-input').click({force:true}).type("pr")
      cy.wait(4000)
      cy.get('li[class="ui-menu-item"]').first().click()
      cy.get('button[id="reButtonNow"]').click({force:true})
      cy.get('select[id="selectmode_reglement_id"]').select("4",{force:true})
      cy.get('.center').find('input[type="submit"]').click()
    })
})
