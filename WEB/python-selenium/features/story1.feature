# Created by adrian at 15/04/2018
Feature: CURA Login
  # Enter feature description here

  Scenario: Valid User Login
    Given A valid User
    When I go to Login page
    And I enter User credentials
    Then I should be logged in

  Scenario: Invalid User Login
    Given An invalid User
    When I go to Login page
    And I enter User credentials
    Then I should not be logged in
