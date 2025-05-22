from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_images():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "loading-images.html"
        )

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "image-container"))
        )

        WebDriverWait(driver, 30).until(
            lambda d: len(d.find_elements(
                By.CSS_SELECTOR, "#image-container img")) >= 4
        )

        images = driver.find_elements(
            By.CSS_SELECTOR, "#image-container img")
        print(f"Найдено изображений: {len(images)}")

        third_image_src = images[2].get_attribute("src")
        print(f"SRC третьей картинки: {third_image_src}")

        driver.save_screenshot('result.png')
        print("Скриншот сохранен как result.png")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        driver.save_screenshot('error.png')
        print("Скриншот ошибки сохранен как error.png")
    finally:
        driver.quit()


if __name__ == "__main__":
    wait_for_images()
