from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Page Object для страницы товаров."""

    def __init__(self, driver):
        """Инициализация страницы товаров."""
        self.driver = driver
        self.item_locator = (
            "//div[@class='inventory_item_name' and text()='{}']"
            "/ancestor::div[@class='inventory_item']"
        )

    def add_item_to_cart(self, item_name):
        """Добавляет указанный товар в корзину.
        
        Args:
            item_name (str): Название товара для добавления
        """
        item = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, self.item_locator.format(item_name))
            )
        )
        item.find_element(By.XPATH, ".//button").click()

    def go_to_cart(self):
        """Переходит на страницу корзины."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    