from behave import *
from pages.login_page import LoginPage
from utils.config_reader import get_environment_url


@given(u"Launch the url")
def launch_the_url(context):
    context.login_page = LoginPage(context.driver)
    env = context.config.userdata.get('environment')
    base_url = get_environment_url(env)
    context.login_page.navigate_to_login(base_url)


@then(u'Validate the oracle application "{oracle_header}"')
def validate_the_oracle_application(context,oracle_header):
    context.login_page = LoginPage(context.driver)
    context.login_page.verify_oracle_application_header(oracle_header)


@then(u"Validate login form")
def validate_login_form(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.verify_login_form()


@when(u'Enter userid "{user_name}" and password "{pass_word}" values')
def enter_userid_and_password_values(context,user_name,pass_word):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_user_id(user_name)
    context.login_page.enter_pass_word(pass_word)


@when(u"Click on signin button")
def click_on_signin_button(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.click_on_sign_in_button()
