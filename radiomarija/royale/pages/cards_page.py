from selenium.webdriver.common.by import By
from royale.pages.base.pagebase import PageBase
class CardsPage:
    def __init__(self,driver):
        super().__init__(driver)
        self.map = CardsPageMap(driver)

    def goto(self):
        self.headernav.goto_cards_page()



class CardsPageMap:
    def __init__(self,driver):
        self._driver = driver

    @property
    def ice_spirit_card(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")