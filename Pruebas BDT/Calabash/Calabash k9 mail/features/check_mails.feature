Feature: check mails

  Scenario: As a user i want find my mails
    When I press "Siguiente"
    And I enter "testautomaticas@gmail.com" into input field number 1
    And I enter "pruebas20181" into input field number 2
    And I press "Siguiente"
    And I wait for 60 seconds
    And I enter "Pruebas" into input field number 1
    And I enter "Test" into input field number 2
    And I press "Terminado"
    And I press "Aceptar"
    And I press "Aceptar"
    And I press "Pruebas"
    Then I should see "Entrada"
