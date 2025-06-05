from selenium.webdriver.common.by import By
from pages.cart import Cart

class Main:
    def __init__(self, browser):
        self.browser = browser
        self.item_add_buttons = {
            "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, item_name):
        self.browser.find_element(*self.item_add_buttons[item_name]).click()

    def go_to_cart(self):
        self.browser.find_element(*self.cart_button).click()
        return Cart(self.browser)
