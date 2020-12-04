from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	button1=browser.find_element_by_id("book")
	WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
	button1.click()

	xx = browser.find_element_by_id('input_value').text
	y=calc(xx)
	input1 = browser.find_element_by_id('answer')
	input1.send_keys(str(y))
	button2 = browser.find_element_by_id('solve')
	button2.click()

finally:
	time.sleep(60)
	browser.quit()
