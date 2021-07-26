import requests
import pytest
from test_rcst_setting import Config

jobhistory_url=Config.jobhistory
response=requests.get(jobhistory_url)

#PageStatus Check
def test_getjobs_status():
    assert response.status_code == 200, "Job History page not availale"

#Authorization Check
def test_getjobs_auth():
    assert response.headers.__contains__("Authorization") == True, "Authorization Token not found"

#Reponse Check
def test_getjobs_responsecheck():
    assert type(response.json()) is list, "Return type is expected to be list, Please check or change the testcase inputs"
    assert len(response.json()) > 0, "Job history results is empty, Please validate"
    assert len(response.json()[0].keys()) == 25, "No of keys in Jobhistory dict is higher/lower than expected, Please validate"
    dict_keys=['vin_rcost_request_id', 'vin_requestId', 'vin_vectorName', 'vin_submission_timestamp', 'vin_requesting_system', 'vin_callback_url', 'job_parentRequestId', 'job_parentUrl', 'job_rootId', 'job_rootUrl', 'job_createdBy', 'job_currentStatus', 'vin_target_organism', 'job_comment_createdOn', 'job_comment_createdBy', 'vas_vector_status', 'vas_source_allergenic_status', 'vas_allergen', 'vas_toxin', 'vas_celiac', 'vas_perception', 'vas_perception_short', 'vas_toxin_short', 'vas_micro_orfs', 'vas_gc_percent_calc']
    for key in dict_keys:
        assert key in response.json()[0].keys(), "Previously existing key: "+ key + " not found in the response"



