Feature: Circle page UI tests

  Scenario: There are 5 benefit boxes
    Given Open target circle page
    Then Verify benefit box is present
    And Verify benefit box has 5 links