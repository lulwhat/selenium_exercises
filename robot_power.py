from selenium import webdriver
import time 
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(str(y))
	box = browser.find_element_by_id("robotCheckbox")
	box.click()
	radio = browser.find_element_by_id("robotsRule")
	radio.click()
	button = browser.find_element_by_css_selector('button.btn')
	button.click()

finally:
	time.sleep(30)
	browser.quit()