from selenium.webdriver.common.by import By


class MyClientGroupsLocators:
    my_client_groups_text_loc = (By.CSS_SELECTOR, "[title ='My Client Groups']>div>span")
    my_client_group_drop_down_loc = (By.CSS_SELECTOR, "[title ='My Client Groups']")
    my_client_groups_form_loc = (By.XPATH, "// *[ @ title ='My Client Groups'] /../..")
    hiring_option_loc = (By.XPATH, "//*[@title='My Client Groups']/../..//span[text()='Hiring']")
    hiring_option_logo_loc = (By.XPATH, "//*[contains(@id,'Recruiting_Hiring::icon')]")
