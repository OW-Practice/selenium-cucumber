from locators.delete_board_loc import DeleteBoardLoc
from utilities.syn_methods import SynMethods
from selenium.webdriver.common.by import By


class DeletePage(DeleteBoardLoc, SynMethods):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_board_is_closed_text(self, input1):
        board_is_closed = self.wait_until_element_visible(self.board_is_closed_text_loc, self.long_wait, self.driver)
        assert board_is_closed.is_displayed() == True, "created board name is closed text is not displayed"
        board_is_closed_text = board_is_closed.text
        input = input1 + " is closed."
        assert board_is_closed_text == input, board_is_closed_text + " text is not matched"

    def verify_re_open_board_button(self,input):
        re_open_button = self.wait_until_element_visible(self.re_open_board_loc, self.long_wait, self.driver)
        assert re_open_button.is_displayed() == True, "reopen board text is not displayed"
        re_open_button_text = re_open_button.text
        assert re_open_button_text == input, re_open_button_text + "text is not matched"

    def verify_permanently_delete_board_button(self,input):
        permanently_delete_board = self.wait_until_element_visible(self.permanently_delete_board_loc, self.long_wait,
                                                                   self.driver)
        assert permanently_delete_board.is_displayed() == True, "permanently delete board text is not displayed"
        permanently_delete_board_text = permanently_delete_board.text
        assert permanently_delete_board_text == input, permanently_delete_board_text + "text is not matched"

    def click_on_permanently_delete_board_button(self):
        permanently_delete_board = self.wait_until_element_visible(self.permanently_delete_board_loc, self.long_wait,
                                                                   self.driver)
        self.wait_until_element_clickable(self.permanently_delete_board_loc, self.long_wait, self.driver)
        permanently_delete_board.click()

    def verify_delete_board_pop_up(self):
        delete_board_pop_up = self.wait_until_element_visible(self.delete_board_pop_up_loc, self.long_wait, self.driver)
        assert delete_board_pop_up.is_displayed() == True, "delete board pop up is not displayed"

    def verify_delete_board_header(self,input):
        delete_board_header = self.wait_until_element_visible(self.delete_board_header_loc, self.long_wait, self.driver)
        assert delete_board_header.is_displayed() == True, "delete board header text is not displayed"
        delete_board_header_text = delete_board_header.text
        assert delete_board_header_text == input, delete_board_header_text + "header is not matched"

    def verify_delete_board_content(self,input):
        delete_board_content = self.wait_until_element_visible(self.delete_board_content_loc, self.long_wait,
                                                               self.driver)
        assert delete_board_content.is_displayed() == True, "delete board content text is not displayed"
        delete_board_content_text = delete_board_content.text
        assert delete_board_content_text.__contains__(input) == True, "delete board content is not matched"

    def verify_delete_button(self):
        delete_button = self.wait_until_element_visible(self.delete_button_loc, self.long_wait, self.driver)
        assert delete_button.is_displayed() == True, "delete button is not displayed"

    def click_on_delete_button(self):
        delete_button = self.wait_until_element_visible(self.delete_button_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.delete_button_loc, self.long_wait, self.driver)
        delete_button.click()

    def verify_delete_board_text(self):
        delete_board = self.wait_until_element_visible(self.delete_board_text_loc, self.long_wait, self.driver)
        assert delete_board.is_displayed() == True, "delete board is not displayed"
