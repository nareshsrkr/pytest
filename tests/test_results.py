import requests
import pytest
from test_rcst_setting import Config

results_url=Config.results
response=requests.get(results_url)

#PageStatus Check
def test_results_status():
    assert response.status_code == 200, "results endpoint not available"

#Authorization Check
def test_results_auth():
    assert response.headers.__contains__("Authorization") == True, "Authorization Token not found"

#Response Check
def test_results_responsecheck():
    assert type(response.json()) is dict, "Return type is expected to be Dictionary, Please check or change the testcase inputs"
    assert type(response.json()['data']) is dict, "Data in Json output is expected to be dictionary, Please validate"
    assert len(response.json()['data']) > 0, "results endpoint data result  is empty, Please validate"
    assert type(response.json()['data']['results']['outputs']) is list,"Date->results->outputs resultset is expected to be dictionary"
    assert type(response.json()['data']['input']) is dict,"Date->results->inputs resultset is expected to be dictionary"
    output_dict_keys=['status', 'unintended_orf_status', 'GC_percent', 'df_status_id', 'source', 'RCST_output', 'type', 'id', 'df_status']
    for output_key in output_dict_keys:
        assert output_key in response.json()['data']['results']['outputs'][0]['dnasequence'].keys(),"Previously existing key: " + key + " not found in the response"
    response.json()['data']['results']['outputs'][0]['dnasequence'].keys()
    input_dict_keys = ['request', 'DNA_segment']
    for input_key in input_dict_keys:
        assert input_key in response.json()['data']['input'].keys(), "Previously existing key: " + input_key + " not found in the response"
