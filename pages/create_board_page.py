import time

from locators.create_board_loc import CreateBoardLocators
from utilities.syn_methods import SynMethods
from selenium.webdriver.common.by import By


class CreateBoardPage(SynMethods,CreateBoardLocators):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_create_button(self, input):
        loc = (By.XPATH, "//p[text()='" + input + "']")
        create_button = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
        create_button.click()

    def verify_create_form(self):
        create_form = self.wait_until_element_visible(self.create_form_loc, self.long_wait, self.driver)
        assert create_form.is_displayed() == True, "create form is not displayed"

    def click_on_create_board(self,input):
        loc = (By.XPATH, "//span[text()='" + input + "']")
        create_board = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
        create_board.click()

    def verify_create_board_header(self):
        create_board_header = self.wait_until_element_visible(self.create_board_header_loc, self.long_wait, self.driver)
        assert create_board_header.is_displayed() == True, "create board header is not displayed"

    def enter_board_name(self,input):
        board_name = self.wait_until_element_visible(self.board_title_field_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.board_title_field_loc, self.long_wait, self.driver)
        board_name.click()
        board_name.clear()
        board_name.send_keys(input)

    def click_on_board_create_button(self):
        create_button = self.wait_until_element_visible(self.create_button_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.create_button_loc, self.long_wait, self.driver)
        create_button.click()

    def verify_created_board_name(self,input):
        time.sleep(3)
        created_board_name = self.wait_until_element_visible(self.board_name_loc, self.long_wait, self.driver)
        assert created_board_name.is_displayed() == True, "board name is not displayed"
        created_board_name_text = created_board_name.text
        assert created_board_name_text == input, created_board_name_text + "created board name is not matched"
