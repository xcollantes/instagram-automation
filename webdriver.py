"""Run script."""

import os
import random
import time
from absl import app
from absl import logging
from absl import flags
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from secure_selenium.secure_selenium import SecureSelenium

logging.set_verbosity(logging.INFO)

FLAGS = flags.FLAGS
flags.DEFINE_string("chromedriver", "", "Path of Chromedriver.")
flags.DEFINE_string("chrome_version", "", "Version of Chrome browser.")
flags.DEFINE_integer("login_time", 30, "Seconds to wait for manual login.")


def main(_):
    driver = SecureSelenium(
        webdriver_path=os.path.abspath(FLAGS.chromedriver),
        headless=False,
        chrome_version=FLAGS.chrome_version,
    )

    driver.initial_cookies()

    # Login manually
    driver.get("https://www.instagram.com")
    logging.info("You have %s seconds to login.", FLAGS.login_time)
    for s in range(FLAGS.login_time, 0, -1):
        logging.info(s)
        time.sleep(1)

    mouse = ActionBuilder(driver.webdriver)

    try:
        while True:
            # Double-click on post
            logging.info("Clicking...")
            mouse.pointer_action.move_to_location(650, 400)
            mouse.pointer_action.double_click()
            mouse.perform()

            driver.scroll_by(200)

            # Instagram caps actions
            time.sleep(random.randint(1, 10))

    except KeyboardInterrupt as ki:
        logging.warning("Stopped by keyboard: %s", ki)
    finally:
        driver.close()


if __name__ == "__main__":
    app.run(main)
