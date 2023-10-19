from behave import *
from pages.job_requisitions_page import JobRequisitionsPage


@then(u'Validate job requisitions header "{job_requisition_header}"')
def validate_job_requisitions_header(context,job_requisition_header):
    context.job = JobRequisitionsPage(context.driver)
    context.job.verify_job_requisitions_header(job_requisition_header)


@then(u"Validate candidate search option")
def validate_candidate_search_option(context):
    context.job = JobRequisitionsPage(context.driver)
    context.job.verify_candidate_search_option()


@when(u"Click on candidate search option")
def click_on_candidate_search_option(context):
    context.job = JobRequisitionsPage(context.driver)
    context.job.click_on_candidate_search_option()


@then(u"Validate candidate search header")
def validate_candidate_search_header(context):
    context.job = JobRequisitionsPage(context.driver)
    context.job.verify_candidate_search_header()


@then(u"Validate search button")
def validate_search_button(context):
    context.job = JobRequisitionsPage(context.driver)
    context.job.verify_the_search_button()


@when(u"Click on search button")
def click_on_search_button(context):
    context.job = JobRequisitionsPage(context.driver)
    context.job.click_on_search_button()