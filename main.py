from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

# init chrome driver
options = ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

# set timeout
driver.implicitly_wait(10)

driver.get('https://www.saucedemo.com')

# fill username 
username = driver.find_element(by=By.CSS_SELECTOR, value='#user-name')
username.send_keys('standard_user')
# fill password
password = driver.find_element(by=By.CSS_SELECTOR, value='#password')
password.send_keys('secret_sauce')
# click submit button
submit_button = driver.find_element(by=By.CSS_SELECTOR, value='#login-button')
submit_button.click()

assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

# add to cart
add_to_cart_button = driver.find_element(by=By.CSS_SELECTOR, value='#add-to-cart-sauce-labs-backpack')
add_to_cart_button.click()
# go to cart
go_to_cart_button = driver.find_element(by=By.CSS_SELECTOR, value='#shopping_cart_container > a')
go_to_cart_button.click()
# checkout
checkout_button = driver.find_element(by=By.CSS_SELECTOR, value='#checkout')
checkout_button.click()

# fill first name
first_name = driver.find_element(by=By.CSS_SELECTOR, value='#first-name')
first_name.send_keys('Anh')
# fill last name
last_name = driver.find_element(by=By.CSS_SELECTOR, value='#last-name')
last_name.send_keys('Nguyen')
# fill postal code
postal_code = driver.find_element(by=By.CSS_SELECTOR, value='#postal-code')
postal_code.send_keys('123456')
# click continue button
continue_button = driver.find_element(by=By.CSS_SELECTOR, value='#continue')
continue_button.click()
# click finish button
finish_button = driver.find_element(by=By.CSS_SELECTOR, value='#finish')
finish_button.click()

# click menu button
menu_button = driver.find_element(by=By.CSS_SELECTOR, value='#react-burger-menu-btn')
menu_button.click()
# click logout button
logout_button = driver.find_element(by=By.CSS_SELECTOR, value='#logout_sidebar_link')
logout_button.click()
assert driver.current_url == 'https://www.saucedemo.com/'

# end browser session
driver.quit()
