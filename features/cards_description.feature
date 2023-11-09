@description
Feature: create board in trello application

  Scenario: launch the trello application and validate trello home page
    Given Launch the trello application
    Then Validate trello logo
    When Click on log in link
    Then Validate login form
    When Enter username
    When Click on continue button
    When Enter password
    When Click on log in button
    Then Validate the trello header should displayed in home page
    When Click on profile button "Amrutha"
    Then Validate username "Amrutha Dasireddy"

  Scenario: add and edit description, attaching image for description for cards and verification
    When Click on the "Create" button in home page.
    Then Validate create form
    When Click on the "Create board" button in create form
    Then Validate create board header
    When Enter random board name in create board form
    When Click on create button in create board form
    Then Validate randomly created board name is displayed
    When Create list title "1" and validate list name
    When Create card with list size "1" and card size "1" and enter card name
    Then Validate cards based on list size "1" and card size "1"
    When Click on the card name "1" "1" add "Description" and "Save" in the card details form
    When Click on edit "Edit" update the description save "Save" list size "1" card size "1"
    When Click on the attachment of card "1" "1" and upload imgage
    Then Validate attached image to card "1" "1"