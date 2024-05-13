from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
chrome_options = ChromeOptions()
# Remove headless option to see the browser actions
# chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = ChromeService(ChromeDriverManager().install())

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    driver.get("http://127.0.0.1:8000/")
    print("Opened the website")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
    login_link = driver.find_element(By.LINK_TEXT, "Login")
    login_link.click()
    print("Clicked login link")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    print("Found username and password fields")

    # Enter the credentials
    username.send_keys("alese")
    password.send_keys("Warf4242")
    print("Entered username and password")

    # Wait until the submit button is present and click it using multiple strategies
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "submit")))
        submit_button = driver.find_element(By.NAME, "submit")
        print("Submit button found by NAME")
    except:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='submit']")))
            submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            print("Submit button found by CSS_SELECTOR")
        except:
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
                submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
                print("Submit button found by XPATH")
            except:
                print("Submit button not found!")
                exit()

    submit_button.click()
    print("Clicked submit button")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
    logout_link = driver.find_element(By.LINK_TEXT, "Logout")
    assert logout_link.is_displayed()
    print("Login successful, found logout link")

except Exception as e:
    print(f"An error occurred: {e}")
