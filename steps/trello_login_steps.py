from behave import *
from utils.config_reader import get_environment_url, get_user_name, get_pass_word
from pages.trello_login_page import TrelloLoginPage


@given(u"Launch the trello application")
def launch_the_trello_application(context):
    context.login_page = TrelloLoginPage(context.driver)
    env = context.config.userdata.get('environment')
    base_url = get_environment_url(env)
    context.login_page.launch_to_trello_page(base_url)


@then(u"validate trello logo")
def validate_trello_logo(context):
    context.login_page = TrelloLoginPage(context.driver)
    context.login_page.verify_the_trello_logo()


@then(u"validate all menus are display")
def validate_all_menus(context):
    context.login_page = TrelloLoginPage(context.driver)
    for row in context.table:
        menu_name = row['menu_names']
        context.login_page.verify_all_menus(menu_name)


@when(u"Click on log in link")
def validate_all_menus(context):
    context.login_page = TrelloLoginPage(context.driver)
    context.login_page.click_on_log_in_link()


@then(u"Validate login form")
def validate_login_form(context):
    context.login_page = TrelloLoginPage(context.driver)
    context.login_page.verify_login_form()


@when(u"Enter username")
def enter_username(context):
    context.login_page = TrelloLoginPage(context.driver)
    env = context.config.userdata.get('environment')
    user_name = get_user_name(env)
    context.login_page.enter_user_name(user_name)


@when(u"Click on continue button")
def click_on_continue_button(context):
    context.login_page = TrelloLoginPage(context.driver)
    context.login_page.click_on_continue_button()


@when(u"Enter password")
def enter_password(context):
    context.login_page = TrelloLoginPage(context.driver)
    env = context.config.userdata.get('environment')
    password = get_pass_word(env)
    context.login_page.enter_pass_word(password)


@when(u"Click on log in button")
def click_on_log_in_button(context):
    context.login_page = TrelloLoginPage(context.driver)
    context.login_page.click_on_login_in_button()


@then(u'Validate "{Atlassian_header}" header')
def validate_Atlassian_header(context, Atlassian_header):
    context.login_page = TrelloLoginPage(context.driver)
    context.login_page.verify_atlassian_header_in_home_page(Atlassian_header)


@then(u'Validate "{user_name}" and "{email}"')
def validate_user_name_email(context, user_name, email):
    context.login_page = TrelloLoginPage(context.driver)
    context.login_page.verify_user_name(user_name)
    context.login_page.verify_email_in_home_page(email)


@when(u"Click on log out button")
def click_on_log_out_button(context):
    context.login_page = TrelloLoginPage(context.driver)
    context.login_page.click_on_log_out_button()


@then(u"Validate login in link in home page")
def validate_login_link(context):
    context.login_page = TrelloLoginPage(context.driver)
    context.login_page.verify_log_in_link()