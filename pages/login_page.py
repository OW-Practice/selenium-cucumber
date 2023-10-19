from pages.base_page import BasePage
from utilities.syn_methods import SynMethods
from locators.login_locators import LoginLocators


class LoginPage(BasePage, SynMethods, LoginLocators):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_login(self,url):
        self.driver.get(url)

    def verify_login_form(self):
        login_form = self.wait_until_element_visible(self.login_form_loc, self.medium_wait, self.driver)
        assert login_form.is_displayed() == True, "url is not launched"

    def verify_oracle_application_header(self,input):
        oracle_application_header = self.wait_until_element_visible(self.oracle_application_header_loc, self.medium_wait, self.driver)
        oracle_application_header_text = oracle_application_header.text
        assert oracle_application_header_text == input, "url is not launched"

    def enter_user_id(self, input):
        user_id = self.wait_until_element_visible(self.user_id_field_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.user_id_field_loc, self.medium_wait, self.driver)
        user_id.click()
        user_id.clear()
        user_id.send_keys(input)

    def enter_pass_word(self, input):
        pass_word = self.wait_until_element_visible(self.pass_word_field_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.pass_word_field_loc, self.medium_wait, self.driver)
        pass_word.click()
        pass_word.clear()
        pass_word.send_keys(input)

    def click_on_sign_in_button(self):
        sign_in_btn = self.wait_until_element_visible(self.sign_in_button_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.sign_in_button_loc, self.medium_wait, self.driver)
        sign_in_btn.click()
