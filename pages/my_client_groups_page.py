import time

from pages.base_page import BasePage
from utilities.syn_methods import SynMethods
from locators.my_client_groups_locators import MyClientGroupsLocators


class MyClientGroupPage(BasePage, SynMethods, MyClientGroupsLocators):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://fa-euth-dev13-saasfademo1.ds-fa.oraclepdemos.com/"

    def click_on_navigation_hamburger(self):
        time.sleep(5)
        ham_burger = self.wait_until_element_visible(self.navigation_ham_burger_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.navigation_ham_burger_loc, self.long_wait, self.driver)
        ham_burger.click()

    def verify_home_header(self):
        home = self.wait_until_element_visible(self.home_header_loc, self.long_wait, self.driver)
        assert home.is_displayed() == True, "home header is not displaying"

    def verify_my_client_group_drop_down(self,input):
        my_client_group = self.wait_until_element_visible(self.my_client_groups_text_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.my_client_groups_text_loc, self.long_wait, self.driver)
        assert my_client_group.is_displayed() == True, "my client group is drop down is not present"
        my_client_group_text = my_client_group.text
        assert my_client_group_text == input,  my_client_group_text + "text is not matched"

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

    def verify_job_requisitions_header(self):
        job_requisitions = self.wait_until_element_visible(self.job_requisitions_header_loc, self.long_wait, self.driver)
        assert job_requisitions.is_displayed() == True, "job_requisitions header is not displayed"

    def verify_candidate_search_option(self):
        candidate_search = self.wait_until_element_visible(self.candidate_search_loc, self.long_wait, self.driver)
        assert candidate_search.is_displayed() == True, "candidate search option is not displayed"

    def click_on_candidate_search_option(self):
        candidate_search = self.wait_until_element_visible(self.candidate_search_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.candidate_search_loc, self.long_wait, self.driver)
        candidate_search.click()

    def verify_the_search_button(self):
        search = self.wait_until_element_visible(self.search_loc, self.long_wait, self.driver)
        assert search.is_displayed() == True, "Search button is not displayed"

    def click_on_search_button(self):
        search = self.wait_until_element_visible(self.search_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.search_loc, self.long_wait, self.driver)
        search.click()
        time.sleep(4)

    def verify_candidate_search_header(self):
        candidate_search = self.wait_until_element_visible(self.candidate_search_header_loc, self.medium_wait, self.driver)
        assert candidate_search.is_displayed() == True, "candidate search header is not displayed"