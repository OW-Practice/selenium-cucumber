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

  Scenario: create card from template
    When Click on the "Create" button in home page.
    Then Validate create form
    When Click on the "Create board" button in create form
    Then Validate create board header
    When Enter random board name in create board form
    When Click on create button in create board form
    Then Validate randomly created board name is displayed
    When Create list title "1" and validate list name
    When Click on "Card templates" add template
    Then Validate template name in form
    When Click on create card button and verify "Create card from template" form
    Then Validate card name
    When Click on create card button
    When Click on template card name under list
    When Click on hide from list button
    Then Validate card name under list

