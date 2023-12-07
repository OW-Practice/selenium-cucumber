from selenium.webdriver.common.by import By


class CreateBoardLocators:
    create_form_loc = (By.CSS_SELECTOR, "section[data-testid*='menu']")
    create_board_header_loc = (By.CSS_SELECTOR, "[title*='Create']")
    board_title_field_loc = (By.CSS_SELECTOR, "input[data-testid*='create']")
    create_button_loc = (By.XPATH, "//button[text()='Create']")
    board_name_loc = (By.CSS_SELECTOR, "h1[data-testid*='name']")
    add_board_icon_loc = (By.CSS_SELECTOR, "h2[aria-label*='Your boards']+div [aria-label='Add board']")


