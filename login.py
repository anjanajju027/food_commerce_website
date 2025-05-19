from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_sign_in_link(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Sign In')]"))).click()

    def login(self, email, password):
        self.wait.until(EC.presence_of_element_located((By.ID, "tbEmail"))).send_keys(email)
        self.driver.find_element(By.ID, "tbPassword").send_keys(password)
        self.driver.find_element(By.ID, "imagebuttonPopupLogin").click()
