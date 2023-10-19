import time

from pages.base_page import BasePage
from locators.add_candidate_info_locators import CandidateInfoLocators
from utilities.syn_methods import SynMethods
from selenium.webdriver.common.by import By
import random


class CandidateInfoPage(BasePage,SynMethods,CandidateInfoLocators):
    def __init__(self, driver):
        super().__init__(driver)

    random_number = random.randint(100,900)

    def click_on_add_button(self):
        add_candidate_button = self.wait_until_element_visible(self.add_candidate_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.add_candidate_loc, self.long_wait, self.driver)
        add_candidate_button.click()

    def verify_create_candidate_page(self):
        create_candidate_page = self.wait_until_element_visible(self.create_candidate_page_loc,self.long_wait,self.driver)
        assert create_candidate_page.is_displayed() == True, "base info header is not displayed"

    def verify_base_info_header(self):
        base_info_header = self.wait_until_element_visible(self.base_info_header_loc,self.long_wait,self.driver)
        assert base_info_header.is_displayed() == True, "base info header is not displayed"

    def verify_create_candidate_fields_names(self,loc_value):
        loc = (By.XPATH, "//label[text()='" + loc_value + "']")
        create_candidate_field_name = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        assert create_candidate_field_name.is_displayed() == True, "create candidate fields are not displayed"

    def verify_candidate_info_input_fields(self,loc_value):
        loc = (By.XPATH, "//*[text()='" + loc_value + "']/../..//input")
        create_candidate_field = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        assert create_candidate_field.is_displayed() == True, "create candidate fields are not displayed"

    def verify_source_title_display_phone_drop_downs(self,loc_value,index):
        loc = (By.XPATH, "(//*[text()='" + loc_value + "']/../..//input)['" + index + "']")
        source_title_input_fields = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        assert source_title_input_fields.is_displayed() == True, "create candidate fields are not displayed"

    def click_on_source_title_display_phone_drop_downs(self,loc_value,index):
        loc = (By.XPATH, "(//*[text()='" + loc_value + "']/../..//input)['" + index + "']")
        source_title_input_fields = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
        source_title_input_fields.click()

    def verify_facebook_mr_save_options_button(self,loc_value):
        loc = (By.XPATH, "//*[text()='"+loc_value+"']")
        options_in_drop_down = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        assert options_in_drop_down.is_displayed() == True, "create candidate fields are not displayed"

    def click_on_facebook_mr_save_options_button(self,loc_value):
        time.sleep(3)
        loc = (By.XPATH, "//*[text()='"+loc_value+"']")
        options_in_drop_down = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
        options_in_drop_down.click()

    def enter_input_into_create_candidate_fields(self,loc_value,input):
        loc = (By.XPATH, "//*[text()='" + loc_value + "']/../..//input")
        create_candidate_field = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
        create_candidate_field.click()
        create_candidate_field.clear()
        create_candidate_field.send_keys(input)
        time.sleep(3)

    def verify_confirmation_pop_up(self):
        confirmation_pop_up = self.wait_until_element_visible(self.confirmation_pop_up_loc, self.long_wait, self.driver)
        assert confirmation_pop_up.is_displayed() == True, "student is not saved"

    def verify_text_in_confirmation_pop_up(self):
        confirmation_text = self.wait_until_element_visible(self.confirmation_text_loc, self.long_wait, self.driver)
        assert confirmation_text.is_displayed() == True, "student is not saved"

    def verify_yes_and_no_button_in_confirmation_pop_up(self,loc):
        loc = (By.XPATH, "//span[text()='" + loc + "']")
        yes_button = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        assert yes_button.is_displayed() == True, "yes or no button is not displayed"

    def click_on_yes_button(self,loc):
        loc = (By.XPATH, "//span[text()='" + loc + "']")
        yes_button = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
        yes_button.click()

    def verify_and_click_on_actions_drop_down(self):
        action_drop_down = self.wait_until_element_visible(self.actions_drop_down_loc, self.long_wait, self.driver)
        assert action_drop_down.is_displayed() == True, "actions drop down is not displayed"
        self.wait_until_element_visible(self.actions_drop_down_loc, self.long_wait, self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",action_drop_down)
        action_drop_down.click()

    def verify_actions_drop_down_form(self):
        drop_down_form = self.wait_until_element_visible(self.actions_drop_down_form_loc, self.long_wait,self.driver)
        assert drop_down_form.is_displayed() == True, "action drop down form is not displayed"

    def enter_input_to_search_field(self,input):
        search_field = self.wait_until_element_visible(self.key_word_search_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.key_word_search_loc, self.long_wait, self.driver)
        search_field.click()
        search_field.send_keys(input)

    def click_on_add_candidate_check_box(self,f_name,l_name):
        loc = (By.XPATH, "(//*[text()='" + f_name + ", " + l_name + "']/ancestor::td/preceding-sibling::td/descendant::label)[2]")
        add_candidate_check_box = self.wait_until_element_visible(loc, self.long_wait,self.driver)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });", add_candidate_check_box)
        add_candidate_check_box.click()

    def verify_add_to_requisitions_header(self,input):
        time.sleep(3)
        requisitions_header = self.wait_until_element_visible(self.add_to_requisitions_header_loc, self.long_wait,self.driver)
        assert requisitions_header.is_displayed() == True, "add_to_requisitions_header is not displayed"
        requisitions_header_text = requisitions_header.text
        assert requisitions_header_text == input, requisitions_header_text + "header is not matched"

    def select_requisitions_header(self,input):
        select_requisitions_header = self.wait_until_element_visible(self.select_requisitions_header_loc, self.long_wait,
                                                              self.driver)
        assert select_requisitions_header.is_displayed() == True, "add_to_requisitions_header is not displayed"
        select_requisitions_header_text = select_requisitions_header.text
        assert select_requisitions_header_text == input, select_requisitions_header_text + "header is not matched"

    def click_on_create_job_application_check_box(self):
        check_box = self.wait_until_element_visible(self.create_job_application_check_box_loc, self.long_wait,self.driver)
        self.wait_until_element_clickable(self.create_job_application_check_box_loc, self.long_wait, self.driver)
        check_box.click()

    def click_on_select_requisitions_drop_down(self):
        drop_down = self.wait_until_element_visible(self.select_requisitions_drop_down_loc, self.long_wait,self.driver)
        self.wait_until_element_clickable(self.select_requisitions_drop_down_loc, self.long_wait, self.driver)
        drop_down.click()

    def click_on_select_requisitions_drop_down_form(self):
        drop_down_form = self.wait_until_element_visible(self.select_requisitions_drop_down_form_loc, self.long_wait,self.driver)
        assert drop_down_form.is_displayed() == True, "select requisitions drop down form is not displayed"
        time.sleep(3)

    def click_on_requisitions(self,requisition_loc):
        loc = (By.XPATH, "//*[text()='" + requisition_loc + "']")
        requisitions = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
        requisitions.click()

    def click_on_requisition_option(self,requisition_loc):
        loc = (By.XPATH, "//*[text()='" + requisition_loc + "']/../..")
        requisitions = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });", requisitions)
        requisitions.click()

    def verify_add_job_requisition(self,input):
        add_requisitions = self.wait_until_element_visible(self.add_requisition_loc,self.long_wait,self.driver)
        assert add_requisitions.is_displayed() == True, "add_to_requisitions_header is not displayed"
        add_requisitions_header_text = add_requisitions.text
        assert add_requisitions_header_text.__contains__(input) == True, add_requisitions_header_text + "header is not matched"

    def requisition_confirmation_text(self):
        time.sleep(3)
        requisition_confirmation = self.wait_until_element_visible(self.requisition_confirmation_text_loc, self.long_wait, self.driver)
        assert requisition_confirmation.is_displayed() == True, "add_to_requisitions_header is not displayed"

    def verify_add_candidate_name(self,f_name,l_name):
        loc = (By.XPATH, "//div[contains(@title,'" + f_name + " " + l_name + "')]")
        candidate_name = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        assert candidate_name.is_displayed() == True, "candidate name is not displayed"