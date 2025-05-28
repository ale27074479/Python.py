from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_info(self, first_name, last_name, postal_code):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='firstName']"))).send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='postalCode']").send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
        wait.until(EC.url_contains("checkout-step-two"))

    def get_total(self):
        wait = WebDriverWait(self.driver, 20)
        total_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Total:')]"))
        )
        return total_element.text
