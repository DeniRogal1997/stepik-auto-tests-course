from selenium import webdriver
import math
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
browser.find_element(By. CSS_SELECTOR, ".btn.btn-primary").click()

change = browser.switch_to.alert
change.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

browser.find_element(By. ID, "answer").send_keys(y)

browser.find_element(By. CSS_SELECTOR, ".btn.btn-primary").click()