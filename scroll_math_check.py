from selenium import webdriver
import time 
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	xx = browser.find_element_by_id('input_value').text
	y=calc(xx)
	browser.execute_script("window.scrollBy(0, 100);")
	input1 = browser.find_element_by_id('answer')
	input1.send_keys(str(y))
	box = browser.find_element_by_id("robotCheckbox")
	box.click()
	radio = browser.find_element_by_id("robotsRule")
	radio.click()
	button = browser.find_element_by_css_selector('button.btn')
	button.click()

finally:
	time.sleep(15)
	browser.quit()

