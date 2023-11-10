from selenium.webdriver.common.by import By


class AddListLocators:
    add_list_button_loc = (By.CSS_SELECTOR, "[id='board'] [data-testid='list-composer-button']")
    list_title_loc = (By.CSS_SELECTOR, "textarea[placeholder='Enter list title…']")
    add_list_button = (By.CSS_SELECTOR, "[id='board'] button[data-testid*='add-list-button']")
    enter_card_title_loc = (By.XPATH, "//ol[@data-testid='list-cards']/form/textarea")
    add_card_button = (By.XPATH, "//textarea[@data-testid='list-card-composer-textarea']//parent::form//button[text("
                                 ")='Add card']")
    card_details_window_loc = (By.CSS_SELECTOR, "[class*='card-detail-window']")
    actions_section_loc = (By.XPATH, "//h3[text()='Actions']//parent::div")
    archive_option_loc = (By.CSS_SELECTOR, "span[title='Archive']")
    delete_button_loc = (By.CSS_SELECTOR, "a[title='Delete']")
    delete_pop_up_loc = (By.XPATH, "//div//following-sibling::div[contains(@class,'pop-over')]")
    delete_header_loc = (By.CSS_SELECTOR, "span[class*='header-title']")
    delete_content_loc = (By.CSS_SELECTOR, "div[class*='pop-over-content'] p")
    confirm_delete_button_loc = (By.CSS_SELECTOR, "input[value='Delete']")
    current_card_name_loc = (By.XPATH, "//textarea[contains(@class,'card-detail-title')]")
    current_list_name_loc = (By.CSS_SELECTOR, "[class*='current-list'] a")
    list_actions_form_loc = (By.XPATH, "//div//following-sibling::div[contains(@class,'pop-over')]")
    description_input_loc = (By.XPATH, "//div[contains(@class,'editor-content-area')]//div[@role='textbox']")
    added_description_text_loc = (By.XPATH, "//p[@dir='auto']")
    close_window_loc = (By.CSS_SELECTOR, "a[class*='close-window']")
    attachment_button_loc = (By.CSS_SELECTOR, "[data-testid='Image']")
    upload_loc = (By.CSS_SELECTOR, "label[for='filepicker']")
    success_text_loc = (By.XPATH, "//span[text()='Success']")
    close_select_img_pop_up_loc = (By.XPATH, "(//span[@data-testid='CloseIcon'])[1]")