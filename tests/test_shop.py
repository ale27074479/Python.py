import pytest
from pages.login import Login

def test_shop(firefox_browser):
    # 1. Авторизация
    login_page = Login(firefox_browser).open()
    main_page = login_page.auth("standard_user", "secret_sauce")
    
    # 2. Добавление товаров
    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items:
        main_page.add_to_cart(item)
    
    # 3. Переход в корзину и оформление
    cart_page = main_page.go_to_cart()
    cart_page.checkout()
    
    # Проверка URL
    assert "checkout" in firefox_browser.current_url.lower()
