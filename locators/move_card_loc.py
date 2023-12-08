from selenium.webdriver.common.by import By


class MoveCard:
    move_button_loc = (By.CSS_SELECTOR, "[title='Move'] span+span")
    move_card_form_loc = (By.CSS_SELECTOR, "[class='no-back']")
    move_card_header_loc = (By.CSS_SELECTOR, "span[class*='header-title']")
    board_name_text_loc = (By.CSS_SELECTOR, "select[data-testid*='board'] option[selected='selected']")
    list_loc = (By.CSS_SELECTOR, "[class='js-select-list']")
    list_name_text_loc = (By.CSS_SELECTOR, "[class='label']+span[class*='list-value']")
    move_button = (By.CSS_SELECTOR, "[value='Move']")

