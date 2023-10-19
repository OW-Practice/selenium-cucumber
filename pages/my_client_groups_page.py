import time

from pages.base_page import BasePage
from utilities.syn_methods import SynMethods
from locators.my_client_groups_locators import MyClientGroupsLocators


class MyClientGroupPage(BasePage, SynMethods, MyClientGroupsLocators):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_my_client_group_drop_down(self,input):
        my_client_group = self.wait_until_element_visible(self.my_client_groups_text_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.my_client_groups_text_loc, self.long_wait, self.driver)
        assert my_client_group.is_displayed() == True, "my client group is drop down is not present"
        my_client_group_text = my_client_group.text
        assert my_client_group_text == input,  my_client_group_text + " text is not matched"

    def click_on_my_client_group_drop_down(self):
        my_client_group = self.wait_until_element_visible(self.my_client_group_drop_down_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.my_client_group_drop_down_loc, self.long_wait, self.driver)
        my_client_group.click()

    def verify_my_client_group_form(self):
        my_client_group_form = self.wait_until_element_visible(self.my_client_groups_form_loc, self.long_wait,
                                                          self.driver)
        assert my_client_group_form.is_displayed() == True, "my client group form is not displayed"

    def verify_hiring_option(self):
        hiring = self.wait_until_element_visible(self.hiring_option_loc, self.long_wait, self.driver)
        assert hiring.is_displayed() == True, "hiring option is not displayed in my client group drop down"

    def verify_hiring_option_logo(self):
        hiring_logo = self.wait_until_element_visible(self.hiring_option_logo_loc, self.long_wait, self.driver)
        assert hiring_logo.is_displayed() == True, "hiring option logo is not displayed for hiring"

    def click_on_hiring_option(self):
        hiring = self.wait_until_element_visible(self.hiring_option_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.hiring_option_loc, self.long_wait, self.driver)
        hiring.click()
        time.sleep(3)

