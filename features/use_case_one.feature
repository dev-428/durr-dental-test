Feature: Successful Login To Dashboard Page

Scenario: Test Login To Dashbord Page
    Given I open VistaSoft Monitor welcome page on my browser
    When I click Login button on the welcome page
    Then I login as user Larry on the login page
    And I click on the LOG-IN button on the login page
    Then I verify I am at the Dashboard page