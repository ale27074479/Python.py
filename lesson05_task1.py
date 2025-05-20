from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


def click_blue_button():
    """Click the blue button on classattr page."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("http://uitestingplayground.com/classattr")

        blue_button = driver.find_element(
            By.CSS_SELECTOR,
            "button.btn-primary"
        )
        blue_button.click()

        alert = driver.switch_to.alert
        alert.accept()

    except NoSuchElementException:
        print("Error: Blue button not found")
    finally:
        driver.quit()


if __name__ == "__main__":
    click_blue_button()
