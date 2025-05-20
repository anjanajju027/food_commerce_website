from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_beelivery_order_process():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://www.beelivery.com/#")
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("Alert handled.")
        except Exception:
            print("No alert found.")

        sign_in_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Sign In')]")))
        sign_in_link.click()
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tbEmail")))
        email_input.send_keys("anjanajju027@gmail.com")
        driver.find_element(By.CSS_SELECTOR, "#tbPassword").send_keys("Govindha10@")
        driver.find_element(By.CSS_SELECTOR, "#imagebuttonPopupLogin").click()
        postcode_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".postcode-search-container")))
        postcode_input.send_keys("SW1A 1AA")
        driver.find_element(By.CSS_SELECTOR, "#shopType-0").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Place Order')]").click()
        search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mobileSearch")))
        search_box.clear()
        search_box.send_keys("Cake")
        search_box.send_keys(Keys.ENTER)
        add_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[contains(text(),'Gourmet Gold')]/ancestor::div[@class='product-card']//button[contains(text(),'Add')]"
        )))
        add_button.click()
        time.sleep(1)
        plus_button = wait.until(EC.element_to_be_clickable((
             By.XPATH, "//div[contains(text(),'Gourmet Gold')]/ancestor::div[@class='product-card']//button[contains(text(),'+')]"
        )))
        plus_button.click()
        plus_button.click()
        side_panel_item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "//div[@class='currentWindow']")))
        assert "Gourmet Gold" in side_panel_item.text, "Item not added to side panel"
        print("Item verified in side panel.")
        driver.find_element(By.CSS_SELECTOR, ".expandDeliveryTimes").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delivery-day-selector"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(),'Sunday')]"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "delivery-time-start"))).click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#confirm-delivery-window").click()
        checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='checkoutSpinner']")))
        checkout_button.click()
        wait.until(EC.url_contains("checkout"))
        assert "checkout" in driver.current_url.lower(), "Did not navigate to checkout page"
        print("Navigated to checkout page.")
        print("Test Passed: Order process successful.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
if __name__ == "__main__":
    test_beelivery_order_process()
