from selenium.webdriver.common.by import By


class CartPage:
    """Page Object для страницы корзины."""

    def __init__(self, driver):
        """Инициализация страницы."""
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def checkout(self):
        """Начинает процесс оформления заказа."""
        self.driver.find_element(*self.checkout_button).click()
    