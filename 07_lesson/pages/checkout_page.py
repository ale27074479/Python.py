from selenium.webdriver.common.by import By


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver):
        """Инициализация страницы."""
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_info(self, first_name, last_name, zip_code):
        """Заполняет информацию для оформления."""
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.zip_code_field).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self):
        """Возвращает итоговую сумму."""
        return self.driver.find_element(*self.total_label).text.split()[-1]
