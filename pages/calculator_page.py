from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, browser):
        self.browser = browser

    def calculate(self, expression):
        wait = WebDriverWait(self.browser, 10)
        input_field = wait.until(
            EC.presence_of_element_located((By.ID, "calculator-input"))
        )
        input_field.send_keys(expression)
        
        result_button = self.browser.find_element(By.ID, "calculate-btn")
        result_button.click()
        
        result = wait.until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        return result.text
        
