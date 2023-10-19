from selenium.webdriver.common.by import By


class CandidateInfoLocators:
    add_candidate_loc = (By.CSS_SELECTOR, "[title='Create Candidate']")
    create_candidate_page_loc = (By.XPATH, "//*[text()='Create Candidate']")
    base_info_header_loc = (By.XPATH, "//*[text()='Basic Info']")
    confirmation_pop_up_loc = (By.XPATH, "//*[text()='Confirmation']")
    confirmation_text_loc = (By.XPATH, "//div[text()='The initial candidate info was saved. Do you want to complete the profile now?']")
    cancel_button_loc = (By.CSS_SELECTOR, "a[title='Cancel']")
    actions_drop_down_loc = (By.XPATH, "//span[text()='Actions']")
    actions_drop_down_form_loc = (By.CSS_SELECTOR, "table[role='menu']")
    add_to_requisitions_option = (By.XPATH, "//*[text()='Add to Requisition']")
    add_to_requisitions_header_loc = (By.CSS_SELECTOR, "[title='Add to Requisition'] h1")
    create_job_application_check_box_loc = (By.XPATH, "//input[@type='checkbox']/..")
    key_word_search_loc = (By.XPATH, "(//div[@title='Keyword Search'])[1]//input")
    select_requisitions_header_loc = (By.CSS_SELECTOR, "[title='Select Requisitions'] h2")
    select_requisitions_drop_down_loc = (By.CSS_SELECTOR, "[role='combobox']>input")
    select_requisitions_drop_down_form_loc = (By.CSS_SELECTOR, "[role='grid']")
    add_requisition_loc = (By.XPATH, "(//*[text()='Job Requisition']/ancestor::table//span)[1]")
    requisition_confirmation_text_loc = (By.XPATH, "//div[text()='Confirmation']/ancestor::div//div[text()='The candidates were added to the selected requisitions.']")