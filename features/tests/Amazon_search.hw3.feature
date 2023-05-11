# Created by abidahmad at 5/9/23
Feature: Amazon Search tests


  Scenario: user can search on Amazon
    Given Open Amazon main page
    When search for cart
    Then verify search results shown

