import pytest
from pages.game_search_page import GameSearch
from pages.login_page import LoginPage
from pages.logout_page import LogOutPage
from config.config import Config

@pytest.mark.order(1)
def test_valid_login_and_logout(setup):
    login_page = LoginPage(setup)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    game_search = GameSearch(setup)
    game_search.search_for_game("Solitaire")
    assert game_search.verify_game_displayed(), "Solitaire game is not displayed in search results!"

    # Game search tool tip.
    assert game_search.verify_tooltip_displayed(), "Tooltip message is not displayed or incorrect!"

    logout_page = LogOutPage(setup)
    logout_page.logout()