from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load_page(self):
        self.driver.get('https://csb-x6dpt1.netlify.app/')

    def search_box(self):
        return self.driver.find_element(By.XPATH, '//input[1]')
    
