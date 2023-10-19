from behave import *
from pages.create_candidate_page import CandidateInfoPage
import random
random_number = random.randint(100, 900)


@when(u"Click on add button")
def click_on_add_button(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.click_on_add_button()


@then(u'Validate create candidate page')
def validate_create_candidate_page(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.verify_create_candidate_page()


@then(u'Validate basic info header')
def validate_base_info_header(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.verify_base_info_header()


@then(u'Validate create candidate field name')
def validate_create_candidate_fields_names(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    for row in context.table:
        print(row['field_names_loc'])
        field_name = row['field_names_loc']
        context.candidate_info.verify_create_candidate_fields_names(field_name)


@then(u'Validate save and close button "{save_close}"')
def validate_save_and_close_button(context, save_close):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.verify_facebook_mr_save_options_button(save_close)


@then(u'Validate create candidate input field names')
def validate_candidate_info_input_fields(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    for row in context.table:
        field_name = row['input_field_names_loc']
        context.candidate_info.verify_candidate_info_input_fields(field_name)


@then(u'Validate drop down fields')
def validate_candidate_info_input_fields(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    for row in context.table:
        drop_down_loc = row['drop_down_loc']
        index_value = row['index']
        context.candidate_info.verify_source_title_display_phone_drop_downs(drop_down_loc, index_value)


@when(u'Enter candidate details into fields')
def enter_candidate_details_into_fields(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    for row in context.table:
        field_names_locator = row['field_name_loc']
        input_data = row['candidate_details']
        if field_names_locator.find("Email") > -1:
            input_data = "suresh"+str(random_number)+"@yopmail.com"
        context.candidate_info.enter_input_into_create_candidate_fields(field_names_locator, input_data)


@when(u'Click on save and close button "{save}"')
def click_on_save_and_close_button(context,save):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.click_on_facebook_mr_save_options_button(save)


@then(u'Validate confirmation popup and confirmation text')
def validate_confirmation_popup_and_confirmation_text(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.verify_confirmation_pop_up()
    context.candidate_info.verify_text_in_confirmation_pop_up()


@then(u'Validate yes and no buttons on confirmation popup')
def validate_yes_and_no_buttons_on_confirmation_popup(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    for row in context.table:
        yes_no_loc = row['yes_no_loc']
        context.candidate_info.verify_yes_and_no_button_in_confirmation_pop_up(yes_no_loc)


@when(u'Click on yes button in confirmation popup "{yes_loc}"')
def click_on_yes_button_in_confirmation_popup(context,yes_loc):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.click_on_yes_button(yes_loc)


@then(u'Validate added candidate name "{input1}" and "{input2}"')
def validate_added_candidate_name(context,input1,input2):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.verify_add_candidate_name(input1,input2)


@when(u'Click on add candidate check box "{input1}" and "{input2}"')
def click_on_actions_drop_down_and_verify_form(context,input1,input2):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.click_on_add_candidate_check_box(input1,input2)


@then(u'Click on actions drop down and verify form')
def click_on_actions_drop_down_and_verify_form(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.verify_and_click_on_actions_drop_down()
    context.candidate_info.verify_actions_drop_down_form()


@when(u'Click on add to requisition option "{add_requisition_loc}"')
def click_on_add_to_requisition_option(context,add_requisition_loc):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.click_on_facebook_mr_save_options_button(add_requisition_loc)


@then(u'Enter add candidate name "{input}" in keyword search field')
def enter_add_candidate_name_in_search_field(context,input):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.enter_input_to_search_field(input)


@then(u'Validate add to requisition header "{add_requisition_header}"')
def validate_add_to_requisition_header(context,add_requisition_header):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.verify_add_to_requisitions_header(add_requisition_header)


@then(u'Validate select requisition header "{select_requisition_header}"')
def validate_select_requisition_header(context,select_requisition_header):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.select_requisitions_header(select_requisition_header)


@when(u'Click on create job application check box')
def click_on_create_job_application_check_box(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.click_on_create_job_application_check_box()


@when(u'Click on select requisitions drop down and verify form')
def click_on_select_requisitions_drop_down_and_verif_form(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.click_on_select_requisitions_drop_down()
    context.candidate_info.click_on_select_requisitions_drop_down_form()


@when(u'Click on requisition option "{requisitions_loc}"')
def click_on_requisition_option(context,requisitions_loc):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.click_on_requisition_option(requisitions_loc)


@then(u'Validate job requisition "{requisitions_text}"')
def validate_job_requisition(context,requisitions_text):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.verify_add_job_requisition(requisitions_text)


@then(u'Validate requisition confirmation')
def validate_requisition_confirmation(context):
    context.candidate_info = CandidateInfoPage(context.driver)
    context.candidate_info.requisition_confirmation_text()