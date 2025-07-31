Feature: Diabetic Care Functionality
  Testing diabetic care product selection and login flow

  Scenario Outline: Selecting diabetic care product and logging in
    Given I am on the Diabetic Care page
    When I scroll to the Health section
    And I click on Diabetic Care
    And I select the first diabetic product
    And I click on Login
    And I enter primary phone number "<phone_number>"

    Examples:
      | phone_number |
      | 7386081569   |
