from royale.pages.headernav import HeaderNav
class PageBase:
    def __int__(self,driver):
        self.headernav = HeaderNav(driver)