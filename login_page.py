from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='username']").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']").click()
    