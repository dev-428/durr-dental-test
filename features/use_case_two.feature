Feature: Successful Verification For User Name And email

    Scenario Outline: Login And Navigate To My User Account And Verify Name And email
        Given I open VistaSoft Monitor welcome page on my browser
        When I click Login button on the welcome page
        Then I fill my email and password on the login page
        And I click on the LOG-IN button on the login page
        Then I click on User Profile button on the left menu component
        And I click on My user account button on the User Profile pop up
        Then I verify I am at the My user account page
        And I verify my first name is "<firstName>" and last name is "<lastName>" at My user account page
        AND I verify my "<email>" at My user account page

    Examples:
        | firstName | lastName | email |
        | Larry | Lim | larrydev428@gmail.com |