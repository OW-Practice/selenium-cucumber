from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SynMethods:
    short_wait = 10
    medium_wait = 65
    long_wait = 170

    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_visible(self, loc, timeout, driver):
        # try:
        webdriver_wait = WebDriverWait(driver, timeout)
        return webdriver_wait.until(EC.visibility_of_element_located(loc))

    def wait_until_element_presence(self, loc, timeout, driver):
        webdriver_wait = WebDriverWait(driver, timeout)
        return webdriver_wait.until(EC.presence_of_element_located(loc))

    def wait_until_element_clickable(self, loc, timeout, driver):
        webdriver_wait = WebDriverWait(driver, timeout)
        return webdriver_wait.until(EC.element_to_be_clickable(loc))

    def wait_until_text_present(self, loc, timeout, driver, text):
        webdriver_wait = WebDriverWait(driver, timeout)
        return webdriver_wait.until(EC.text_to_be_present_in_element(loc, text))

    def visibility_of_element_located(self, loc, timeout, driver):
        webdriver_wait = WebDriverWait(driver, timeout)
        return webdriver_wait.until(EC.element_to_be_clickable(loc))

    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def switch_to_new_tab(self):
        self.driver.maximize_window()
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])

    def is_element_visible(self, loc, timeout, driver):
        isPresent = True
        try:
            webdriver_wait = WebDriverWait(driver, timeout)
            ele = webdriver_wait.until(EC.presence_of_element_located(loc))
        except:
            isPresent = False
        return isPresent

    def is_Element_invisible(self, loc, timeout, driver):
        iselement = True
        try:
            webdriver_wait = WebDriverWait(driver, timeout)
            ele = webdriver_wait.until(EC.invisibility_of_element(loc))
        except:
            iselement = False
        return iselement
