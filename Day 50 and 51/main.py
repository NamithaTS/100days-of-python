from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Constants
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"

  # Update with the correct path to your chromedriver.exe

# Store sensitive data as environment variables for security
TWITTER_EMAIL = os.getenv("namithasrinivasa@gmail.com")  # Replace with your email if not using env vars
TWITTER_PASSWORD = os.getenv("Nami@2004")  # Replace with your password if not using env vars


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        # Open Speedtest.net
        self.driver.get("https://www.speedtest.net/")

        # Wait for the "Go" button to be clickable and click it
        try:
            go_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a"))
            )
            go_button.click()
        except Exception as e:
            print("Error interacting with the Go button:", e)
            self.driver.quit()
            return

        # Wait for the speed test to complete
        time.sleep(60)  # Static wait for simplicity; adjust if necessary

        # Extract download and upload speeds
        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text

    def tweet_at_provider(self):
        # Open Twitter login page
        self.driver.get("https://twitter.com/login")

        # Log in to Twitter
        try:
            email_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            email_input.send_keys(TWITTER_EMAIL)
            email_input.send_keys(Keys.ENTER)

            time.sleep(2)  # Wait for redirection to password field
            password_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)
        except Exception as e:
            print("Error during Twitter login:", e)
            self.driver.quit()
            return

        # Compose the tweet
        try:
            tweet_compose = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div[aria-label='Tweet text']")
                )
            )
            tweet = (
                f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up "
                f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            )
            tweet_compose.send_keys(tweet)

            # Click the Tweet button
            tweet_button = self.driver.find_element(
                By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']"
            )
            tweet_button.click()
        except Exception as e:
            print("Error during tweet composition or sending:", e)
        finally:
            time.sleep(2)
            self.driver.quit()


# Main Script
if __name__ == "__main__":
    bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
    bot.get_internet_speed()
    bot.tweet_at_provider()
