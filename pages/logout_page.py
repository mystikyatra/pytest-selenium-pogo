from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LogOutPage(BasePage):
    PROFILE_PAGE = (By.CSS_SELECTOR, 'img[alt="Avatar Image"]')
    SIGN_OUT = (By.XPATH, '//button[div[text()="Sign Out"]]')

    CONTINUE = (By.XPATH, '//button[div[text()="Continue"]]')

    def logout(self):
        self.click(self.PROFILE_PAGE)
        self.click(self.SIGN_OUT)
        self.click(self.CONTINUE)