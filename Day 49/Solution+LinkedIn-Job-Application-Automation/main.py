from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Environment variables or placeholders for sensitive data
ACCOUNT_EMAIL = os.getenv("LINKEDIN_EMAIL", "namithasrinivasa@gmail.com")  # Replace with your email
ACCOUNT_PASSWORD = os.getenv("LINKEDIN_PASSWORD", "future@44")    # Replace with your password
PHONE = os.getenv("PHONE_NUMBER", "8147178773")                       # Replace with your phone number

# Configure WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keep the browser open after script execution
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# LinkedIn Jobs URL
driver.get("https://www.linkedin.com/jobs")

try:
    # Wait for the Sign In button and click
    wait = WebDriverWait(driver, 10)
    sign_in_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
    sign_in_button.click()

    # Sign in with credentials
    email_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    email_field.send_keys(ACCOUNT_EMAIL)
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(ACCOUNT_PASSWORD)
    password_field.send_keys(Keys.ENTER)

    # Handle CAPTCHA manually
    input("Please solve the CAPTCHA and press Enter to continue...")

    # Wait for job listings to load
    time.sleep(5)
    all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

    for listing in all_listings:
        print("Opening job listing...")
        listing.click()
        time.sleep(2)
        try:
            # Click the Apply button if available
            apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
            apply_button.click()
            print("Clicked Apply button.")

            # Wait for phone number field, fill it if empty
            phone_field = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[id*=phoneNumber]"))
            )
            if phone_field.get_attribute("value") == "":
                phone_field.send_keys(PHONE)

            # Check and click the Submit or Continue button
            submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
            if "continue_unify" in submit_button.get_attribute("data-control-name"):
                print("Complex application detected. Skipping...")
                driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
                time.sleep(1)
                driver.find_element(
                    By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn"
                ).click()
                continue
            else:
                print("Submitting application...")
                submit_button.click()

            # Close the application confirmation modal
            time.sleep(2)
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
        except NoSuchElementException:
            print("No Apply button found, skipping...")
            continue

except TimeoutException as e:
    print(f"Error: {e}. A required element did not load in time.")

finally:
    print("Closing the browser...")
    time.sleep(5)
    driver.quit()
