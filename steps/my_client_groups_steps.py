from behave import *
from pages.my_client_groups_page import MyClientGroupPage


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