Feature: Product Selection Functionality
  Testing product selection and cart verification flow

  Scenario: Selecting Pampers and verifying cart
    Given I am on the Product Selection page
    When I click on the Offers section
    And I scroll to the product section
    And I select Pampers product
    And I add the product to the cart
    And I click on the cart icon
    Then I verify the cart page
