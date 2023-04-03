PATH = "C:\Program Files (x86)\chromedriver.exe"
import pytest
from selenium import webdriver

from royale.pages.card_details_page import CardDetailsPage
from royale.pages.cards_page import CardsPage
from royale.services import card_service

cards =card_service.get_all_cards()


@pytest.mark.parametrize('api_card', cards)
def test_card_is_displayed(api_card):
    driver = webdriver.Chrome(PATH)
    driver.get('https://statsroyale.com')

    cards_page = CardsPage(driver).goto()
    card_on_page = cards_page.get_card_by_name(api_card.name)
    assert  card_on_page.is_displayed()

@pytest.mark.parametrize('api_card', cards)
def test_ice_spirit_details_displayed(api_card):
    driver = webdriver.Chrome(PATH)
    # 1. go to statsorayle.com
    # 2. go to cards page
    # 3. go to Ice spirit card page
    CardsPage(driver).goto().get_card_by_name(api_card.name).click()

    #4. get the card name, type, arena, rarity
    details_page = CardDetailsPage(driver)
    card_name = details_page.map.card_name.text
    split = details_page.map.card_category.split(', ')
    card_type = split[0]
    card_arena = split[1]
    card_rarity = details_page.map.card_category.text.split('\n')[1]
    #5. assert they are correct

    assert card_name == api_card.name
    assert card_type == api_card.type
    assert card_arena == api_card.arena
    assert card_rarity == api_card.rarity



def test_mirror_details_displayed():
    driver = webdriver.Chrome()
    # 1. go to statsorayle.com
    # 2. go to cards page
    # 3. go to Ice spirit card page
    CardsPage(driver).goto().get_card_by_name('Mirror').click()

    #4. get the card name, type, arena, rarity
    card = CardDetailsPage(driver).get_base_card()

    #5. assert they are correct

    assert card.name == 'Mirror'
    assert card.type == 'Spell'
    assert card.arena == 12
    assert card.rarity == 'Epic'