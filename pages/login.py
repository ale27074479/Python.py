from selenium.webdriver.common.by import By
from pages.main import Main

class Login:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://www.saucedemo.com/"
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.browser.get(self.url)
        return self

    def auth(self, username, password):
        self.browser.find_element(*self.username_field).send_keys(username)
        self.browser.find_element(*self.password_field).send_keys(password)
        self.browser.find_element(*self.login_button).click()
        return Main(self.browser)
