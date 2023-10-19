from locators.job_requision_locators import JobRequisitionLocators
from utilities.syn_methods import SynMethods


class JobRequisitionsPage(SynMethods, JobRequisitionLocators):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_job_requisitions_header(self,input):
        job_requisitions = self.wait_until_element_visible(self.job_requisitions_header_loc, self.long_wait, self.driver)
        assert job_requisitions.is_displayed() == True, "job requisitions header is not displayed"
        job_requisitions_text = job_requisitions.text
        print(".............",job_requisitions_text)
        assert job_requisitions_text == input, job_requisitions_text + "header is not matched"

    def verify_candidate_search_option(self):
        candidate_search = self.wait_until_element_visible(self.candidate_search_loc, self.long_wait, self.driver)
        assert candidate_search.is_displayed() == True, "candidate search option is not displayed"

    def click_on_candidate_search_option(self):
        candidate_search = self.wait_until_element_visible(self.candidate_search_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.candidate_search_loc, self.long_wait, self.driver)
        candidate_search.click()

    def verify_the_search_button(self):
        search = self.wait_until_element_visible(self.search_loc, self.long_wait, self.driver)
        assert search.is_displayed() == True, "Search button is not displayed"

    def click_on_search_button(self):
        search = self.wait_until_element_visible(self.search_loc, self.long_wait, self.driver)
        self.wait_until_element_clickable(self.search_loc, self.long_wait, self.driver)
        search.click()

    def verify_candidate_search_header(self):
        candidate_search = self.wait_until_element_visible(self.candidate_search_header_loc, self.medium_wait, self.driver)
        assert candidate_search.is_displayed() == True, "candidate search header is not displayed"