import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage

@pytest.fixture
def browser():
    # Настраиваем Chrome для надежности
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # Неявное ожидание
    yield driver
    driver.quit()

def test_calculator_with_delay(browser):
    # 1. Открываем страницу калькулятора
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # 2. Инициализируем Page Object
    calculator = CalculatorPage(browser)
    
    # 3. Устанавливаем задержку 55 секунд
    calculator.set_delay(55)
    
    # 4. Вводим выражение 7 + 8
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    
    # 5. Нажимаем равно
    calculator.click_button("=")
    
    # 6. Получаем и проверяем результат
    result = calculator.get_result(timeout=55)
    assert result == "15", f"Ожидался результат 15, получено {result}"
