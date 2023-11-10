from behave import *
from pages.create_board_page import CreateBoardPage
from faker import Faker
fake = Faker()


@when(u'Click on the "{input}" button in home page.')
def click_on_create_button(context,input):
    context.create = CreateBoardPage(context.driver)
    context.create.click_on_create_button(input)


@then(u"Validate create form")
def validate_create_form(context):
    context.create = CreateBoardPage(context.driver)
    context.create.verify_create_form()


@when(u'Click on the "{input}" button in create form')
def click_on_create_board_button(context,input):
    context.create = CreateBoardPage(context.driver)
    context.create.click_on_create_board(input)


@then(u"Validate create board header")
def validate_create_board_header(context):
    context.create = CreateBoardPage(context.driver)
    context.create.verify_create_board_header()


@when(u'Enter board name "{input}"')
def enter_board_name(context,input):
    context.create = CreateBoardPage(context.driver)
    context.create.enter_board_name(input)


@when(u"Enter random board name in create board form")
def enter_random_board_name(context):
    context.create = CreateBoardPage(context.driver)
    name = fake.name()
    context.name = name
    context.create.enter_board_name(name)


@when(u"Click on create button in create board form")
def click_on_create_button(context):
    context.create = CreateBoardPage(context.driver)
    context.create.click_on_board_create_button()


@then(u'Validate created board name "{input}" is displayed')
def verify_created_board_name(context,input):
    context.create = CreateBoardPage(context.driver)
    context.create.verify_created_board_name(input)


@then(u'Validate randomly created board name is displayed')
def verify_random_created_board_name(context):
    context.create = CreateBoardPage(context.driver)
    context.create.verify_created_board_name(context.name)