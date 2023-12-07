from behave import *
from pages.delete_page import DeletePage


@then(u'Validate "{input}" is closed text should displayed in delete page.')
def validate_board_name_is_closed_text_is_displayed(context,input):
    context.delete = DeletePage(context.driver)
    context.delete.verify_board_is_closed_text(input)


@then(u"Validate randomly board name is closed text is displayed in the delete board page")
def validate_board_name_is_closed_text_is_displayed(context):
    context.delete = DeletePage(context.driver)
    context.delete.verify_board_is_closed_text(context.name)


@then(u"Validate board name is closed text is displayed in the delete board page")
def validate_board_names_is_closed_text_is_displayed(context):
    context.delete = DeletePage(context.driver)
    context.delete.verify_board_is_closed_text(context.board_names[0])


@then(u'Validate "{input}" button is displayed in the Delete boards page.')
def validate_re_open_board_button_is_displayed(context,input):
    context.delete = DeletePage(context.driver)
    context.delete.verify_re_open_board_button(input)


@then(u'Validate "{input}" link is displayed in the delete boards page.')
def validate_re_open_board_button_is_displayed(context,input):
    context.delete = DeletePage(context.driver)
    context.delete.verify_permanently_delete_board_button(input)


@when(u"Click on permanently delete board button")
def click_on_permanently_delete_board_button(context):
    context.delete = DeletePage(context.driver)
    context.delete.click_on_permanently_delete_board_button()


@then(u"Validate delete board pop up is displayed")
def validate_delete_board_pop_up_is_displayed(context):
    context.delete = DeletePage(context.driver)
    context.delete.verify_delete_board_pop_up()


@then(u'Validate "{input}" header should displayed in delete pop up.')
def validate_delete_board_pop_header_displayed(context,input):
    context.delete = DeletePage(context.driver)
    context.delete.verify_delete_board_header(input)


@then(u'Validate "{input}" content text should displayed in delete pop up.')
def validate_delete_board_pop_content_displayed(context,input):
    context.delete = DeletePage(context.driver)
    context.delete.verify_delete_board_content(input)


@then(u"Validate delete button should displayed in delete pop up.")
def validate_delete_button_displayed(context):
    context.delete = DeletePage(context.driver)
    context.delete.verify_delete_button()


@when(u"Click on delete button")
def click_on_delete_button(context):
    context.delete = DeletePage(context.driver)
    context.delete.click_on_delete_button()


@then(u"Validate board deleted pop up should displayed in the home page.")
def validate_board_deleted_pop_up_is_displayed(context):
    context.delete = DeletePage(context.driver)
    context.delete.verify_delete_board_text()