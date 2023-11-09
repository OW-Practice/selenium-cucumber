import time
import pyautogui
import pyperclip
from utilities.syn_methods import SynMethods
from selenium.webdriver.common.by import By
from locators.add_list_loc import AddListLocators
from selenium.webdriver.common.action_chains import ActionChains


class AddAListCardPage(SynMethods, AddListLocators, ActionChains):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_add_a_list_button(self):
        add_a_list_button = self.wait_until_element_visible(self.add_list_button_loc, self.medium_wait, self.driver)
        assert add_a_list_button.is_displayed() == True, "add a list button is not displayed"

    def click_on_add_a_list_button(self):
        add_a_list_button = self.wait_until_element_visible(self.add_list_button, self.medium_wait, self.driver)
        self.wait_until_element_visible(self.add_list_button, self.medium_wait, self.driver)
        add_a_list_button.click()

    def enter_list_title(self, input):
        time.sleep(7)
        list_title = self.wait_until_element_visible(self.list_title_loc, self.medium_wait, self.driver)
        list_title.send_keys(input)

    def click_on_add_a_card_button(self, input):
        self.driver.refresh()
        loc = (By.XPATH, "//h2[text()='" + input + "']//ancestor::div[@data-testid='list']//*[contains(@data-testid,"
                                                   "'add-card')]")
        add_a_card_button = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(loc, self.medium_wait, self.driver)
        add_a_card_button.click()

    def enter_card_name(self, input_data):
        card_name = self.wait_until_element_visible(self.enter_card_title_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.enter_card_title_loc, self.medium_wait, self.driver)
        card_name.click()
        card_name.clear()
        card_name.send_keys(input_data)

    def click_on_add_card_button(self):
        add_card_button = self.wait_until_element_visible(self.add_card_button, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.add_card_button, self.medium_wait, self.driver)
        add_card_button.click()

    def verify_added_list_name(self, input):
        loc = (By.XPATH, "//h2[text()='" + input + "']")
        list_name = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        assert list_name.is_displayed() == True, "list name is not displayed"

    def verify_card_name(self, list_name, card_value):
        loc = (By.XPATH, "//h2[text()='" + list_name + "']//ancestor::div//a[text()='" + card_value + "']")
        card_name = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        assert card_name.is_displayed() == True, "card name is not displayed"

    def deleting_the_card(self, list_name, card_value, header, content):
        self.click_on_current_card(list_name, card_value)
        self.verify_card_details_window()
        self.verify_current_card_name(card_value)
        self.verify_current_list_name(list_name)
        self.verify_actions_section()
        self.verify_and_click_on_archive_option()
        self.verify_and_click_on_delete_button()
        self.verify_delete_pop_up()
        self.verify_delete_header(header)
        self.verify_delete_content(content)
        self.verify_and_click_on_confirm_delete_button()
        self.verify_deleted_card_in_list(list_name, card_value)

    def click_on_current_card(self, list_name, card_value):
        self.driver.refresh()
        loc = (By.XPATH, "//h2[text()='" + list_name + "']//ancestor::div//a[text()='" + card_value + "']")
        current_card = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(loc, self.medium_wait, self.driver)
        current_card.click()

    def verify_deleted_card_in_list(self, list_name, card_value):
        loc = (By.XPATH, "//h2[text()='" + list_name + "']//ancestor::div//a[text()='" + card_value + "']")
        card_name = self.is_Element_invisible(loc, self.medium_wait, self.driver)
        assert card_name == True, "deleted card name is displayed"

    def verify_deleted_lists(self, list_name):
        loc = (By.XPATH, "//h2[text()='" + list_name + "']")
        list_name = self.is_Element_invisible(loc, self.medium_wait, self.driver)
        assert list_name == True, "deleted card name is displayed"

    def verify_card_details_window(self):
        card_details_window = self.wait_until_element_visible(self.card_details_window_loc, self.medium_wait,
                                                              self.driver)
        assert card_details_window.is_displayed() == True, "card_details_window is not displayed"

    def verify_current_card_name(self, name):
        current_card_name = self.wait_until_element_visible(self.current_card_name_loc, self.medium_wait, self.driver)
        current_card_name_text = current_card_name.get_attribute("value")
        assert current_card_name_text == name, current_card_name_text + "card name is not matched"

    def verify_current_list_name(self, name):
        current_list_name = self.wait_until_element_visible(self.current_list_name_loc, self.medium_wait, self.driver)
        current_list_name_text = current_list_name.text
        assert current_list_name_text == name, current_list_name_text + "card name is not matched"

    def verify_actions_section(self):
        actions_section = self.wait_until_element_visible(self.actions_section_loc, self.medium_wait, self.driver)
        assert actions_section.is_displayed() == True, "action section is not displayed"

    def verify_and_click_on_archive_option(self):
        archive_option = self.wait_until_element_visible(self.archive_option_loc, self.medium_wait, self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", archive_option)
        assert archive_option.is_displayed() == True, "archive option is not displayed under actions section"
        self.wait_until_element_visible(self.archive_option_loc, self.medium_wait, self.driver)
        archive_option.click()

    def verify_and_click_on_delete_button(self):
        delete_button = self.wait_until_element_visible(self.delete_button_loc, self.medium_wait, self.driver)
        assert delete_button.is_displayed() == True, "delete button is not displayed under actions section"
        self.wait_until_element_visible(self.delete_button_loc, self.medium_wait, self.driver)
        delete_button.click()

    def verify_delete_pop_up(self):
        delete_pop_up = self.wait_until_element_visible(self.delete_pop_up_loc, self.medium_wait, self.driver)
        assert delete_pop_up.is_displayed() == True, "delete pop up is not displayed"

    def verify_delete_header(self, header):
        delete_header = self.wait_until_element_visible(self.delete_header_loc, self.medium_wait, self.driver)
        delete_header_text = delete_header.text
        assert delete_header_text == header, delete_header_text + "header is not matched"

    def verify_delete_content(self, content):
        delete_content = self.wait_until_element_visible(self.delete_content_loc, self.medium_wait, self.driver)
        delete_content_text = delete_content.text
        assert delete_content_text.__contains__(content) == True, delete_content_text + "content is not matched"

    def verify_and_click_on_confirm_delete_button(self):
        delete_button = self.wait_until_element_visible(self.confirm_delete_button_loc, self.medium_wait, self.driver)
        assert delete_button.is_displayed() == True, "delete button is not displayed"
        self.wait_until_element_visible(self.confirm_delete_button_loc, self.medium_wait, self.driver)
        delete_button.click()

    def click_list_menu_button(self, list_name):
        self.driver.refresh()
        loc = (By.XPATH, "//h2[text()='" + list_name + "']//parent::div//following-sibling::button//span//span")
        list_menu_button = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(loc, self.medium_wait, self.driver)
        list_menu_button.click()

    def verify_list_actions_and_archive(self, input):
        loc = (By.XPATH, "//*[text()='" + input + "']")
        actions_archive = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        assert actions_archive.is_displayed() == True, "actions header and archive of list option is not displayed"

    def click_on_archive_the_list_option(self, input):
        loc = (By.XPATH, "//*[text()='" + input + "']")
        archive_option = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(loc, self.medium_wait, self.driver)
        archive_option.click()

    def click_on_card_and_add_description_to_card(self, list_name, card_value, input_loc, description_value, save):
        self.click_on_current_card(list_name, card_value)
        self.verify_card_details_window()
        self.verify_current_card_name(card_value)
        self.verify_current_list_name(list_name)
        self.verify_the_description_section(input_loc)
        self.enter_description_input(description_value)
        self.click_on_save_edit_cancel_buttons(save)
        self.verify_added_description(description_value)
        self.click_on_close_window()

    def click_on_card_name_and_update_description(self, list_name, card_value, edit, description_value, save):
        self.click_on_current_card(list_name, card_value)
        self.verify_card_details_window()
        self.click_on_save_edit_cancel_buttons(edit)
        self.enter_description_input(description_value)
        self.click_on_save_edit_cancel_buttons(save)
        self.verify_added_description(description_value)
        self.click_on_close_window()

    def click_on_attachment_upload_image(self, list_name, card_value, file_path):
        self.click_on_current_card(list_name, card_value)
        self.verify_card_details_window()
        self.click_on_description()
        self.click_on_image()
        self.upload_image_in_description(file_path)
        time.sleep(5)

    def verify_the_description_section(self, input_loc):
        loc = (By.XPATH, "//h3[text()='" + input_loc + "']")
        description = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        assert description.is_displayed() == True, "description section is not displayed"

    def enter_description_input(self,description_value):
        description = self.wait_until_element_visible(self.description_input_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.description_input_loc, self.medium_wait, self.driver)
        description.click()
        description.clear()
        description.send_keys(description_value)

    def click_on_save_edit_cancel_buttons(self,input):
        loc = (By.XPATH, "//button[text()='" + input + "']")
        save_button = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(loc, self.medium_wait, self.driver)
        save_button.click()

    def verify_added_description(self,description_value):
        added_description = self.wait_until_element_visible(self.added_description_text_loc, self.medium_wait, self.driver)
        added_description_text = added_description.text
        assert added_description_text.upper() == description_value.upper(), added_description_text + " text is not matched"

    def click_on_close_window(self):
        close_window = self.wait_until_element_visible(self.close_window_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.close_window_loc, self.medium_wait, self.driver)
        close_window.click()

    def click_on_image(self):
        upload_img = self.wait_until_element_visible(self.attachment_button_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.attachment_button_loc, self.medium_wait, self.driver)
        upload_img.click()

    def upload_image_in_description(self,file_path):
        upload_img = self.wait_until_element_visible(self.upload_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.upload_loc, self.medium_wait, self.driver)
        upload_img.click()
        time.sleep(5)
        pyperclip.copy(file_path)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(3)

    def click_on_description(self):
        added_description = self.wait_until_element_visible(self.added_description_text_loc, self.medium_wait,self.driver)
        self.wait_until_element_clickable(self.added_description_text_loc, self.medium_wait, self.driver)
        added_description.click()

    def verify_success_text(self):
        success = self.wait_until_element_visible(self.success_text_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.success_text_loc, self.medium_wait, self.driver)
        assert success.is_displayed() == True, "success text is not displayed"

    def verify_uploaded_image_for_card(self, input):
        loc = (By.XPATH, "//a[text()='" + input + "']//ancestor::div[@data-testid='trello-card']//div[@data-testid='card-front-cover']")
        image_to_card = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", image_to_card)
        assert image_to_card.is_displayed() == True, "image is not attached"

    def click_on_close_btn(self):
        close_btn = self.wait_until_element_visible(self.close_select_img_pop_up_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.close_select_img_pop_up_loc, self.medium_wait, self.driver)
        close_btn.click()
