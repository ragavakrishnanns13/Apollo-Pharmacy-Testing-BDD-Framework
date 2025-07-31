Feature: Product Search Flow
  Testing product search, selection, variant change, and cart flow

  Scenario Outline: Searching and adding a product to cart
    Given I am on the Search page
    When I search for the product "<product_name>"
    And I select the first product from results
    And I change the product variant
    And I scroll and add the product to cart
    And I view the cart
    Then I scroll to Last Minute Buys section

    Examples:
      | product_name         |
      | Nivea Under Arm Men |
