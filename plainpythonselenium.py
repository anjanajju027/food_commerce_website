from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get("https://www.beelivery.com/#")
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Sign In')]"))).click()

wait.until(EC.presence_of_element_located((By.ID, "tbEmail"))).send_keys("anjanajju027@gmail.com")
driver.find_element(By.ID, "tbPassword").send_keys("Govindha10@")
driver.find_element(By.ID, "imagebuttonPopupLogin").click()

wait.until(EC.presence_of_element_located((By.ID, "postcode"))).send_keys("SW1A 1AA")
driver.find_element(By.ID, "shopType-0").click()
driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()

search_box = wait.until(EC.presence_of_element_located((By.ID, "mobileSearch")))
search_box.clear()
search_box.send_keys("Cake")
search_box.send_keys(Keys.ENTER)

add_button = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//h3[contains(text(),'Gourmet Gold')]/ancestor::div[contains(@class,'product')]//button[contains(text(),'Add')]"
)))
add_button.click()

plus_button = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//h3[contains(text(),'Gourmet Gold')]/ancestor::div[contains(@class,'product')]//button[contains(@aria-label,'Increase')]"
)))
plus_button.click()
plus_button.click()

side_panel_item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".side-panel .cart-item-name")))
assert "Gourmet Gold" in side_panel_item.text, "Item not added to side panel"

driver.find_element(By.CSS_SELECTOR, ".expandDeliveryTimes").click()
wait.until(EC.element_to_be_clickable((By.ID, "delivery-day-selector"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(),'Sunday')]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'09:50')]"))).click()

driver.find_element(By.ID, "confirm-delivery-window").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='checkoutSpinner']"))).click()

wait.until(EC.url_contains("checkout"))
assert "checkout" in driver.current_url.lower(), "Did not navigate to checkout page"
print("Test Passed: Item added and checkout page reached.")
driver.quit()