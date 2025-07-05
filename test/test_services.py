import pytest
from georeport import GeoReport
from time import sleep

@pytest.fixture(autouse=True)
def wait_between_tests():
    sleep(1.5)

class TestServices:
    client = GeoReport('http://test311api.cityofchicago.org/open311/v2')

    def test_get_service_list(self):
        assert len(self.client.get_service_list()) == 123

    def test_get_service_definition(self):
        assert self.client.get_service_definition('65eb9968e9c601284100e331')['service_code'] == '65eb9968e9c601284100e331'
