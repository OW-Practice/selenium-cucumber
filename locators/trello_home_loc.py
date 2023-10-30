from selenium.webdriver.common.by import By


class TrelloHomeLocators:
    trello_header_loc = (By.CSS_SELECTOR, "nav#header a")
    yours_work_space_section_loc = (By.CSS_SELECTOR, "h3[class*='page-section']")
    show_menu_button_loc = (By.CSS_SELECTOR, "[aria-label='Show menu']")
    show_header_loc = (By.CSS_SELECTOR, "h3[class*='menu']")
    close_board_option_loc = (By.CSS_SELECTOR, "a.js-close-board")
    close_board_pop_up_loc = (By.CSS_SELECTOR, ".pop-over")
    close_board_header_loc = (By.CSS_SELECTOR, "span[class*='title']")
    close_button_loc = (By.CSS_SELECTOR, "[value='Close']")
    pop_over_content_loc = (By.CSS_SELECTOR, "div.pop-over-content p")
    work_space_loc = (By.XPATH, "//div[text()='Workspaces']")


