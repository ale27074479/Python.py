import pytest
from pages.calculator import Calculator

def test_calculator(chrome_browser):
    calc = Calculator(chrome_browser)
    chrome_browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    calc.set_delay(45)
    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")
    
    assert calc.get_result(), "Калькулятор показал неверный результат"
