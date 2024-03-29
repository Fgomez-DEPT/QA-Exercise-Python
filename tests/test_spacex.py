from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home import Home
import requests
import time


def get_rockets_data():
    """Function to fetch rockets data from SpaceX API."""
    response = requests.get('https://api.spacexdata.com/v3/rockets')
    response.raise_for_status()
    return response.json()


def search_rockets(home: Home, search_text):
    """Function to search for rockets using Selenium."""
    search_box = home.search_box()
    search_box.clear()
    search_box.send_keys(search_text)


def check_favorite_tab(driver):
    """Function to check the favorite tab using Selenium."""
    driver.find_element(By.XPATH, '//a[contains(text(), "Favorites")]').click()
    assert driver.find_element(By.XPATH, '//div[contains(text(), "CRS-13")]'), "CRS-13 is not in the Favorites tab"


def test_spacex():
    # Initialize webdriver and open browser
    driver = webdriver.Chrome()
    home = Home(driver)
    home.load_page()

    # Load rockets data
    rockets_data = get_rockets_data()
    assert len(rockets_data) == 4, "The number of rockets is not equal to 4"

    for rocket in rockets_data:
        assert rocket['first_flight'] > "2005", f"The first flight of {rocket['name']} is not later than 2005"

    # Search for rockets
    search_rockets(home, 'crs')
    assert driver.find_element(By.XPATH, '//div[contains(text(), "3")]'), "The number of pages is not equal to 3"

    # Mark a rocket as favorite
    driver.find_element(By.XPATH, '//div[contains(text(), "CRS-13")]').click()
    driver.find_element(By.XPATH, '//div[contains(text(), "Favorites")]').click()

    # Check that the rocket is marked as favorite
    check_favorite_tab(driver)

    # Refresh browser and check again for step 5.
    driver.refresh()
    time.sleep(5)
    check_favorite_tab(driver)

    # Close browser
    driver.quit()
