

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Your Amazon Credentials File
from credentials import *

url = "https://sellercentral.amazon.com/inventory/ref=id_invmgr_dnav_xx_?tbla_myitable=sort:%7B%22sortOrder%22%3A%22DESCENDING%22%2C%22sortedColumnId%22%3A%22date%22%7D;search:;pagination:1;"

driver = webdriver.Firefox()
driver.get(url)

#assert "NatureServe" in driver.title
#SciName = driver.find_element_by_name('searchSciOrCommonName')

username = driver.find_element_by_name("email")
username.send_keys(amazon_email)

password = driver.find_element_by_name("password")
password.send_keys(amazon_password)

password.send_keys(Keys.RETURN)
