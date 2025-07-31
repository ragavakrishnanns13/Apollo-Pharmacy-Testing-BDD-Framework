Feature: Apollo Products Functionality
  Testing the product selection and checkout flow on Apollo Pharmacy

  Scenario: Product selection and checkout
    Given I am on the Apollo Pharmacy homepage
    When I hover over Apollo Products
    And I select ORS Drinks
    And I sort products by price
    And I add a product to cart
    And I click on the view the cart option
    And I change the quantity to 5
    And I proceed to checkout

