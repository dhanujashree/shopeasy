import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,800")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

try:
    file_path = os.path.abspath("index.html")
    driver.get("file:///" + file_path.replace("\\", "/"))

    wait.until(
        EC.element_to_be_clickable((By.ID, "loginNav"))
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "email"))
    ).send_keys("test@example.com")

    driver.find_element(By.ID, "password").send_keys("password123")

    driver.find_element(
        By.XPATH,
        "//section[@id='login']//button[contains(text(),'Login')]"
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "products"))
    )

    products = driver.find_elements(
        By.CSS_SELECTOR,
        "#productList .product"
    )

    assert len(products) == 3

    add_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#productList .product:first-child button")
        )
    )

    add_button.click()

    alert = wait.until(EC.alert_is_present())

    assert alert.text == "Wireless Mouse added to cart."

    alert.accept()

    wait.until(
        lambda d: d.find_element(By.ID, "cartCount").text == "1"
    )

    assert driver.find_element(By.ID, "cartCount").text == "1"

    driver.find_element(
        By.XPATH,
        "//nav//button[contains(text(),'Cart')]"
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "cart"))
    )

    assert "Wireless Mouse" in driver.find_element(
        By.ID,
        "cartItems"
    ).text

    remove_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#cartItems .cart-item button")
        )
    )

    remove_button.click()

    wait.until(
        lambda d: d.find_element(By.ID, "cartCount").text == "0"
    )

    assert driver.find_element(By.ID, "cartCount").text == "0"

    print("All ShopEase automated tests passed")

finally:
    driver.quit()