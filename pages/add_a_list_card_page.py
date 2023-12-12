import time
import pyautogui
import pyperclip
from utilities.syn_methods import SynMethods
from selenium.webdriver.common.by import By
from locators.add_list_loc import AddListLocators
from selenium.webdriver.common.action_chains import ActionChains
from locators.move_card_loc import MoveCardLoc
from selenium.webdriver.support.ui import Select
from locators.template_card_loc import TemplateCardsLoc


class AddAListCardPage(SynMethods, AddListLocators, ActionChains, MoveCardLoc, Select,TemplateCardsLoc):
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
        time.sleep(3)
        list_title = self.wait_until_element_visible(self.list_title_loc, self.medium_wait, self.driver)
        list_title.send_keys(input)

    def click_on_add_a_card_button(self, input):
        self.driver.refresh()
        loc = (By.XPATH, "//h2[text()='" + input + "']//ancestor::div[@data-testid='list']//*[contains(@data-testid,'add-card')]")
        add_a_card_button = self.wait_until_element_visible(loc, self.long_wait, self.driver)
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
        current_card = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", current_card)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
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
        current_card_name_text = current_card_name.text
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
        delete_header_text = delete_header.get_attribute("value")
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
        self.click_on_buttons(save)
        self.verify_added_description(description_value)
        self.click_on_close_window()

    def click_on_card_name_and_update_description(self, list_name, card_value, edit, description_value, save):
        self.click_on_current_card(list_name, card_value)
        self.verify_card_details_window()
        self.click_on_buttons(edit)
        self.enter_description_input(description_value)
        self.click_on_buttons(save)
        self.verify_added_description(description_value)
        self.click_on_close_window()

    def click_on_attachment_upload_image(self, list_name, card_value, file_path):
        self.click_on_current_card(list_name, card_value)
        self.verify_card_details_window()
        self.click_on_description()
        self.click_on_image()
        self.upload_image_in_description(file_path)

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

    def click_on_buttons(self,input):
        loc = (By.XPATH, "//button[text()='" + input + "']")
        button = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(loc, self.medium_wait, self.driver)
        button.click()

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
        time.sleep(3)
        pyperclip.copy(file_path)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

    def click_on_description(self):
        added_description = self.wait_until_element_visible(self.added_description_text_loc, self.medium_wait,self.driver)
        self.wait_until_element_clickable(self.added_description_text_loc, self.medium_wait, self.driver)
        added_description.click()

    def verify_success_text(self):
        success = self.wait_until_element_visible(self.success_text_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.success_text_loc, self.medium_wait, self.driver)
        assert success.is_displayed() == True, "success text is not displayed"

    def verify_uploaded_image_for_card(self):
        image_to_card = self.wait_until_element_visible(self.image_loc, self.medium_wait, self.driver)
        assert image_to_card.is_displayed() == True, "image is not attached"

    def click_on_close_btn(self):
        close_btn = self.wait_until_element_visible(self.close_select_img_pop_up_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.close_select_img_pop_up_loc, self.medium_wait, self.driver)
        close_btn.click()

    def verify_label_icon(self):
        label_icon = self.wait_until_element_visible(self.label_icon_loc, self.medium_wait, self.driver)
        assert label_icon.is_displayed() == True, "label icon is not displayed"

    def verify_label_option(self):
        label_option = self.wait_until_element_visible(self.label_option_loc, self.medium_wait, self.driver)
        assert label_option.is_displayed() == True, "label option is not displayed"

    def click_on_label_option(self):
        label_option = self.wait_until_element_visible(self.label_option_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.label_option_loc, self.medium_wait, self.driver)
        label_option.click()

    def verify_label_form(self):
        label_form = self.wait_until_element_visible(self.label_form_loc, self.medium_wait, self.driver)
        assert label_form.is_displayed() == True, "label option is not displayed"

    def verify_label_header(self):
        label_header = self.wait_until_element_visible(self.label_header_loc, self.medium_wait, self.driver)
        assert label_header.is_displayed() == True, "label option is not displayed"

    def select_color(self, input):
        loc = (By.CSS_SELECTOR, "ul span[data-color='" + input + "']")
        select_color = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(loc, self.medium_wait, self.driver)
        select_color.click()

    def click_on_edit_button(self, input):
        loc = (By.XPATH, "//span[@data-color='" + input + "']//following-sibling::button//span[@data-testid='EditIcon']")
        edit_button = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(loc, self.medium_wait, self.driver)
        edit_button.click()

    def verify_edit_label_form(self):
        edit_label_form = self.wait_until_element_visible(self.edit_label_form_loc, self.medium_wait, self.driver)
        assert edit_label_form.is_displayed() == True, "label option is not displayed"

    def verify_edit_label_header(self):
        edit_label_header = self.wait_until_element_visible(self.edit_label_header_loc, self.medium_wait, self.driver)
        assert edit_label_header.is_displayed() == True, "label option is not displayed"

    def enter_input_in_title(self, input):
        title_input = self.wait_until_element_visible(self.title_field_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.title_field_loc, self.medium_wait, self.driver)
        title_input.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        title_input.send_keys(input)
        pyautogui.press('enter')

    def click_on_close_button_of_label_pop_up(self):
        label_pop_up = self.wait_until_element_visible(self.close_label_pop_up_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.close_label_pop_up_loc, self.medium_wait, self.driver)
        label_pop_up.click()

    def verify_color_name_of_label(self, input, label_text):
        loc = (By.CSS_SELECTOR, "[data-color='" + input + "']")
        color_name_of_label = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", color_name_of_label)
        assert color_name_of_label.is_displayed() == True, "color is added under label field"
        color_name_of_label_text = color_name_of_label.text
        assert color_name_of_label_text == label_text, color_name_of_label_text + "label text is not matched"

    def add_color_and_label_name(self, color_input, title_input):
        self.verify_label_icon()
        self.verify_label_option()
        self.click_on_label_option()
        self.verify_label_form()
        self.verify_label_header()
        self.select_color(color_input)
        self.click_on_edit_button(color_input)
        self.verify_edit_label_form()
        self.verify_edit_label_header()
        self.enter_input_in_title(title_input)
        self.click_on_close_button_of_label_pop_up()

    def verify_move_option(self):
        move_option = self.wait_until_element_visible(self.move_button_loc, self.medium_wait, self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", move_option)
        assert move_option.is_displayed() == True, "move option is not present"

    def click_on_move_option(self):
        move_option = self.wait_until_element_visible(self.move_button_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.move_button_loc, self.medium_wait, self.driver)
        move_option.click()

    def verify_move_card_form(self):
        move_card_form = self.wait_until_element_visible(self.move_card_form_loc, self.medium_wait, self.driver)
        assert move_card_form.is_displayed() == True, "move option is not present"

    def verify_move_card_header(self, input):
        move_card_header = self.wait_until_element_visible(self.move_card_form_loc, self.medium_wait, self.driver)
        assert move_card_header.is_displayed() == True, "move option is not present"
        move_card_header_text = move_card_header.text
        assert move_card_header_text.__contains__(input) == True, move_card_header_text + "text is not matched"

    def verify_board_name(self, input):
        board_name = self.wait_until_element_visible(self.board_name_text_loc, self.medium_wait, self.driver)
        assert board_name.is_displayed() == True, "move option is not present"
        board_name_text = board_name.text
        assert board_name_text.__contains__(input) == True, board_name_text + "text is not matched"

    def verify_list_name(self, input):
        list_name = self.wait_until_element_visible(self.list_name_text_loc, self.medium_wait, self.driver)
        assert list_name.is_displayed() == True, "move option is not present"
        list_name_text = list_name.text
        assert list_name_text.__contains__(input) == True, list_name_text + "text is not matched"

    def click_on_list(self,input):
        dropdown = self.driver.find_element(By.CSS_SELECTOR, "[class='js-select-list']")
        select = Select(dropdown)
        select.select_by_visible_text(input)

    def select_board(self,input):
        dropdown = self.driver.find_element(By.CSS_SELECTOR, "[class*='select-board']")
        select = Select(dropdown)
        select.select_by_visible_text(input)

    def click_on_move_button(self):
        list_name = self.wait_until_element_visible(self.move_button, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.move_button, self.medium_wait, self.driver)
        list_name.click()

    def move_cards_from_one_list_to_another_list(self, card_name, list_name, move, board, list):
        self.verify_card_details_window()
        self.verify_current_card_name(card_name)
        self.verify_current_list_name(list_name)
        self.verify_move_option()
        self.click_on_move_option()
        self.verify_move_card_form()
        self.verify_move_card_header(move)
        self.verify_board_name(board)
        self.verify_list_name(list_name)
        self.click_on_list(list)
        self.click_on_move_button()
        self.click_on_close_window()

    def click_on_edit_button_of_list(self, input):
        loc = (By.XPATH, "//textarea[@aria-label='"+input+"']//parent::div//following-sibling::button")
        edit_button = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(loc, self.medium_wait, self.driver)
        edit_button.click()

    def click_on_move_list(self):
        move_list = self.wait_until_element_visible(self.move_list_option_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.move_list_option_loc, self.medium_wait, self.driver)
        move_list.click()

    def verify_form_header(self, input):
        header = self.wait_until_element_visible(self.form_header_loc, self.medium_wait, self.driver)
        header_text = header.text
        assert header_text == input, header_text + "text is not matched"

    def verify_the_board_name(self, input):
        time.sleep(3)
        board_name = self.wait_until_element_visible(self.board_name_loc, self.medium_wait, self.driver)
        board_name_text = board_name.text
        assert board_name_text.__contains__(input) == True, board_name_text + "board name is not matched"

    def click_on_edit_and_move_list(self, list_name, actions, move, board):
        self.click_on_edit_button_of_list(list_name)
        self.verify_form_header(actions)
        self.click_on_move_list()
        self.verify_form_header(move)
        self.select_board(board)
        self.click_on_move_button()

    def move_cards_from_one_board_to_another_board(self, card_name, list_name, move, board):
        self.verify_card_details_window()
        self.verify_current_card_name(card_name)
        self.verify_current_list_name(list_name)
        self.verify_move_option()
        self.click_on_move_option()
        self.verify_move_card_form()
        self.verify_move_card_header(move)
        self.select_board(board)
        self.click_on_move_button()

    def click_on_template_button(self, list):
        self.driver.refresh()
        loc = (By.XPATH, "//h2[text()='"+list+"']//ancestor::div[@data-testid='list']//button[contains(@data-testid,'template')]")
        template_button = self.wait_until_element_visible(loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(loc, self.long_wait, self.driver)
        template_button.click()
        time.sleep(5)

    def verify_card_template_header(self, input_text):
        card_template = self.wait_until_element_visible(self.card_template_header_loc, self.long_wait, self.driver)
        card_template_text = card_template.text
        assert card_template_text == input_text, card_template_text + " header is not matched"

    def click_on_crate_new_template_button(self):
        crate_new_template_button = self.wait_until_element_visible(self.create_a_new_template_button_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.create_a_new_template_button_loc, self.medium_wait, self.driver)
        crate_new_template_button.click()

    def enter_template_title(self, title):
        template_title = self.wait_until_element_visible(self.template_title_input_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.template_title_input_loc, self.medium_wait, self.driver)
        template_title.send_keys(title)

    def click_on_add_button(self):
        add_button = self.wait_until_element_visible(self.add_button_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.add_button_loc, self.medium_wait, self.driver)
        add_button.click()

    def verify_template_card_name(self):
        time.sleep(5)
        template_card_name = self.wait_until_element_presence(self.created_template_name_text_loc, self.medium_wait, self.driver)
        assert template_card_name.is_displayed() == True, "text is not displayed"
        self.click_on_close_window()

    def click_on_create_card_from_template_button(self):
        create_card_from_template_button = self.wait_until_element_visible(self.create_card_from_template_button_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.create_card_from_template_button_loc, self.medium_wait, self.driver)
        create_card_from_template_button.click()

    def verify_create_card_from_template_header(self, input_text):
        create_card_from_template = self.wait_until_element_visible(self.create_card_from_template_header_loc, self.medium_wait, self.driver)
        create_card_from_template_text = create_card_from_template.text
        assert create_card_from_template_text == input_text, create_card_from_template_text + " header is not matched"

    def verify_card_from_template_textarea(self, input_text):
        card_from_template_textarea = self.wait_until_element_visible(self.card_title_textarea_loc, self.medium_wait, self.driver)
        card_from_template_textarea_text = card_from_template_textarea.text
        assert card_from_template_textarea_text == input_text, card_from_template_textarea_text + " header is not matched"
        self.wait_until_element_visible(self.card_title_textarea_loc, self.medium_wait, self.driver)
        card_from_template_textarea.click()
        card_from_template_textarea.send_keys(" card")

    def click_on_create_card_button(self):
        create_card_button = self.wait_until_element_visible(self.crate_card_button_loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(self.crate_card_button_loc, self.medium_wait, self.driver)
        create_card_button.click()

    def click_on_template_card_name(self, input):
        loc = (By.XPATH, "//a[text()='"+input+"']")
        card_name = self.wait_until_element_visible(loc, self.medium_wait, self.driver)
        self.wait_until_element_clickable(loc, self.medium_wait, self.driver)
        card_name.click()

    def click_on_hide_from_list_button(self):
        hide_from_list_button = self.wait_until_element_visible(self.hide_from_list_button_loc, self.medium_wait, self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", hide_from_list_button)
        self.wait_until_element_clickable(self.hide_from_list_button_loc, self.medium_wait, self.driver)
        hide_from_list_button.click()

    def verify_template_card_name_under_list(self, input):
        loc = (By.XPATH, "//a[text()='" + input + "']")
        template_card_name = self.is_Element_invisible(loc, self.medium_wait, self.driver)
        assert template_card_name == True, "card is not hide from the list"
