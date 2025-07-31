Feature: Brand Selection Functionality
  Testing brand selection and offer verification flow in the Oral Care section

  Scenario: Selecting Colgate brand and verifying offers
    Given I am on the Brand Selection page
    When I scroll to Browse By section
    And I click on Oral Care
    And I click on Brands filter
    And I select Colgate brand
    And I add the first product to the cart
    And I select the first product
    And I scroll to Available Offers
    Then I verify the Available Offers section
