Feature: Product Category Navigation
  Testing footer navigation, window switch, and product category flow

  Scenario: Navigating to Baby Food category via footer
    Given I am on the Product Category page
    When I scroll to the footer section
    And I click on the Formula link
    And I switch to the newly opened window
    And I hover over the Infant category
    And I click on the Baby Food category
    And I scroll to the Read Section
    Then I click on View All
