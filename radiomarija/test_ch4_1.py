from selenium import webdriver
from selenium.webdriver.common.by import By
PATH = "C:\Program Files (x86)\chromedriver.exe"

def test_ice_spirit_displayed():
    driver = webdriver.Chrome(PATH)
    #1. go to statsorayle.com
    driver.get('https://statsroyale.com')
    #2. go to cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    #3. assert if Ice spirit card is displayed
    ice_spirit_cards = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    assert ice_spirit_cards.is_displayed()


def test_ice_spirit_details_displayed():
    driver = webdriver.Chrome(PATH)
    # 1. go to statsorayle.com
    driver.get('https://statsroyale.com')
    # 2. go to cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    # 3. go to Ice spirit card page
    driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']").click()
    #4. get the card name, type, arena, rarity
    card_name = driver.find_element(By.CSS_SELECTOR, "[class*='cardName']").text
    split = driver.find_element(By.CSS_SELECTOR, "[class*='card_rarity']").text.split(',')
    card_type = split[0]
    card_arena = split[1]
    card_rarity =  driver.find_element(By.CSS_SELECTOR, "[class*='rarityCaption']").text.split('\n')[1]
    #5. assert they are correct

    assert card_name == 'Ice Spirit'
    assert card_type == 'Troop'
    assert card_arena == 'Arena 8'
    assert card_rarity == 'Common'
