from locators.trello_home_loc import TrelloHomeLocators
from utilities.syn_methods import SynMethods
from selenium.webdriver.common.by import By


class TrelloHomePage(SynMethods, TrelloHomeLocators):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_profile(self, loc_input):
        loc = (By.CSS_SELECTOR, "div[title*='" + loc_input + "']")
        profile_button = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
        profile_button.click()

    def verify_user_name(self, input):
        loc = (By.XPATH, "//div[text()='" + input + "']")
        user_name = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        assert user_name.is_displayed() == True, "user name is not  displayed"

    def verify_trello_header(self):
        trello_header = self.wait_until_element_visible(self.trello_header_loc, self.long_wait, self.driver)
        assert trello_header.is_displayed() == True, "trello header is not displayed"

    def click_on_trello_header(self):
        trello_header = self.wait_until_element_visible(self.trello_header_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.trello_header_loc, self.long_wait, self.driver)
        trello_header.click()

    def verify_yours_work_space_section(self, input):
        yours_work_space_section = self.wait_until_element_visible(self.yours_work_space_section_loc, self.long_wait,
                                                                   self.driver)
        assert yours_work_space_section.is_displayed() == True, "yours work space section text is not displayed"
        yours_work_space_section_text = yours_work_space_section.text
        assert yours_work_space_section_text == input, yours_work_space_section_text + "text is not matched"

    def verify_create_board_name(self, loc_input):
        loc = (By.XPATH, "//div/h3//following-sibling::div//*[@title='" + loc_input + "']")
        create_board_name = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        assert create_board_name.is_displayed() == True, "created board name is not displayed"

    def verify_deleted_board_name_should_not_display(self, loc_input):
        yours_work_space_section = self.wait_until_element_visible(self.yours_work_space_section_loc, self.long_wait,
                                                                   self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView();", yours_work_space_section)
        loc = (By.XPATH, "//div/h3//following-sibling::div//*[@title='" + loc_input + "']")
        create_board_name = self.is_Element_invisible(loc, self.long_wait, self.driver)
        assert create_board_name == True, "deleted board name is displaying"

    def click_on_create_board(self, loc_input):
        loc = (By.XPATH, "//div/h3//following-sibling::div//*[@title='" + loc_input + "']")
        create_board_name = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
        create_board_name.click()

    def click_on_show_menu(self):
        show_menu = self.wait_until_element_visible(self.show_menu_button_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.show_menu_button_loc, self.long_wait, self.driver)
        show_menu.click()

    def verify_menu_header(self):
        menu_header = self.wait_until_element_visible(self.show_header_loc, self.long_wait, self.driver)
        assert menu_header.is_displayed() == True, "menu header is not displayed"

    def verify_close_board_option(self):
        close_board = self.wait_until_element_visible(self.close_board_option_loc, self.long_wait, self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView();", close_board)
        assert close_board.is_displayed() == True, "close board option is not displayed"

    def click_on_close_board_option(self):
        close_board = self.wait_until_element_visible(self.close_board_option_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.close_board_option_loc, self.long_wait, self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView();", close_board)
        close_board.click()

    def verify_close_board_pop_up(self):
        close_board_form = self.wait_until_element_visible(self.close_board_pop_up_loc, self.long_wait, self.driver)
        assert close_board_form.is_displayed() == True, "close board pop up is not displayed"

    def verify_close_board_header(self, input):
        close_board_header = self.wait_until_element_visible(self.close_board_header_loc, self.long_wait, self.driver)
        assert close_board_header.is_displayed() == True, "close board header is not displayed"
        close_board_header_text = close_board_header.text
        assert close_board_header_text == input, close_board_header_text + "header is not matched"

    def verify_close_board_content(self, input):
        close_board_content = self.wait_until_element_visible(self.pop_over_content_loc, self.long_wait, self.driver)
        assert close_board_content.is_displayed() == True, "close board pop content up is not displayed"
        close_board_content_text = close_board_content.text
        assert close_board_content_text.__contains__(input) == True, "close board content is not matched"

    def verify_close_board_button(self):
        close_board_button = self.wait_until_element_visible(self.close_button_loc, self.long_wait, self.driver)
        assert close_board_button.is_displayed() == True, "close button is not displayed"

    def click_on_close_board_button(self):
        close_board_button = self.wait_until_element_visible(self.close_button_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.close_button_loc, self.long_wait, self.driver)
        close_board_button.click()

    def verify_work_space_section(self):
        work_space = self.wait_until_element_visible(self.work_space_loc, self.long_wait, self.driver)
        assert work_space.is_displayed() == True, "work space section is not displayed"

    def verify_work_space_menu_options(self, input):
        loc = (By.XPATH, "//li[contains(@data-testid,'home-team')] //ul //span[text()='" + input + "']")
        menu_options = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        assert menu_options.is_displayed() == True, "menu options are not displayed"

    def verify_log_out_button_in_menu(self, input):
        log_out = self.wait_until_element_visible(self.log_out_button_loc, self.medium_wait, self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", log_out)
        assert log_out.is_displayed() == True, "log out option is not displayed in menu"
        log_out_text = log_out.text
        assert log_out_text == input, log_out_text + " text is not matched"

    def click_on_log_out_option(self):
        log_out = self.wait_until_element_visible(self.log_out_button_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.log_out_button_loc, self.medium_wait, self.driver)
        log_out.click()