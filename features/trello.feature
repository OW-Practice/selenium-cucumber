Feature: create board in trello application

  Scenario: launch the trello application
    Given Launch the trello application
    Then Validate trello logo
#    Then Validate all menus are display
#      | menu_names |
#      | Features   |
#      | Solutions  |
#      | Plans      |
#      | Pricing    |
#      | Resources  |
    When Click on log in link
    Then Validate login form
    When Enter username
    When Click on continue button
    When Enter password
    When Click on log in button
    Then Validate the trello header is displayed
    When Click on profile button "Amrutha"
    Then Validate username "Amrutha Dasireddy"

  Scenario Outline: creating the board with static data
    When Click on create button "Create"
    Then Validate create form
    When Click on create board button "Create board"
    Then Validate create board header
    When Enter board name "<BoardName>"
    When Click on create button
    Then Validate created board name "<BoardName>" is displayed
    Examples:
    | BoardName |
    | Testing1  |
    | Testing2  |
  Scenario:
    When Click on the trello header
  Scenario Outline: deleting the created board
    Then Validate the trello header is displayed
    Then Validate the yours workspace section header "YOUR WORKSPACES" is displayed
    Then Validate the created board names under yours workspace section "<CreatedBoardName>" is displayed
    When Click on the created board name "<CreatedBoardName>"
    Then Validate created board name "<CreatedBoardName>" is displayed
    When Click on the menu show
    Then Validate menu header is displayed
    Then Validate close board option is displayed
    When Click on close board option
    Then Validate close board pop up is displayed
    Then Validate close board header "Close board?" is displayed
    Then Validate close board content "find and reopen closed" is displayed
    Then Validate close button is displayed
    When Click on the close button
    Then Validate board name is closed text "<CreatedBoardName>" is displayed
    Then Validate re open board button "Reopen board" is displayed
    Then Validate permanently delete board button "Permanently delete board" is displayed
    When Click on permanently delete board button
    Then Validate delete board pop up is displayed
    Then Validate delete board header "Delete board?" is displayed
    Then Validate delete board content "cards and actions will be deleted" is displayed
    Then Validate delete button is displayed
    When Click on delete button
    Then Validate board deleted pop up is displayed
    Then Validate delete board name "<CreatedBoardName>" in your work space section
    Examples:
    | CreatedBoardName |
    | Testing1         |
    | Testing2         |
#  @faker
  Scenario: creating and deleting randomly board name
    When Click on create button "Create"
    Then Validate create form
    When Click on create board button "Create board"
    Then Validate create board header
    When Enter random board name
    When Click on create button
    Then Validate randomly created board name is displayed
    When Click on the trello header
    Then Validate the trello header is displayed
    Then Validate the yours workspace section header "YOUR WORKSPACES" is displayed
    Then Validate work space section is displayed
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
    Then Validate close board header "Close board?" is displayed
    Then Validate close board content "find and reopen closed" is displayed
    Then Validate close button is displayed
    When Click on the close button
    Then Validate randomly board name is closed text is displayed
    Then Validate re open board button "Reopen board" is displayed
    Then Validate permanently delete board button "Permanently delete board" is displayed
    When Click on permanently delete board button
    Then Validate delete board pop up is displayed
    Then Validate delete board header "Delete board?" is displayed
    Then Validate delete board content "cards and actions will be deleted" is displayed
    Then Validate delete button is displayed
    When Click on delete button
    Then Validate board deleted pop up is displayed
    Then Validate delete random board name in your work space section
















