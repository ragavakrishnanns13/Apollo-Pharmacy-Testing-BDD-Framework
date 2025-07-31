Feature: Discount Navigation Functionality
  Testing discount section navigation and product addition flow

  Scenario Outline: Navigating discount section and adding products
    Given I am on the Discount page
    When I click on Discount section
    And I scroll to Category section
    And I click on Home category
    And I scroll to Add button section
    And I click Add buttons with stock "<stock>"

    Examples:
      | stock  |
      | True   |
      | False  |
