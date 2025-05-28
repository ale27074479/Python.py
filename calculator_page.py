from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")
        self.equal_btn = (By.CSS_SELECTOR, ".btn-outline-success")

    def set_delay(self, seconds):
        """Устанавливает задержку вычислений"""
        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(str(seconds))
        # Проверяем что значение установилось
        assert delay.get_attribute("value") == str(seconds), "Задержка не установилась"

    def click_button(self, button_text):
        """Нажимает кнопку с указанным текстом"""
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        ).click()

    def get_result(self, timeout=60):
        """Ожидает и возвращает результат вычислений"""
        # Ждем пока в поле результата появится не пустое значение
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*self.result_field).text.strip() not in ['', '7+8']
        )
        return self.driver.find_element(*self.result_field).text    
    