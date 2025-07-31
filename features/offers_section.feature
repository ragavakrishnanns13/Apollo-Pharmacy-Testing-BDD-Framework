Feature: Offers Section Functionality
  Testing product sorting and cart flow from the offers section

  Scenario: Navigating offers and adding product to cart
    Given I am on the Offers page
    When I click on the Offers icon
    And I scroll to the product section of the home page
    Then I verify the Deals by Category section
    When I select Home Essentials category
    And I sort products by price from low to high
    And I add a product to the cart
    Then I view the cart
