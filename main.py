from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import config

user = config.user
pswd = config.pswd
url = config.url
domain_name = config.domain_name

options = webdriver.FirefoxOptions()

options.add_argument("-headless")
driver = webdriver.Firefox(options=options)


driver.get(url)

time.sleep(1)
try:
    driver.find_element(By.XPATH,"//span[text()=' 注销 ']").click()
    time.sleep(1)
except NoSuchElementException: 
    pass

username = driver.find_element(By.XPATH, "//input[@placeholder='请输入用户名']")
wait = WebDriverWait(driver, timeout=20)
wait.until(lambda d : username.is_displayed())
username.clear()
username.send_keys(user)

password = driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']")
password.clear()
password.send_keys(pswd)

driver.find_element(By.XPATH, "//span[@class='el-checkbox__inner']").click()
driver.find_element(By.XPATH, "//span[text()=' 登录 ']").click()
time.sleep(1)

driver.find_element(By.XPATH, f"//span[text()=' {domain_name} ']").click()
time.sleep(1)

wait = WebDriverWait(driver, timeout=20)
driver.quit()
