import pytest
from utils.driver_factory import DriverFactory
from config.config import Config

@pytest.fixture
def setup():
    driver = DriverFactory.get_driver("chrome")
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()