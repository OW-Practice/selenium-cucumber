from selenium.webdriver.common.by import By


class DeleteBoardLoc:
    board_is_closed_text_loc = (By.CSS_SELECTOR, "h1[data-testid*='message']")
    re_open_board_loc = (By.CSS_SELECTOR, "[data-testid*='reopen'] button")
    permanently_delete_board_loc = (By.CSS_SELECTOR, "[data-testid*='delete']")
    delete_board_pop_up_loc = (By.CSS_SELECTOR, "section.js-react-root")
    delete_board_header_loc = (By.CSS_SELECTOR, "[title='Delete board?']")
    delete_board_content_loc = (By.CSS_SELECTOR, "section.js-react-root div")
    delete_button_loc = (By.CSS_SELECTOR, "section.js-react-root div button")
    delete_board_text_loc = (By.XPATH, "//span[text()='Board deleted.']")



