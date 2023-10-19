from behave import *
from pages.my_client_groups_page import MyClientGroupPage


@when(u"Click on navigation hamburger")
def click_on_navigation_ham_burger(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.click_on_navigation_hamburger()


@then(u"Validate home header")
def validate_home_header(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.verify_home_header()


@then(u'Validate my client group drop down "{client_group_text}"')
def validate_my_client_group_drop_down(context,client_group_text):
    context.client = MyClientGroupPage(context.driver)
    context.client.verify_my_client_group_drop_down(client_group_text)


@when(u"Click on client group drop down")
def click_on_client_group_drop_down(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.click_on_my_client_group_drop_down()


@then(u"Validate my client group form")
def validate_my_client_group_form(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.verify_my_client_group_form()


@then(u"Validate hiring option")
def validate_hiring_option(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.verify_hiring_option()


@then(u"Validate hiring option logo")
def validate_hiring_option_logo(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.verify_hiring_option_logo()


@when(u"Click on hiring option")
def click_on_hiring_option(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.click_on_hiring_option()


@then(u"Validate job requisitions header")
def validate_job_requisitions_header(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.verify_job_requisitions_header()


@then(u"Validate candidate search option")
def validate_candidate_search_option(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.verify_candidate_search_option()


@when(u"Click on candidate search option")
def click_on_candidate_search_option(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.click_on_candidate_search_option()


@then(u"Validate candidate search header")
def validate_candidate_search_header(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.verify_candidate_search_header()


@then(u"Validate search button")
def validate_search_button(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.verify_the_search_button()


@when(u"Click on search button")
def click_on_search_button(context):
    context.client = MyClientGroupPage(context.driver)
    context.client.click_on_search_button()