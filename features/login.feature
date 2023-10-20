Feature: Student Registration

  Scenario:
    Given Launch the url
    Then Validate the oracle application "Oracle Applications Cloud"
    Then Validate login form
    When Enter userid "Davina.Taylor" and password "N#dr8xo=" values
    When Click on signin button
    Then Validate User is logged into vision page
    Then Validate setting and actions image
    When Click on navigation hamburger
    Then Validate home header
    Then Validate my client group drop down "My Client Groups"
    When Click on client group drop down
    Then Validate my client group form
    Then Validate hiring option
    Then Validate hiring option logo
    When Click on hiring option
    Then Validate job requisitions header "Job Requisitions"
    Then Validate candidate search option
    When Click on candidate search option
    Then Validate search button
    When Click on search button
    Then Validate candidate search header
    When Click on add button
    Then Validate create candidate page
    Then Validate basic info header
    Then Validate create candidate field name
      | field_names_loc           |
      | Last Name                 |
      | First Name                |
      | Title                     |
      | Middle Name               |
      | Source                    |
      | Phone Number              |
      | Display Data to Candidate |
      | Email                     |
    Then Validate save and close button "ave and Close"
    Then Validate create candidate input field names
      | input_field_names_loc |
      | Last Name   |
      | First Name  |
      | Email       |
      | Middle Name |
    Then Validate drop down fields
      | drop_down_loc          | index|
      | Title                  | 1    |
      | Source                 | 1    |
      | Phone Number           | 1    |
      | Display Data to Candidate | 1 |
    When Enter candidate details into fields
      | field_name_loc | candidate_details |
      | Last Name      | suresh            |
      | First Name     | sallorju          |
      | Middle Name    | optim             |
      | Email          |suresh@yopmail.com |
    When Click on save and close button "ave and Close"
    Then Validate confirmation popup and confirmation text
    Then Validate yes and no buttons on confirmation popup
      | yes_no_loc |
      | Yes        |
      | No         |
    When Click on yes button in confirmation popup "Yes"
    Then Validate added candidate name "sallorju" and "suresh"
    When Click on navigation hamburger
    When Click on hiring option
    When Click on candidate search option
    When Click on search button
    When Click on add candidate check box "Gechi" and "Robert"
    Then Click on actions drop down and verify form
    When Click on add to requisition option "Add to Requisition"
    Then Validate add to requisition header "Add to Requisition"
    Then Validate select requisition header "Select Requisitions"
    When Click on create job application check box
    When Click on select requisitions drop down and verify form