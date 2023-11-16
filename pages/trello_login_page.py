from locators.trello_login_loc import TrelloLoginLocators
from utilities.syn_methods import SynMethods
from selenium.webdriver.common.by import By


class TrelloLoginPage(SynMethods,TrelloLoginLocators):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_to_trello_page(self,url):
        self.driver.get(url)

    def verify_the_trello_logo(self):
        trello_logo = self.wait_until_element_visible(self.trello_logo_loc, self.long_wait, self.driver)
        assert trello_logo.is_displayed() == True, "trello logo is not displayed"

    def verify_all_menus(self,loc_input):
        loc = (By.XPATH, "//div[contains(@class,'TabGroup')]/button[text()='" + loc_input + "']")
        all_menus = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        assert all_menus.is_displayed() == True, "all menu are not displayed"

    def click_on_log_in_link(self):
        log_in_link = self.wait_until_element_visible(self.log_in_link_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.log_in_link_loc, self.long_wait, self.driver)
        log_in_link.click()

    def verify_login_form(self):
        login_form = self.wait_until_element_visible(self.login_form_loc, self.long_wait, self.driver)
        assert login_form.is_displayed() == True, "login form is not displayed"

    def enter_user_name(self,input):
        user_name = self.wait_until_element_visible(self.user_name_field_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.user_name_field_loc, self.long_wait, self.driver)
        user_name.click()
        user_name.clear()
        user_name.send_keys(input)

    def enter_pass_word(self,input):
        pass_word = self.wait_until_element_visible(self.pass_word_field_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.pass_word_field_loc, self.long_wait, self.driver)
        pass_word.click()
        pass_word.clear()
        pass_word.send_keys(input)

    def click_on_continue_button(self):
        continue_button = self.wait_until_element_visible(self.continue_button_loc, self.long_wait, self.driver)
        self.wait_until_element_visible(self.continue_button_loc, self.long_wait, self.driver)
        continue_button.click()

    def click_on_login_in_button(self):
        log_in_button = self.wait_until_element_visible(self.log_in_button_loc, self.long_wait, self.driver)
        self.wait_until_element_visible(self.log_in_button_loc, self.long_wait, self.driver)
        log_in_button.click()

    def verify_atlassian_header_in_home_page(self, input):
        atlassian_header = self.wait_until_element_visible(self.log_out_header_loc, self.medium_wait, self.driver)
        assert atlassian_header.is_displayed() == True, "atlassian_header is not displayed"
        atlassian_header_text = atlassian_header.text
        assert atlassian_header_text == input,  atlassian_header_text + "header is not matched"

    def verify_user_name(self, input):
        user_name = self.wait_until_element_visible(self.user_name_loc, self.medium_wait, self.driver)
        assert user_name.is_displayed() == True, "atlassian_header is not displayed"
        user_name_text = user_name.text
        assert user_name_text == input,  user_name_text + "header is not matched"

    def verify_email_in_home_page(self, input):
        email = self.wait_until_element_visible(self.e_mail_address_loc, self.medium_wait, self.driver)
        assert email.is_displayed() == True, "atlassian_header is not displayed"
        email_text = email.text
        assert email_text == input,  email_text + "header is not matched"

    def click_on_log_out_button(self):
        log_out_button = self.wait_until_element_visible(self.log_out_button_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.log_out_button_loc, self.medium_wait, self.driver)
        log_out_button.click()

    def verify_log_in_link(self):
        log_in_link = self.wait_until_element_visible(self.log_in_link_loc, self.long_wait, self.driver)
        assert log_in_link.is_displayed() == True, "login link is not displayed"
