# Created by adrian at 15/04/2018
Feature: CURA Profile
  # Enter feature description here

  Scenario: User Profile
    Given A valid User
    When I go to Login page
    And I enter User credentials
    And I go to Profile page
    Then I should see my Profile
