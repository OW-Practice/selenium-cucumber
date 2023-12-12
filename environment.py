import allure
import os
from selenium import webdriver


def before_all(context):
    browser = context.config.userdata.get('browser')
    if browser == 'chrome':
        context.driver = webdriver.Chrome(executable_path="drivers\chromedriver.exe")
    elif browser == 'firefox':
        context.driver = webdriver.Firefox()
    else:
        context.driver = webdriver.ChromiumEdge()
    context.driver.maximize_window()


def before_scenario(context, scenario):
    context.board_names = []

def after_step(context, step):
    if step.status == "failed":
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_name = "screenshot1.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)
        context.driver.save_screenshot(screenshot_path)
        allure.attach(
            body=open(screenshot_path, "rb").read(),
            name=screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )


def after_all(context):
    context.driver.quit()