from selenium.webdriver.common.by import By


class LoginLocators:
    login_form_loc = (By.CSS_SELECTOR, "[name ='loginForm']")
    user_id_field_loc = (By.CSS_SELECTOR, "#userid")
    pass_word_field_loc = (By.CSS_SELECTOR, "#password")
    sign_in_button_loc = (By.CSS_SELECTOR, "#btnActive")
    oracle_logo_loc = (By.CSS_SELECTOR, "[title='Oracle Logo Home']")
    vision_header_loc = (By.CSS_SELECTOR, "[title='Oracle Logo Home']")