# Created by abidahmad at 5/9/23
Feature: Amazon Search tests


  Scenario: user can search on Amazon
    Given Open Amazon main page
    When Search for Best Sellers
    Then Verify search results shown


