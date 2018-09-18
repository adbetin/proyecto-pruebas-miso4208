Feature: Login feature

  Scenario: As a valid user I can log into my app
    When I press "Siguiente"
    And I enter "testautomaticas@gmail.com" into input field number 1
    And I enter "pruebas20181" into input field number 2
    And I press "Siguiente"
    And I wait for 60 seconds
    Then I should see "Terminado"
