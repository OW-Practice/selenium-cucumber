from selenium.webdriver.common.by import By


class TrelloLoginLocators:
    trello_logo_loc = (By.CSS_SELECTOR, "[class*='InnerHeader'] [class*='LogoLink']")
    log_in_link_loc = (By.XPATH, "//div[contains(@class,'ButtonGroup')]/a[text()='Log in']")
    login_form_loc = (By.CSS_SELECTOR, "#form-login")
    user_name_field_loc = (By.CSS_SELECTOR, "#username")
    continue_button_loc = (By.CSS_SELECTOR, "#login-submit")
    pass_word_field_loc = (By.CSS_SELECTOR, "input#password")
    log_in_button_loc = (By.CSS_SELECTOR, "#login-submit")
    log_out_header_loc = (By.CSS_SELECTOR, "[data-testid='header-suffix']")
    user_name_loc = (By.CSS_SELECTOR, "[data-testid='email']")
    e_mail_address_loc = (By.CSS_SELECTOR, "[data-testid='email']+p")
    log_out_button_loc = (By.CSS_SELECTOR, "[data-testid='logout-button'] span")