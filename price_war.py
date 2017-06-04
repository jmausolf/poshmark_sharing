

import selenium, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Your Amazon Credentials File
from credentials import *

#Define URL and Web Driver
url = "https://sellercentral.amazon.com/inventory/ref=id_invmgr_dnav_xx_?tbla_myitable=sort:%7B%22sortOrder%22%3A%22DESCENDING%22%2C%22sortedColumnId%22%3A%22date%22%7D;search:;pagination:1;"
driver = webdriver.Firefox()
driver.get(url)

#Login
username = driver.find_element_by_name("email")
username.send_keys(amazon_email)
time.sleep(5)

password = driver.find_element_by_name("password")
password.send_keys(amazon_password)
time.sleep(5)

password.send_keys(Keys.RETURN)
driver.implicitly_wait(10)

#Price Match Inventory
def match_prices():

    price_match = driver.find_elements_by_link_text("Match price")
    print(len(price_match))

    for link in price_match:
        try:
            link.click()
            time.sleep(2)
        except:
            pass



def price_war(price):
    new_price = round(price - 0.01, 2)
    return new_price


item_price = driver.find_element_by_name("price")
item_price.send_keys(109.75)

print(len(driver.find_elements_by_xpath('//a')))

#match_prices(5)

item_price = driver.find_element_by_class_name("a-input-text main-entry mt-icon-input mt-input-text")
item_price.send_keys(109.75)

a-input-text main-entry mt-icon-input mt-input-text
a-input-text main-entry mt-input-text
