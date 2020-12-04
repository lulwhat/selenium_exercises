import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
	print("\nstart browser for test..")
	browser = webdriver.Chrome()
	yield browser
	print("\nquit browser..")
	browser.quit()

@pytest.mark.parametrize('lesson', \
 ["236895", "236896", "236897", "236898", \
 "236899", "236903", "236904", "236905"])
def test_message(browser, lesson):
	link = f"https://stepik.org/lesson/{lesson}/step/1"
	browser.get(link)
	browser.implicitly_wait(6)
	input1=browser.find_element_by_css_selector(".string-quiz__textarea")
	answer = math.log(int(time.time()))
	input1.send_keys(str(answer))
	button=browser.find_element_by_css_selector(".submit-submission")
	button.click()
	result=browser.find_element_by_css_selector(".smart-hints__feedback").text
	assert result == "Correct!", "should be correct answer"