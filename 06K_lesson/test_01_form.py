import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    # Инициализация браузера
    driver = webdriver.Chrome()
    yield driver
    # Закрытие браузера после теста
    driver.quit()


def test_form_submission(browser):
    # 1. Открываем страницу
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    browser.get(url)

    # 2. Заполняем форму
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
    # Zip code оставляем пустым
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

    # 3. Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # 4. Проверяем, что поле Zip code подсвечено красным
    zip_code = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#zip-code'))
    )
    assert "alert-danger" in zip_code.get_attribute("class")

    # 5. Проверяем, что остальные поля подсвечены зеленым
    fields_to_check = [
        'first-name', 'last-name', 'address', 'e-mail',
        'phone', 'city', 'country', 'job-position', 'company'
    ]

    for field in fields_to_check:
        element = browser.find_element(By.CSS_SELECTOR, f'#{field}')
        assert "alert-success" in element.get_attribute("class")
