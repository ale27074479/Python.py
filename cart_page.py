from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        wait = WebDriverWait(self.driver, 15)
        checkout_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='checkout']"))
        )
        checkout_btn.click()

    def get_cart_items(self):
        wait = WebDriverWait(self.driver, 15)
        items = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
        )
        return [item.text for item in items]
