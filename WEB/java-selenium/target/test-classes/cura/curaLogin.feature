Feature: Login

  As a registered User I want to login
  /
  As an unregistered User I should not be able to login.

  Background:
    User navigates to CURA Login
    Given I open CURA Login

  Scenario Outline: User Login
    Given A username <username>
    And A password <password>
    When I fill login form
    Then I should <succeedOrFail>

    Examples:
      | username | password | succeedOrFail |
      | "John Doe" | "ThisIsNotAPassword" | succeed |
      | "Jane Doe" | "ThisIsAPassword" | fail |
