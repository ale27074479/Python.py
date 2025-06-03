import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
def test_store_checkout(driver):
    """Тест процесса оформления заказа"""
    # 1. Авторизация
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # 2. Добавление товаров
    wait = WebDriverWait(driver, 10)
    
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    
    for item in items_to_add:
        item_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']")
            )
        )
        item_element.find_element(By.XPATH, ".//button").click()
    
    # 3. Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # 4. Оформление заказа
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    
    # 5. Проверка итоговой суммы
    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    assert total == "Total: $58.29"
