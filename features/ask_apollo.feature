Feature: Ask Apollo Functionality
  Testing the banner interaction and doctor consultation flow on Ask Apollo

  Scenario: Interacting with Ask Apollo and booking consultation
    Given I am on the Ask Apollo homepage
    When I scroll and click the banner
    And I click on doctor
    And I select the first option
    And I scroll and click Book Now
    And I click on Consult Online
