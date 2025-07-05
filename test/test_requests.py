import pytest
from georeport import GeoReport
from time import sleep

@pytest.fixture(autouse=True)
def wait_between_tests():
    sleep(1.5)

class TestRequests:
    client = GeoReport('http://test311api.cityofchicago.org/open311/v2')

    def test_get_requests(self):
        self.client.get_service_requests()

    def test_get_request(self):
        self.client.get_service_request('SR25-00000001')

