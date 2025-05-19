from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def search_product(self, product):
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "mobileSearch")))
        search_box.clear()
        search_box.send_keys(product)
        search_box.send_keys(Keys.ENTER)

    def add_gourmet_gold(self):
        add_button = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//h3[contains(text(),'Gourmet Gold')]/ancestor::div[contains(@class,'product')]//button[contains(text(),'Add')]"
        )))
        add_button.click()

    def increase_quantity(self, count):
        plus_button = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//h3[contains(text(),'Gourmet Gold')]/ancestor::div[contains(@class,'product')]//button[contains(@aria-label,'Increase')]"
        )))
        for _ in range(count):
            plus_button.click()

    def verify_item_in_cart(self):
        side_item = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".side-panel .cart-item-name")))
        return "Gourmet Gold" in side_item.text
