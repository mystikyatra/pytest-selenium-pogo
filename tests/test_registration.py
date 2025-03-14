import pytest
import selenium.webdriver.common.by as By
from config.config import Config
from pages.registration_page import RegistrationPage
from utils.driver_factory import DriverFactory

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver("chrome")
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

def test_user_registration(driver):
    registration_page = RegistrationPage(driver)
    
    registration_page.register_user(
        country="Nepal",
        month="May",
        day=5,
        year=1990,
        email="mystikyatra@gmail.com",
        ea_id="mystikyatra",
        password="Test@123",
        visibility="My friends", 
        email_verify_code="copy code from email"
    )
    
    # Verify successful registration
    user_dashboard = driver.find_element(By.XPATH, '//*[@id="pageContent"]/header/div[2]/div/div[4]/div[1]/div/div/img').click()
    assert "Success" in user_dashboard, "User registered successfully"
