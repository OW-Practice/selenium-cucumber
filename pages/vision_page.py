from locators.vision_locators import VisionLocators
from utilities.syn_methods import SynMethods
import time


class VisionPage(SynMethods,VisionLocators):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_vision_header(self):
        time.sleep(4)
        vision = self.wait_until_element_visible(self.vision_header_loc, self.long_wait, self.driver)
        assert vision.is_displayed() == True, "user is not logged in to application"

    def click_on_navigation_hamburger(self):
        ham_burger = self.wait_until_element_visible(self.navigation_ham_burger_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.navigation_ham_burger_loc, self.long_wait, self.driver)
        ham_burger.click()

    def verify_home_header(self):
        home = self.wait_until_element_visible(self.home_header_loc, self.long_wait, self.driver)
        assert home.is_displayed() == True, "home header is not displaying"

    def verify_setting_actions_img(self):
        setting_actions_img = self.wait_until_element_visible(self.setting_actions_img_loc, self.long_wait, self.driver)
        assert setting_actions_img.is_displayed() == True, "home header is not displaying"