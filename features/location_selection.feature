Feature: Location Selection Functionality
  Testing location selection and pharmacy navigation flow

  Scenario Outline: Selecting a location and navigating to pharmacy
    Given I am on the Location Selection page
    When I click on the address section
    And I choose a different location
    And I enter the location "<location>"
    And I select Hosur from suggestions
    And I click on Pharmacy Near Me
    Then I enter full screen mode

    Examples:
      | location |
      | Hosur    |
