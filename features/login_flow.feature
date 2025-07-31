Feature: Login Flow Functionality
  Testing login flow including phone number entry and OTP submission

  Scenario Outline: Logging in with phone number and OTP
    Given I am on the Login page
    When I click on the login button
    And I click the phone number input section
    And I enter the phone number "<phone_number>"
    And I click the submit button
    And I enter the OTP "<otp>"
    Then I click the final submit button

    Examples:
      | phone_number | otp     |
      | 7386081569   | 123456  |
      | 7386081569   | 000000  |
      | 7386081569   | aks098  |
