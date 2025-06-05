from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://shop.example.com/login")
        return self

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        
        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = self.driver.find_element(By.ID, "password")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        
        login_button = self.driver.find_element(By.ID, "login-btn")
        login_button.click()
