import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    """Инициализация и закрытие браузера."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_shopping_flow(browser):
    """Тест процесса покупки с проверкой итоговой суммы."""
    # 1. Открываем сайт магазина
    browser.get("https://www.saucedemo.com/")

    # 2. Авторизация
    browser.find_element(By.ID, "user-name").send_keys("problem_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # 3. Добавление товаров в корзину
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item in items_to_add:
        xpath = ("//div[text()='{item}']"
                 "/ancestor::div[@class='inventory_item']//button")
        browser.find_element(By.XPATH, xpath.format(item=item)).click()

    # 4. Переход в корзину
    cart_locator = (By.CLASS_NAME, "shopping_cart_link")
    cart_icon = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(cart_locator)
    )
    cart_icon.click()

    # 5. Проверка количества товаров в корзине
    badge_locator = (By.CLASS_NAME, "shopping_cart_badge")
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element(badge_locator, "3")
    )

    # 6. Начало оформления заказа
    checkout_locator = (By.ID, "checkout")
    checkout_btn = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(checkout_locator)
    )
    checkout_btn.click()

    # 7. Заполнение формы
    first_name_locator = (By.ID, "first-name")
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(first_name_locator)
    ).send_keys("Александра")
    browser.find_element(By.ID, "last-name").send_keys("Чернышова")
    browser.find_element(By.ID, "postal-code").send_keys("123456")

    # 8. Продолжение оформления
    browser.find_element(By.ID, "continue").click()

    # 9. Проверка итоговой суммы
    total_locator = (By.CLASS_NAME, "summary_total_label")
    total_element = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located(total_locator)
    )
    total_text = total_element.text
    expected = "58.29"
    assert expected in total_text, f"Ожидалось {expected}, получено {total_text}"
