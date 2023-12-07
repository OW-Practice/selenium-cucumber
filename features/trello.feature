Feature: create board in trello application

Scenario: launch the trello application
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

#  Scenario Outline: creating the board with static data
#    When Click on the "Create" button in home page.
#    Then Validate create form
#    When Click on the "Create board" button in create form
#    Then Validate create board header
#    When Enter board name "<BoardName>"
#    When Click on create button in create board form
#    Then Validate created board name "<BoardName>" is displayed
#    Examples:
#    | BoardName |
#    | Testing1  |
#    | Testing2  |
#  Scenario:
#    When Click on the trello header
#  Scenario Outline: deleting the created board
#    Then Validate the trello header should displayed in home page
#    Then Validate "YOUR WORKSPACES" section header should displayed in trello home page.
#    Then Validate "<CreatedBoardName>" should displayed in yours workspace section
#    When Click on the created board name "<CreatedBoardName>"
#    Then Validate created board name "<CreatedBoardName>" is displayed
#    When Click on the menu show
#    Then Validate menu header is displayed
#    Then Validate close board option is displayed
#    When Click on close board option
#    Then Validate close board pop up is displayed
#    Then Validate "Close board?" close header should displayed in delete pop up.
#    Then Validate "find and reopen closed" close content text should displayed in delete pop up.
#    Then Validate close button is displayed in close board pop up
#    When Click on the close button in close board pop up
#    Then Validate "<CreatedBoardName>" is closed text should displayed in delete page.
#    Then Validate "Reopen board" button is displayed in the Delete boards page.
#    Then Validate "Permanently delete board" link is displayed in the delete boards page.
#    When Click on permanently delete board button
#    Then Validate delete board pop up is displayed
#    Then Validate "Delete board?" header should displayed in delete pop up.
#    Then Validate "cards and actions will be deleted" content text should displayed in delete pop up.
#    Then Validate delete button should displayed in delete pop up.
#    When Click on delete button
#    Then Validate board deleted pop up should displayed in the home page.
#    Then Validate "<CreatedBoardName>" name should not display in your work space section
#    Examples:
#    | CreatedBoardName |
#    | Testing1         |
#    | Testing2         |

  Scenario: creating and deleting randomly board name
    When Click on the "Create" button in home page.
    Then Validate create form
    When Click on the "Create board" button in create form
    Then Validate create board header
    When Enter random board name in create board form
    When Click on create button in create board form
    Then Validate randomly created board name is displayed
    When Click on the trello header
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
    Then Validate the randomly created board names under yours workspace section is displayed
    When Click on the randomly created board name
    Then Validate randomly created board name is displayed
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
    When Click on profile button "Amrutha"
    When Click on "Log out" option in menu bar
    Then Validate "Log out of your Atlassian account" header
    Then Validate "Amrutha Dasireddy" and "amrutha.dasireddy@optimworks.com"
    When Click on log out button
    Then Validate login in link in home page