# Created by abidahmad at 7/18/23
Feature: Feature: Test for Main page feature

  Scenario: User can access Search by Product page
    Given Open main page
    When Click on Shop by product button
    When Click Sunscreen
    When Open the first product in search
    Then Verify the fist product in Sunscreen