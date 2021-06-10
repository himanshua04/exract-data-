from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from os import path
import json
import logging
import pytest

TYPE_OF_LOCATORS = {
    'css': By.CSS_SELECTOR,
    'css selector': By.CSS_SELECTOR,
    'id': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME
}


def wait_for_page_to_load(timeout,url):
    try:
        WebDriverWait(pytest.driver, timeout).until(EC.url_contains(url))
    except TimeoutException:
        pass
    

def is_element_present(loc_pair, timeout=5):
    loc_pair[0] = TYPE_OF_LOCATORS[loc_pair[0].lower()]
    if not isinstance(loc_pair, tuple):
        loc_pair = tuple(loc_pair)
    
    try:
        WebDriverWait(pytest.driver, timeout).until(
            EC.presence_of_element_located(loc_pair)
        )
        return True
    except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
        logging.error(e)
        logging.warning(f"the locator {loc_pair} on url {pytest.driver.current_url} is not present")
    return False
