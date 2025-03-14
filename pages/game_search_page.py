from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class GameSearch(BasePage):
    SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Search for games"]')
    GAME_THUMBNAIL = (By.XPATH, '//a[contains(@href, "/games/snowbird-solitaire") and contains(text(), "Snowbird Solitaire")]')
    SEARCH_TOOLTIP = (By.XPATH, '//div[contains(@class, "copy__R67Vc") and contains(text(), "Search For Games By Title Or Category")]')

    def search_for_game(self, game_name):
        search_box = self.find_element(self.SEARCH_INPUT)
        search_box.clear()
        search_box.send_keys(game_name)
        search_box.send_keys(Keys.ENTER)
    
    def verify_game_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.GAME_THUMBNAIL))
    
    def verify_tooltip_displayed(self):
        tooltip = self.wait.until(EC.visibility_of_element_located(self.SEARCH_TOOLTIP))
        return tooltip.is_displayed() and "Search For Games By Title Or Category" in tooltip.text
