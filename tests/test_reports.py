import requests,sys
import pytest
from test_rcst_setting import Config

report_endpoint=Config.report

def test_post_report_endpoint():
    payload_csv = "{\"username\":\"nareshbabu.nimmala@corteva.com\",\"full_name\":\"Naresh Babu Nimmala\",\"emailid\":\"nareshbabu.nimmala@corteva.com\",\"vector_ids\":[\"test_ART-G3NUP16\"],\"report_format\":\"csv\"}"
    response_csv = requests.request("POST", report_endpoint, data=payload_csv)
    assert response_csv.status_code == 200, "/report endpoint to download data is not reachable/working"

    payload_view = "{\"username\":\"nareshbabu.nimmala@corteva.com\",\"full_name\":\"Naresh Babu Nimmala\",\"emailid\":\"nareshbabu.nimmala@corteva.com\",\"vector_ids\":[\"test_ART-G3NUP16\"],\"report_format\":\"json\"}"
    response_view = requests.request("POST", report_endpoint, data=payload_view)
    assert response_view.status_code == 200, "/report endpoint to view vector data is not reachable/working"
    assert type(response_view.json()) is dict, "Return type is expected to be dictionat, Please validate and change test case if required"
    assert len(response_view.json()['report'][0]) > 0, "Report resultset is empty, Expected data is changed, Please validate"
    dict_keys=['submission_date', 'vector_status', 'vector_id']
    for key in  dict_keys:
        assert key in response_view.json()['report'][0].keys(),"Expected dict keys not found in resultset from /report endpoint"
    sys.exit()