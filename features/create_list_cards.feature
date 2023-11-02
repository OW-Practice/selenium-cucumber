@smoke
Feature: create board in trello application

  Background: : launch the trello application and validate trello home page
    Given Launch the trello application
    Then Validate trello logo
    When Click on log in link
    Then Validate login form
    When Enter username
    When Click on continue button
    When Enter password
    When Click on log in button
    Then Validate the trello header is displayed
    When Click on profile button "Amrutha"
    Then Validate username "Amrutha Dasireddy"

#  Scenario:Create board and lists and cards under each board and validating board, lists, cards
#    Then Validate the trello header is displayed
#    Then Validate the yours workspace section header "YOUR WORKSPACES" is displayed
#    Then Validate work space section is displayed
#    Then Validate work space menu options should display
#      | menu_options |
#      | Boards       |
#      | Highlights   |
#      | Views        |
#      | Members      |
#      | Settings     |
#    When Click on create button "Create"
#    Then Validate create form
#    When Click on create board button "Create board"
#    Then Validate create board header
#    When Enter random board name
#    When Click on create button
#    Then Validate randomly created board name is displayed
#    When Create list title "2" and validate list name
#    When Create card with list size "2" and card size "3" and enter card name
#    Then Validate cards based on list size "2" and card size "3"
#    When Click on the menu show
#    Then Validate menu header is displayed
#    Then Validate close board option is displayed
#    When Click on close board option
#    Then Validate close board pop up is displayed
#    Then Validate close board header "Close board?" is displayed
#    Then Validate close board content "find and reopen closed" is displayed
#    Then Validate close button is displayed
#    When Click on the close button
#    Then Validate randomly board name is closed text is displayed
#    Then Validate re open board button "Reopen board" is displayed
#    Then Validate permanently delete board button "Permanently delete board" is displayed
#    When Click on permanently delete board button
#    Then Validate delete board pop up is displayed
#    Then Validate delete board header "Delete board?" is displayed
#    Then Validate delete board content "cards and actions will be deleted" is displayed
#    Then Validate delete button is displayed
#    When Click on delete button
#    Then Validate board deleted pop up is displayed
#    Then Validate delete random board name in your work space section




