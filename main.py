from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import config

user = config.user
pswd = config.pswd
url = config.url
domain = config.domain

options = webdriver.FirefoxOptions()

options.add_argument("-headless")
driver = webdriver.Firefox(options=options)

driver.get(url)

time.sleep(1)

btn = driver.find_element(By.ID, "logout")

btn.click()

time.sleep(1)

username = driver.find_element(By.ID, "username")

wait = WebDriverWait(driver, timeout=20)
wait.until(lambda d : username.is_displayed())
username.clear()
username.send_keys(user)
password = driver.find_element(By.ID, "password")

password.clear()
password.send_keys(pswd)

time.sleep(1)

driver.find_element(By.CSS_SELECTOR, domain).click()

time.sleep(1)

login = driver.find_element(By.ID, "login")

login.click()

wait = WebDriverWait(driver, timeout=20)
wait.until(lambda d : btn.is_displayed())

driver.quit()