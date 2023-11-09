from behave import *
from pages.trello_home_page import TrelloHomePage


@then(u"Validate the trello header should displayed in home page")
def validate_the_trello_header(context):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_trello_header()


@When(u'Click on profile button "{input}"')
def click_on_profile_button(context,input):
    context.home = TrelloHomePage(context.driver)
    context.home.click_on_profile(input)


@then(u'Validate username "{input}"')
def validate_username(context,input):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_user_name(input)


@when(u"Click on the trello header")
def click_on_the_trello_header(context):
    context.home = TrelloHomePage(context.driver)
    context.home.click_on_trello_header()


@then(u'Validate "{input}" section header should displayed in trello home page.')
def validate_the_yours_workspace_section_header(context,input):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_yours_work_space_section(input)


@then(u'Validate "{input}" should displayed in yours workspace section')
def validate_the_created_board_names_under_yours_workspace_section(context,input):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_create_board_name(input)


@then(u"Validate the randomly created board names under yours workspace section is displayed")
def validate_the_created_board_names_under_yours_workspace_section(context):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_create_board_name(context.name)


@when(u'Click on the created board name "{input}"')
def click_on_the_created_board_name(context,input):
    context.home = TrelloHomePage(context.driver)
    context.home.click_on_create_board(input)


@when(u"Click on the randomly created board name")
def click_on_the_created_board_name(context):
    context.home = TrelloHomePage(context.driver)
    context.home.click_on_create_board(context.name)


@when(u"Click on the menu show")
def click_on_the_menu_show(context):
    context.home = TrelloHomePage(context.driver)
    context.home.click_on_show_menu()


@then(u"Validate menu header is displayed")
def validate_menu_header_is_displayed(context):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_trello_header()


@then(u"Validate close board option is displayed")
def validate_close_board_option_is_displayed(context):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_close_board_option()


@when(u"Click on close board option")
def click_on_close_board_option(context):
    context.home = TrelloHomePage(context.driver)
    context.home.click_on_close_board_option()


@then(u"Validate close board pop up is displayed")
def validate_close_board_pop_up_is_displayed(context):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_close_board_pop_up()


@then(u'Validate "{input}" close header should displayed in delete pop up.')
def validate_close_board_header_is_displayed(context,input):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_close_board_header(input)


@then(u'Validate "{input}" close content text should displayed in delete pop up.')
def validate_close_board_context_is_displayed(context,input):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_close_board_content(input)


@then(u"Validate close button is displayed in close board pop up")
def validate_close_button_is_displayed(context):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_close_board_button()


@when(u"Click on the close button in close board pop up")
def click_on_the_close_button(context):
    context.home = TrelloHomePage(context.driver)
    context.home.click_on_close_board_button()


@then(u'Validate "{input}" name should not display in your work space section')
def validate_delete_board_name_in_your_work_space_section(context,input):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_deleted_board_name_should_not_display(input)


@then(u"Validate delete random board name should not display in your work space section")
def validate_delete_board_name_in_your_work_space_section(context):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_deleted_board_name_should_not_display(context.name)


@then(u"Validate work space section should displayed in trello home page.")
def validate_work_space_section_is_displayed(context):
    context.home = TrelloHomePage(context.driver)
    context.home.verify_work_space_section()


@then(u"Validate work space menu options should display")
def validate_work_space_menu_options_should_display(context):
    context.home = TrelloHomePage(context.driver)
    for row in context.table:
        options = row['menu_options']
        context.home.verify_work_space_menu_options(options)