import selenium, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.command import Command


#Your Amazon Credentials File
from credentials import *



#Define URL and Web Driver
driver = webdriver.Firefox()
driver.implicitly_wait(0)
url = "https://sellercentral.amazon.com/inventory/ref=id_invmgr_dnav_xx_?tbla_myitable=sort:%7B%22sortOrder%22%3A%22DESCENDING%22%2C%22sortedColumnId%22%3A%22date%22%7D;search:;pagination:1;"
driver.get(url)

#Login
username = driver.find_element_by_name("email")
username.send_keys(amazon_email)
time.sleep(5)

password = driver.find_element_by_name("password")
password.send_keys(amazon_password)
time.sleep(5)
password.send_keys(Keys.RETURN)


## USER FUNCTIONS FOR PRICE CHANGES

#Price Match Inventory (new)
def match_prices(inventory_item):
    #price_match = driver.find_elements_by_link_text("Match price")
    #print(len(price_match))
    for link in inventory_item:
        try:
            link.click()
            time.sleep(2)
        except:
            print("exception")
            pass


def beat_price(price):
    price = float(price)
    new_price = round(price - 0.02, 2)
    return str(new_price)


def lower_price(inventory_item):

    current_price = inventory_item.get_attribute('value')
    print(current_price)
    #price_war(inventory_item)
    new_price = beat_price(current_price)
    inventory_item.clear()
    inventory_item.send_keys(new_price)
    time.sleep(1)


def save_changes():
    try:
        save_all = driver.find_element_by_link_text("Save all")
        save_all.click()
    except:
        save_all = driver.find_element_by_xpath("//a[@id='a-autoid-2-announce-floating']")
        save_all.click()
    finally:
        pass

## MAIN FUNCTION TO RUN PRICE WAR

def price_war():

    #Select Only Active Inventory
    time.sleep(2)
    radio = driver.find_element_by_xpath("//div[@data-filter-id='Open']")
    radio.click()
    time.sleep(3)

    items = driver.find_elements_by_xpath("//tr[@class='mt-row']")
    len(items)

    index = -1
    for row in items:
        index +=1
        better_price = row.find_elements_by_link_text("Match price")

        if len(better_price) >= 1:
            #Match price
            print("Matching price")
            match_prices(better_price)

            #Select Inventory Item
            inventory_item = row.find_elements_by_xpath("//input[@maxlength='23']")[index]
            lower_price(inventory_item)

        else:
            pass

    #Save Changes
    save_changes()
    time.sleep(5)

    #Close Driver
    driver.close()

if __name__=="__main__":
    price_war()
