Feature: Login

Scenario: As user i want to login
  Given I press image button number 1
  Then I press "Acceder a Wikipedia"
  Then I enter "davidaso28" into input field number 1
  Then I enter "123456a" into input field number 2
  Then I press "Acceder"
  Then I should see "Accediendo"
