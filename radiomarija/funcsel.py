from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


domain = input()
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.nordweb.rs/")
sleep(10)    
driver.find_element(By.CLASS_NAME, "btn search").submit
sleep(10)   
driver.find_element(By.CLASS_NAME, "form-control").send_keys(domain)
sleep(10)
driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click
sleep(10)
driver.find_element(By.ID, "btnCheckAvailability").submit
sleep(10)
rezultat = driver.find_element(By.ID, "primaryLookupResult")
sleep(10)


print(rezultat)
