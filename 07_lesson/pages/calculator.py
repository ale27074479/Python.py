from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:
    def __init__(self, browser):
        self.browser = browser
        self.delay_field = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            num: (By.XPATH, f"//span[text()='{num}']") for num in '1234567890+-='
        }

    def set_delay(self, seconds):
        self.browser.find_element(*self.delay_field).clear()
        self.browser.find_element(*self.delay_field).send_keys(str(seconds))

    def click_button(self, button):
        self.browser.find_element(*self.buttons[button]).click()

    def get_result(self, timeout=45):
        wait = WebDriverWait(self.browser, timeout)
        # Улучшенная проверка результата
        wait.until_not(
            EC.text_to_be_present_in_element(self.result_field, "7+8")
        )
        return wait.until(
            lambda d: "15" in d.find_element(*self.result_field).text
        )
