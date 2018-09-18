Feature: Search content

Scenario: As user i want to search colombia
  Given I press image button number 1
  Then I enter "Colombia" into input field number 1
  Then I should see "País de América del Sur"

Scenario: As user i want to search colombia
    Given I press image button number 1
    Then I enter "android" into input field number 1
    Then I should see "Sistema operativo"
