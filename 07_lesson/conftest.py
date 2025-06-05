import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Перенесите объявление опции на уровень модуля
browser_option = None

def pytest_addoption(parser):
    """Добавляет опцию командной строки для выбора браузера."""
    global browser_option
    if not hasattr(pytest, 'browser_option_added'):  # Проверяем, была ли уже добавлена опция
        browser_option = parser.addoption(
            "--browser",
            action="store",
            default="chrome",
            help="Браузер для тестов: chrome или firefox"
        )
        pytest.browser_option_added = True  # Помечаем, что опция добавлена

@pytest.fixture
def driver(request):
    """Фикстура для инициализации и закрытия драйвера."""
    browser_name = request.config.getoption("--browser").lower()
    
    if browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=options
        )
    
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
