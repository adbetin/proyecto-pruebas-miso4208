#Complete siguiendo las instrucciones del taller.

Feature: Dolibar web
    Acciones registradas en el plan de pruebas


Scenario Outline: Login correcto

  Given I go to dolibar home screen
    When I open the login screen
    And I fill with <user> and <password>
    And I try to login
    Then I expect to see <msg>

    Examples:
      | user            | password | msg        |
      | admin           | 123456   | Acceso correcto!   |
	  
Scenario Outline: Lista de tercero

  Given  I go to listaterceros
    Then I expect to see <msg>

    Examples:
      | msg        |
      | Lista de tercero  |
	  	 
Scenario Outline: Ver detalle de tercero

  Given  I go to detalletercero
    Then I expect to see <msg>

    Examples:
      | msg        |
      | Ver detalle de tercero  |	  