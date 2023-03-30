from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.nordweb.rs/")
print(driver.title)
