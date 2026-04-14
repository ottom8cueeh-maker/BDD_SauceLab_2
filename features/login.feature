# Acceptance Criteria

Feature: User Login
  As a registered user
  I want to log in to the application
  So that I can access my account

  Background:
    Given I navigate to the login page, which is the base_url (see conftest.py)

  Scenario: Successful login with valid credentials
    When I enter username "standard_user" and password "secret_sauce"
    And I click the login button
    Then I should be redirected to the dashboard
    And I should see the main menu on the left side

  Scenario: Failed login with invalid password
    When I enter username "standard_user" and password "wrongpassword"
    And I click the login button
    Then I should see an error message "Invalid credentials"
    And I should remain on the login page

  Scenario: Failed login with invalid username
    When I enter username "bad_username" and password "secret_sauce"
    And I click the login button
    Then I should see an error message "Invalid credentials"
    And I should remain on the login page

  Scenario: Login form validation — empty fields
    When I click the login button without entering credentials
    Then I should see no error displayed
    And I should remain on the login page
