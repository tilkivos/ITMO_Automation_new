from selenium import webdriver
from selenium.webdriver.common.by import By
def test_search():
    driver = webdriver.Chrome()
    driver.get('https://saucedemo.com/')

    name_field = driver.find_element(By.CSS_SELECTOR, '#user-name')
    password_field = driver.find_element(By.CSS_SELECTOR, '#password')
    submit_button = driver.find_element(By.CSS_SELECTOR, '#login-button')

    if name_field and password_field and submit_button is not None:
        print('Элементы найдены')
    else:
        print('')

test_search()