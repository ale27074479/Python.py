import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    """Фикстура для инициализации и закрытия браузера."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(browser):
    """Тест медленного калькулятора с задержкой 45 секунд."""
    # 1. Открываем страницу калькулятора
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    browser.get(url)

    # 2. Устанавливаем задержку 45 секунд
    delay_field = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_field.clear()
    delay_field.send_keys("45")

    # 3. Нажимаем кнопки: 7 + 8 =
    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()

    # 4. Ожидаем результат и проверяем его
    result_locator = (By.CSS_SELECTOR, ".screen")
    result = WebDriverWait(browser, 46).until(
        EC.text_to_be_present_in_element(result_locator, "15")
    )
    assert result, "Результат 15 не появился после ожидания"
