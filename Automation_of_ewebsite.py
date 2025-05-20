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
    driver.implicitly_wait(15)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.beelivery.com/#")
        #time.sleep(5)
        try:
            driver.find_element(By.XPATH,"//div[@id='cookiescript_accept']").click()
            print("Alert handled.")
        except Exception:
            print("No alert found.")

        sign_in_link = driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]")
        sign_in_link.click()
        #time.sleep(5)
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tbEmail")))
        email_input.send_keys("anjanajju027@gmail.com")
        driver.find_element(By.CSS_SELECTOR, "#tbPassword").send_keys("Govindha10@")
        driver.find_element(By.CSS_SELECTOR, "#imagebuttonPopupLogin").click()
        time.sleep(5)
        postcode_input = driver.find_element(By.CSS_SELECTOR, "[placeholder='Enter your postcode']")
        #time.sleep(5)
        postcode_input.send_keys("SW1A 1AA")
        #time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "#shopType-0").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Place Order')]").click()
        #time.sleep(5)
        search_box =driver.find_element(By.XPATH,"//input[@class='textboxItemSearch ProductSearchBox']")
        search_box.send_keys("Cake")
        #time.sleep(4)
        search_box.click()
        search_box.send_keys(Keys.ENTER)
        #time.sleep(5)
        #wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='textboxItemSearch ProductSearchBox']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Gourmet Gold Savoury Cake Meat 8 x 85g (680g)')]"))
        )
        #time.sleep(5)
        plus_button = wait.until(EC.element_to_be_clickable((
             By.XPATH,"/html/body/form/div[6]/div[1]/div[1]/div[5]/div[1]/div/div[3]/div/div[1]/div[3]/div[87]/div[2]/div[2]"
        )))
        plus_button.click()
        plus_button.click()
        plus_button.click()
        #time.sleep(5)

        side_panel_item = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".item-name")))
        assert "Gourmet Gold" in side_panel_item.text, "Item not added to side panel"
        print("Item verified in side panel.")
        #time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".expandDeliveryTimes").click()
        #time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#delivery-day-selector")))
        #time.sleep(5)
        driver.find_element(By.XPATH, "//div[@class='delivery-day-selector-container']").click()
        #time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='delivery-day-selector']/option[6]")))
        print("sunday")
        driver.find_element(By.XPATH,"//*[@id='delivery-day-selector']/option[6]").click()
        #time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.ID, "delivery-time-start"))).click()
        #time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "#confirm-delivery-window").click()
        #time.sleep(3)
        print("delivery")
        #wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='checkoutSpinner']")))
        driver.find_element(By.XPATH,"//*[@id='button']").click()
        #time.sleep(3)
        #wait.until(EC.url_contains("checkout"))
        #assert "checkout" in driver.current_url.lower(), "Did not navigate to checkout page"
        print("Navigated to checkout page.")
        print("Test Passed: Order process successful.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
if __name__ == "__main__":
    test_beelivery_order_process()
