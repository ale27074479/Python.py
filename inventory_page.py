from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        wait = WebDriverWait(self.driver, 15)
        # Кнопка добавления рядом с названием товара
        add_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@class='inventory_item_name' and text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
            )
        )
        add_btn.click()

    def go_to_cart(self):
        cart_btn = self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
        cart_btn.click()
