from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def rename_button():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("http://uitestingplayground.com/textinput")

        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "newButtonName"))
        )
        input_field.clear()
        input_field.send_keys("SkyPro")

        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "updatingButton"))
        )
        button.click()

        updated_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "updatingButton"))
        )
        print(updated_button.text)

    finally:
        driver.quit()


if __name__ == "__main__":
    rename_button()
