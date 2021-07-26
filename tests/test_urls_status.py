import requests
import pytest
from test_rcst_setting import Config


download_endpoint=Config.download
qtrack_endpoint=Config.qtrack
home=Config.host

endpoints = [home,download_endpoint,qtrack_endpoint]
@pytest.mark.parametrize('endpoint', endpoints)
def test_get_all_endpoints(endpoint):
    response = requests.get(endpoint)
    assert response.status_code == 200,"Endpoint "+endpoint+" not reachable"
    assert response.headers.__contains__("Authorization") == True, "Authorization Token not found"