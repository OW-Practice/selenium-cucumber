from selenium.webdriver.common.by import By


class TemplateCardsLoc:
    card_template_header_loc = (By.CSS_SELECTOR, "[title='Card templates']")
    create_a_new_template_button_loc = (By.CSS_SELECTOR, "[data-testid*='new-template']")
    template_title_input_loc = (By.CSS_SELECTOR, "[placeholder='Template title']")
    add_button_loc = (By.CSS_SELECTOR, "[data-testid*='submit-button']")
    template_card_header_loc = (By.CSS_SELECTOR, "[data-testid*='template-card'] div h3")
    created_template_name_text_loc = (By.CSS_SELECTOR, "textarea[class*='detail-title']")
    create_card_from_template_button_loc = (By.CSS_SELECTOR, "span[data-testid='TemplateCreateIcon']")
    create_card_from_template_header_loc = (By.CSS_SELECTOR, "[title*='Create']")
    card_title_textarea_loc = (By.CSS_SELECTOR, "[data-testid='card-title-textarea']")
    crate_card_button_loc = (By.CSS_SELECTOR, "[data-testid='create-card-from-template-button']")
    hide_from_list_button_loc = (By.CSS_SELECTOR, "[title='Hide from list']")



