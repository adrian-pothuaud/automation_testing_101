Feature: Appointment

  As a registered User I want to create an Appointment.

  Scenario Outline: Appointment Creation
    Given I open CURA Login
    And A username <username>
    And A password <password>
    When I fill login form
    And I open appointment form
    And I choose facility <facility>
    And I <doornot> select apply for readmission
    And I choose healthcare program <program>
    And I choose visit date <date>
    And I write comment <comment>
    And I submit appointment
    Then My appointment is created
    And I can see 1 element in my history

    Examples:
    | username   | password             | facility                           | doornot | program    | date         | comment        |
    | "John Doe" | "ThisIsNotAPassword" | "Tokyo CURA Healthcare Center"     | do      | "medicaid" | "21-03-2019" | "auto comment" |
    | "John Doe" | "ThisIsNotAPassword" | "Hongkong CURA Healthcare Centerr" | do not  | "medicare" | "21-03-2021" | "comment"      |
