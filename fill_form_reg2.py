from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('.first_block .first')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('.first_block .second')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('.first_block .third')
    input3.send_keys("iv_petr@mail.ru")
    input4 = browser.find_element_by_css_selector('.second_block .first')
    input4.send_keys("911")
    input5 = browser.find_element_by_css_selector('.second_block .second')
    input5.send_keys("Las Vegas")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()