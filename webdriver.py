"""Run script."""

import time
import logging
from secure_selenium.secure_selenium import SecureSelenium

logging.basicConfig(level=logging.INFO)


def main():
    driver = SecureSelenium(
        webdriver_path="/home/xavier/Documents/instagram_automation/chromedriver-linux64/chromedriver",
        headless=False,
    )

    driver.initial_cookies()

    try:
        driver.get("https://www.instagram.com/")

        logging.info("Sleeping... zzz")
        time.sleep(5)
    except KeyboardInterrupt as ki:
        logging.warning("Stopped by keyboard: %s", ki)
    finally:
        driver.close()


if __name__ == "__main__":
    main()
