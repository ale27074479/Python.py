from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def login_and_get_message():
    """Perform login and get message."""
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        driver.get("http://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username")\
            .send_keys("tomsmith")
        driver.find_element(By.ID, "password")\
            .send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button.radius")\
            .click()

        message = driver.find_element(By.ID, "flash").text
        print(message.strip())

    finally:
        driver.quit()


if __name__ == "__main__":
    login_and_get_message()
