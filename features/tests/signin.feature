# Created by jle@sitetracker.com at 11/5/23
Feature: SignIn Tests

  Scenario: User can open SignIn page
    Given Open target main page
    When Click Sign In
    And From right wide navigation menu, click Sign In
    Then Verify Sign In form opened