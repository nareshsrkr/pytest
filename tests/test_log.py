import requests
import pytest
from test_rcst_setting import Config

log_url=Config.log
response=requests.get(log_url)

#PageStatus Check
def test_log_status():
    assert response.status_code == 200, "log endpoint not availale"

#Authorization Check
def test_log_auth():
    assert response.headers.__contains__("Authorization") == True, "Authorization Token not found"

#Response Check
def test_log_responsecheck():
    assert type(response.json()) is dict, "Return type is expected to be Dictionary, Please check or change the testcase inputs"
    assert type(response.json()['data']) is dict, "Data in Json output is expected to be dictionary, Please validate"
    assert len(response.json()['data']) > 0, "Status endpoint data result  is empty, Please validate"
    assert type(response.json()['data']['log']) is list, "data->log resultset is expected to be list, Please validate"
    assert len(response.json()['data']['log']) > 0, "No data found in log resultset, Please check"