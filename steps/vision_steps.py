from behave import *
from pages.vision_page import VisionPage


@then(u"Validate User is logged into vision page")
def validate_user_is_logged_into_vision_page(context):
    context.vision = VisionPage(context.driver)
    context.vision.verify_vision_header()


@then(u"Validate setting and actions image")
def validate_setting_and_actions_image(context):
    context.vision = VisionPage(context.driver)
    context.vision.verify_setting_actions_img()


@when(u"Click on navigation hamburger")
def click_on_navigation_ham_burger(context):
    context.vision = VisionPage(context.driver)
    context.vision.click_on_navigation_hamburger()


@then(u"Validate home header")
def validate_home_header(context):
    context.vision = VisionPage(context.driver)
    context.vision.verify_home_header()



