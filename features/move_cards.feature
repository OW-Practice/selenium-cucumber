Feature: create board in trello application

  Background: launch the trello application and validate trello home page
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

  Scenario: moving cards to another list in same board
    When Click on the "Create" button in home page.
    Then Validate create form
    When Click on the "Create board" button in create form
    Then Validate create board header
    When Enter random board name in create board form
    When Click on create button in create board form
    Then Validate randomly created board name is displayed
    When Create list title "2" and validate list name
    When Create card with list size "1" and card size "2" and enter card name
    Then Validate cards based on list size "1" and card size "2"
    When Click on card name "2" and "Move card" to list
    Then Validate card names "2" in new list
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

  Scenario: moving cards from one board to another board
    When Click on the "Create" button in home page.
    Then Validate create form
    When Click on the "Create board" button in create form
    Then Validate create board header
    When Enter 1st board name in create board form
    When Click on create button in create board form
    When Create list name "1" and validate list name
    When Click on add board icon
    When Enter 2nd board name in create board form
    When Click on create button in create board form
    When Create list title "1" and validate list name
    When Create card with list size "1" and card size "2" and enter card name
    Then Validate cards based on list size "1" and card size "2"
    When Click on card name "2" and "Move card" to list in another board
    When Click on board name
    Then Validate card names "2" in list of another board
    When Click on the menu show
    Then Validate menu header is displayed
    Then Validate close board option is displayed
    When Click on close board option
    Then Validate close board pop up is displayed
    Then Validate "Close board?" close header should displayed in delete pop up.
    Then Validate "find and reopen closed" close content text should displayed in delete pop up.
    Then Validate close button is displayed in close board pop up
    When Click on the close button in close board pop up
    Then Validate board name is closed text is displayed in the delete board page
    Then Validate "Reopen board" button is displayed in the Delete boards page.
    Then Validate "Permanently delete board" link is displayed in the delete boards page.
    When Click on permanently delete board button
    Then Validate delete board pop up is displayed
    Then Validate "Delete board?" header should displayed in delete pop up.
    Then Validate "cards and actions will be deleted" content text should displayed in delete pop up.
    Then Validate delete button should displayed in delete pop up.
    When Click on delete button
    Then Validate board deleted pop up should displayed in the home page.
    Then Validate delete board name should not display in your work space section
    When Click on profile button "Amrutha"
    When Click on "Log out" option in menu bar
    Then Validate "Log out of your Atlassian account" header
    Then Validate "Amrutha Dasireddy" and "amrutha.dasireddy@optimworks.com"
    When Click on log out button
    Then Validate login in link in home page


