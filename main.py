from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

# Define options for Chrome session before starting it
options = ChromeOptions()
# options.add_argument('headless')

# Initalize Chrome driver
# A new Chrome browser session is automatically started.
driver = webdriver.Chrome(options=options)

# set timeout
driver.implicitly_wait(10)

driver.get('https://testops.staging.katalon.com')

title = driver.title
assert title == 'Katalon TestOps'

print (driver.window_handles)
# fill username 
username = driver.find_element(by=By.CSS_SELECTOR, value='[name=username]')
username.send_keys('hai.nguyen+4@katalon.com')
# fill password
password = driver.find_element(by=By.CSS_SELECTOR, value='[name=password]')
password.send_keys('-9gBFiixf8H2wXg')
# click submit button
submit_button = driver.find_element(by=By.CLASS_NAME, value='signin-button')
submit_button.click()

# find logo link to homepage
logo_link = driver.find_element(by=By.CLASS_NAME, value='navbar-brand')
assert logo_link.is_displayed

driver.get('https://www.selenium.dev/documentation/')
assert "Automation" in driver.title 
print (driver.window_handles)

edit_page_link = driver.find_element(by=By.LINK_TEXT, value='Edit this page')
edit_page_link.click()

print(driver.window_handles)
main_tab = driver.current_window_handle
print ('Before switch:', main_tab)


for handle in driver.window_handles:
    if handle != main_tab:
        driver.switch_to.window(handle)
        main_tab = driver.current_window_handle
print('After switch:', main_tab)
# end browser session
driver.quit()
