from selenium.webdriver.common.by import By


class VisionLocators:
    vision_header_loc = (By.CSS_SELECTOR, "[title='Oracle Logo Home']")
    setting_actions_img_loc = (By.CSS_SELECTOR, "img[title='Settings and Actions']")
    navigation_ham_burger_loc = (By.CSS_SELECTOR, "[title ='Navigator']")
    home_header_loc = (By.XPATH, "//span[text()='Home']")