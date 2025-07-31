Feature: Negative Login Flow Functionality
  Testing login flow with invalid phone number and error handling

  Scenario Outline: Attempting login with invalid phone number
    Given I am on the Negative Login page
    When I open the page and click on the login button
    And I click the phone number input div
    And I enter an invalid phone number "<phone_number>"
    Then I verify the wrong number message
    And I close the error pop-up
    And I click the WhatsApp button

    Examples:
      | phone_number |
      | 12345        |
      | abcdef       |
      | 0000000000   |
