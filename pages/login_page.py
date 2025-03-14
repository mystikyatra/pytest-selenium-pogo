from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    SIGN_IN_BUTTON = (By.XPATH, '//button[div[text()="Sign In"]]')

    
    USERNAME_INPUT = (By.ID, "email")
    LOGIN_BUTTON = (By.ID, "logInBtn")

    PASSWORD_INPUT = (By.ID, "password")

    def login(self, username, password):
        self.click(self.SIGN_IN_BUTTON)
        self.enter_text(self.USERNAME_INPUT, username)
        self.click(self.LOGIN_BUTTON)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)