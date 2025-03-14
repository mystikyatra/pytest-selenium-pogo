from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    # Locators
    REGISTER_BUTTON = (By.XPATH, '//button[div[text()="Register free"]]')
    
    COUNTRY_DROPDOWN = (By.NAME, "country")
    
    DOB_MONTH_DROPDOWN = (By.NAME, "dobMonth")
    DOB_DAY_DROPDOWN = (By.NAME, "dobDay")
    DOB_YEAR_DROPDOWN = (By.NAME, "dobYear")

    NEXT_BUTTON = (By.ID, "panel-action-area-container")

    EMAIL_FIELD = (By.NAME, "email")
    EA_ID = (By.NAME, "originId")
    PASSWORD = (By.NAME, "password")
    NEXT_BUTTO = (By.ID, "basicInfoNextBtn")

    PROFILE_VISIBILITY = (By.ID, "friend_visibility_selctrl")
    TERMS_CHECKBOX = (By.ID, "readAccept")
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="submitBtn"]')

    EMAIL_VERIFY_CODE = (By.NAME, "emailVerifyCode")
    SEND_CODE_BUTTON = (By.ID, "id=btnSendCode")

    SCREEN_NAME = (By.ID, "screenname")
    SEND_NAME_NEXT = (By.XPATH, '//*[@id="pageContent"]/div[1]/div/div/button')

    START_PLAYING_POGO = (By.XPATH, '//*[@id="pageContent"]/div[1]/div/div[2]/button')
    REWARD_CONTINUE = (By.XPATH, '//*[@id="pageContent"]/div[1]/div/div[1]/div[3]/div/div/div[7]/button')
       
    def __init__(self, driver):
        super().__init__(driver)

    def select_country(self, country_name):
        dropdown = Select(self.find(self.COUNTRY_DROPDOWN))
        dropdown.select_by_visible_text(country_name)

    def select_dob(self, month, day, year):
        Select(self.find(self.DOB_MONTH_DROPDOWN)).select_by_visible_text(month)
        Select(self.find(self.DOB_DAY_DROPDOWN)).select_by_visible_text(str(day))
        Select(self.find(self.DOB_YEAR_DROPDOWN)).select_by_visible_text(str(year))
    
    def select_profile_visibility(self, visibility):
        Select(self.find(self.PROFILE_VISIBILITY)).select_by_value(visibility)
    
    def terms_checkbox(self):
        self.find(self.TERMS_CHECKBOX).click()
    
    def email_verify_code(self, email_verify_code):
        self.find(self.EMAIL_VERIFY_CODE).send_keys(email_verify_code)
    
    def send_name_next(self):
        self.find(self.SEND_NAME_NEXT).click()

    def register_user(self, country, month, day, year, email, ea_id, password, visibility, email_verify_code):
        self.click(self.REGISTER_BUTTON)
        self.select_country(country)
        self.select_dob(month, day, year)
        self.click(self.NEXT_BUTTON)
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.EA_ID, ea_id)
        self.enter_text(self.PASSWORD, password)
        self.click(self.NEXT_BUTTO)
        self.select_profile_visibility(visibility)
        self.terms_checkbox()
        self.click(self.SUBMIT_BUTTON)
        self.email_verify_code(email_verify_code)
        self.click(self.SEND_CODE_BUTTON)
        self.enter_text(self.SCREEN_NAME, ea_id)
        self.click(self.SEND_NAME_NEXT)
        self.click(self.START_PLAYING_POGO)
        self.click(self.REWARD_CONTINUE)