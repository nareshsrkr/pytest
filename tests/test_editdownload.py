import requests
import pytest
from test_rcst_setting import Config

edit_download=Config.edit_download
payload = "{\r\n\"api_version\": 0.1,\r\n    \"data\": {\r\n \"request\": {\r\n \"requesting_users\": [\r\n \"nareshbabu.nimmala@corteva.com\"\r\n ],\r\n \"target_organism\": \"3736\",\r\n \"region_to_analyze\": {\r\n \"coordinates\": [\r\n  [\r\n  1,\r\n  1716\r\n  ]\r\n ]\r\n },\r\n \"program_id_name\": \"\",\r\n \"requesting_system\": \"RCOSTManualInterface.edited\",\r\n \"submission_timestamp\": \"2021-07-16T11:34:53.547444Z\",\r\n \"vector_type\": \"\",\r\n \"RCOST_request_id\": \"ePolnNw\",\r\n \"JobMasterData\": {\r\n \"parentVectorId\": \"test_ART-G3NUP16.e1\",\r\n \"vectorId\": \"test_ART-G3NUP16.e1\",\r\n \"parentRequestId\": \"YdSuyB9\",\r\n \"requestId\": null,\r\n \"createdBy\": \"Nimmala, Nareshbabu\"\r\n }\r\n },\r\n \"DNA_segment\": {\r\n \"features\": [\r\n {\r\n  \"feature_type\": \"CDS\",\r\n  \"coordinates\": [\r\n  [\r\n  1,\r\n  1716\r\n  ]\r\n  ],\r\n  \"label\": \"ART-G3NUP16\",\r\n  \"identifier\": \"F00001\",\r\n  \"source_organism\": \"\",\r\n  \"strand\": \"forward\",\r\n  \"name\": \"ART-G3NUP16\"\r\n }\r\n ],\r\n \"vector_id\": \"test_ART-G3NUP16.e2\",\r\n \"biosequence\": {\r\n \"sequence_topology\": \"linear\",\r\n \"sequence_type\": \"DNA\",\r\n \"sequence\": \"ATGACT\"\r\n }\r\n }\r\n}\r\n}"
response = requests.request("POST", edit_download, data=payload)

def test_post_editdownload_endpoint():
    assert response.status_code == 200, "/editdownload endpoint not reachable/working"
