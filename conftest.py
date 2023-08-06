import logging
import pytest
log = logging.getLogger(__name__)

from reportportal_client import RPLogger


@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logging.setLoggerClass(RPLogger)
    return logger

@pytest.fixture(scope="session")
def setup():
    print("###########")
    log.info("Test Started")
    yield
    log.info("Test End")