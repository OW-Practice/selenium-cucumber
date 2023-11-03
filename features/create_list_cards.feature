@smoke
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

  Scenario:Create board and lists and cards under each board and validating board, lists, cards
    Then Validate the trello header should displayed in home page
    Then Validate "YOUR WORKSPACES" section header should displayed in trello home page.
    Then Validate work space section should displayed in trello home page.
    Then Validate work space menu options should display
      | menu_options |
      | Boards       |
      | Highlights   |
      | Views        |
      | Members      |
      | Settings     |
    When Click on the "Create" button in home page.
    Then Validate create form
    When Click on the "Create board" button in create form
    Then Validate create board header
    When Enter random board name in create board form
    When Click on create button in create board form
    Then Validate randomly created board name is displayed
    When Create list title "2" and validate list name
    When Create card with list size "2" and card size "3" and enter card name
    Then Validate cards based on list size "2" and card size "3"
    When Click on the menu show
    Then Validate menu header is displayed
    Then Validate close board option is displayed
    When Click on close board option
    Then Validate close board pop up is displayed
    Then Validate "Close board?" close header should displayed in delete pop up.
    Then Validate "find and reopen closed" close content text should displayed in delete pop up.
    Then Validate close button is displayed in close board pop up
    When Click on the close button in close board pop up
    Then Validate randomly board name is closed text is displayed in the delete board page
    Then Validate "Reopen board" button is displayed in the Delete boards page.
    Then Validate "Permanently delete board" link is displayed in the delete boards page.
    When Click on permanently delete board button
    Then Validate delete board pop up is displayed
    Then Validate "Delete board?" header should displayed in delete pop up.
    Then Validate "cards and actions will be deleted" content text should displayed in delete pop up.
    Then Validate delete button should displayed in delete pop up.
    When Click on delete button
    Then Validate board deleted pop up should displayed in the home page.
    Then Validate delete random board name should not display in your work space section

  Scenario: deleting the cards and lists in the board
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
    When Click on the card name "1"  and "1" and add "Description" and "this card is created by faker" in the card details form
    When Click on the card and delete "2" and "2" and "Delete card?" and "All actions will be removed"
    When Click on the list menu list size "2" and archive this list "Archive this list"
      | headers           |
      | List actions      |
      | Archive this list |
    Then Validate deleted lists list size "2" in the board
    When Click on the menu show
    Then Validate menu header is displayed
    Then Validate close board option is displayed
    When Click on close board option
    Then Validate close board pop up is displayed
    Then Validate "Close board?" close header should displayed in delete pop up.
    Then Validate "find and reopen closed" close content text should displayed in delete pop up.
    Then Validate close button is displayed in close board pop up
    When Click on the close button in close board pop up
    Then Validate randomly board name is closed text is displayed in the delete board page
    Then Validate "Reopen board" button is displayed in the Delete boards page.
    Then Validate "Permanently delete board" link is displayed in the delete boards page.
    When Click on permanently delete board button
    Then Validate delete board pop up is displayed
    Then Validate "Delete board?" header should displayed in delete pop up.
    Then Validate "cards and actions will be deleted" content text should displayed in delete pop up.
    Then Validate delete button should displayed in delete pop up.
    When Click on delete button
    Then Validate board deleted pop up should displayed in the home page.
    Then Validate delete random board name should not display in your work space section
