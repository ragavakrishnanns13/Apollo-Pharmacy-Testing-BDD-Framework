Feature: Doctor Appointment Functionality
  Testing doctor appointment flow and error handling for invalid phone number

  Scenario Outline: Booking a doctor appointment with invalid phone number
    Given I am on the Doctor Appointment page
    When I click on Doctor Appointment section
    And I select Neurology specialty
    And I sort doctors by Relevance
    And I sort doctors by Experience
    And I click on Consult
    And I click on Continue
    And I enter phone number "<phone_number>"
    Then I verify the error message for invalid phone number

    Examples:
      | phone_number |
      | 12345        |
      | abcdef       |
      | 7386081569   |
