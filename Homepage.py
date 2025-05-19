from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_postcode_and_order(self, postcode):
        self.wait.until(EC.presence_of_element_located((By.ID, "postcode"))).send_keys(postcode)
        self.driver.find_element(By.ID, "shopType-0").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
