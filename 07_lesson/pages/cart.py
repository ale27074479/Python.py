from selenium.webdriver.common.by import By

class Cart:
    def __init__(self, browser):
        self.browser = browser
        self.checkout_button = (By.ID, "checkout")

    def checkout(self):
        self.browser.find_element(*self.checkout_button).click()
