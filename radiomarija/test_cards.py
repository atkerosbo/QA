from selenium import webdriver
from selenium.webdriver.common.by import By
<<<<<<< Updated upstream

from royale.pages.card_details_page import CardDetailsPage
from royale.pages.cards_page import CardsPage

=======
>>>>>>> Stashed changes
PATH = "C:\Program Files (x86)\chromedriver.exe"

def test_ice_spirit_displayed():
    driver = webdriver.Chrome(PATH)
<<<<<<< Updated upstream
    driver.get('https://statsroyale.com')

    cards_page = CardsPage(driver)
    cards_page.goto()
    ice_spirit = cards_page.get_card_by_name('Ice Spirit')
    assert  ice_spirit.is_displayed()
=======
    #1. go to statsorayle.com
    driver.get('https://statsroyale.com')
    #2. go to cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    #3. assert if Ice spirit card is displayed
    ice_spirit_cards = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    assert ice_spirit_cards.is_displayed()

>>>>>>> Stashed changes

def test_ice_spirit_details_displayed():
    driver = webdriver.Chrome(PATH)
    # 1. go to statsorayle.com
<<<<<<< Updated upstream
    # 2. go to cards page
    # 3. go to Ice spirit card page
    CardsPage(driver).goto().get_card_by_name('Ice Spirit').click()

    #4. get the card name, type, arena, rarity
    details_page = CardDetailsPage(driver)
    card_name = details_page.map.card_name.text
    split = details_page.map.card_category.split(', ')
    card_type = split[0]
    card_arena = split[1]
    card_rarity = details_page.map.card_category.text.split('\n')[1]
=======
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
>>>>>>> Stashed changes
    #5. assert they are correct

    assert card_name == 'Ice Spirit'
    assert card_type == 'Troop'
    assert card_arena == 'Arena 8'
    assert card_rarity == 'Common'
<<<<<<< Updated upstream


def test_mirror_details_displayed():
    driver = webdriver.Chrome(PATH)
    # 1. go to statsorayle.com
    # 2. go to cards page
    # 3. go to Ice spirit card page
    CardsPage(driver).goto().get_card_by_name('Mirror').click()

    #4. get the card name, type, arena, rarity
    card = CardDetailsPage(driver).get_base_card()

    #5. assert they are correct

    assert card.name == 'Mirror'
    assert card.typee == 'Spell'
    assert card.arena == 12
    assert card.rarity == 'Epic'
=======
>>>>>>> Stashed changes
