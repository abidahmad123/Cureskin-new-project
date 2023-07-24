# Created by abidahmad at 7/24/23
Feature: cureskin search result test cases

  Scenario: Search results shows the right result
    Given Open Main page
    When From Header Page, click "Search"
    And Search for SPF
    Then Verify the results have spfe