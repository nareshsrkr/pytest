import requests
import pytest
from test_rcst_setting import Config

status_url=Config.status
response=requests.get(status_url)

#PageStatus Check
def test_status_status():
    assert response.status_code == 200, "Status endpoint not availale"

#Authorization Check
def test_status_auth():
    assert response.headers.__contains__("Authorization") == True, "Authorization Token not found"

#Response Check
def test_status_responsecheck():
    assert type(response.json()) is dict, "Return type is expected to be Dictionary, Please check or change the testcase inputs"
    assert type(response.json()['data']) is dict, "Data in Json output is expected to be dictionary, Please validate"
    assert len(response.json()['data']) > 0, "Status endpoint data result  is empty, Please validate"
    dict_keys = ['status', 'results_URL', 'results_WS_URL', 'RCOST_request_id', 'log_URL']
    for key in dict_keys:
        assert key in response.json()['data'].keys(), "Previously existing key: " + key + " not found in the response"