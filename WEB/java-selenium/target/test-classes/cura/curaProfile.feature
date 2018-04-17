Feature: Profile

  As a registered User I want to see my Profile Page.

  Background:
    User navigates to CURA Login and User log in
    Given I open CURA Login
    And A username "John Doe"
    And A password "ThisIsNotAPassword"
    And I fill login form
    And I should succeed

  Scenario: Logged in User's Profile
    When I open CURA Profile
    Then I should see my profile
