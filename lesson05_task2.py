from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def click_dynamic_button():
    """Click button with dynamic ID."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("http://uitestingplayground.com/dynamicid")

        button = driver.find_element(
            By.XPATH,
            "//button[starts-with(@id, 'button-')]"
        )
        button.click()

    finally:
        driver.quit()


if __name__ == "__main__":
    click_dynamic_button()
