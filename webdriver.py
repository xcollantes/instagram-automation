from secure_selenium.secure_selenium import SecureSelenium


driver = SecureSelenium(webdriver_path="./secure_selenium/chromedriver", headless=False)

driver.get("https://google.com")
driver.save_screenshot()
