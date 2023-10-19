from selenium.webdriver.common.by import By


class MyClientGroupsLocators:

    navigation_ham_burger_loc = (By.CSS_SELECTOR, "[title ='Navigator']")
    home_header_loc = (By.XPATH, "//span[text()='Home']")
    my_client_groups_text_loc = (By.CSS_SELECTOR, "[title ='My Client Groups']>div>span")
    my_client_group_drop_down_loc = (By.CSS_SELECTOR, "[title ='My Client Groups']")
    my_client_groups_form_loc = (By.XPATH, "// *[ @ title ='My Client Groups'] /../..")
    hiring_option_loc = (By.XPATH, "//*[@title='My Client Groups']/../..//span[text()='Hiring']")
    hiring_option_logo_loc = (By.XPATH, "//*[contains(@id,'Recruiting_Hiring::icon')]")
    job_requisitions_header_loc = (By.XPATH, "(//*[text()='Job Requisitions'])[3]")
    candidate_search_loc = (By.XPATH, "//div[text()='Candidate Search']")
    search_loc = (By.CSS_SELECTOR, "[title='Search'] span")
    candidate_search_header_loc = (By.XPATH, "//h1[text()='Candidate Search']")