import pytest
import logging

log = logging.getLogger(__name__)

@pytest.mark.usefixtures("setup")
class TestSample:

    def test_sampleTest1(self,rp_logger):
        rp_logger.info("This is Sample Test 1")
        assert True

    def test_sampleTest2(self, rp_logger):
        rp_logger.info("This is sample Test 2")
        assert True