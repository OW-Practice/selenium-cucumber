from selenium.webdriver.common.by import By


class JobRequisitionLocators:
    job_requisitions_header_loc = (By.CSS_SELECTOR, "[title='Job Requisitions'] h1")
    candidate_search_loc = (By.XPATH, "//div[text()='Candidate Search']")
    search_loc = (By.CSS_SELECTOR, "[title='Search'] a")
    candidate_search_header_loc = (By.XPATH, "//h1[text()='Candidate Search']")