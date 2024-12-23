from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


options = Options()
service = Service("C:/Users/vs292/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://127.0.0.1:5500/us/index.html")


first_name_input = driver.find_element(By.XPATH, '//*[@id="fname"]')
first_name_input.send_keys("Vivek")


last_name_input = driver.find_element(By.XPATH, '//*[@id="lname"]')
last_name_input.send_keys("Singh")


email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_input.send_keys("vs292713@gmail.com")


message_input = driver.find_element(By.XPATH, '//*[@id="message"]')
message_input.send_keys("Hello! Greetings of the day. My name is Vivek Singh.")

time.sleep(100)
driver.quit()
