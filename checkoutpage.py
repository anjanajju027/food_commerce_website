from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def select_delivery_slot(self):
        self.driver.find_element(By.CSS_SELECTOR, ".expandDeliveryTimes").click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "delivery-day-selector"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(),'Sunday')]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'09:50')]"))).click()

    def confirm_and_checkout(self):
        self.driver.find_element(By.ID, "confirm-delivery-window").click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='checkoutSpinner']"))).click()
        self.wait.until(EC.url_contains("checkout"))
        return "checkout" in self.driver.current_url.lower()
