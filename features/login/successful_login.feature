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
