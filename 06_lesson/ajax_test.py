from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("http://uitestingplayground.com/ajax")

        ajax_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
        ajax_button.click()

        wait = WebDriverWait(driver, 20)
        green_banner = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
        )
        print(green_banner.text)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
