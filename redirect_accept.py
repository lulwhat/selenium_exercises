from selenium import webdriver
import time 
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	button = browser.find_element_by_css_selector('button.btn')
	button.click()
	browser.switch_to.window(browser.window_handles[1])
	xx = browser.find_element_by_id('input_value').text
	y=calc(xx)
	input1 = browser.find_element_by_id('answer')
	input1.send_keys(str(y))
	button = browser.find_element_by_css_selector('button.btn')
	button.click()

finally:
	time.sleep(15)
	browser.quit()

