Feature: Amazon Search tests


  Scenario: user can search on Amazon
    Given Open Amazon main page
    When Search for cart
    Then Verify search results shown