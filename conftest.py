from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-test='username']"))).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "input[data-test='password']").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input[data-test='login-button']").click()
    