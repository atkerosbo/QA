from selenium.webdriver.common.by import By

class HeaderNav:
    def __int__(self,driver):
        self.map = HeaderNavMap(driver)

    def goto_cards_page(self):
        self.map.cards_link.click()
class HeaderNavMap:
    def __int__(self,driver):
        self._driver = driver

    @property
    def cards_link(self):
        return self._driver.find.element(By.CSS_SELECTOR, "[href='/cards']")