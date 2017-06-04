import selenium, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Your Amazon Credentials File
from credentials import *

#Define URL and Web Driver
driver = webdriver.Firefox()
driver.implicitly_wait(0)


def login():
    url = "https://sellercentral.amazon.com/inventory/ref=id_invmgr_dnav_xx_?tbla_myitable=sort:%7B%22sortOrder%22%3A%22DESCENDING%22%2C%22sortedColumnId%22%3A%22date%22%7D;search:;pagination:1;"
    driver.get(url)

    try:
        #Login
        print("Logging into Amazon seller account. The price war will begin momentarily.")
        username = driver.find_element_by_name("email")
        username.send_keys(amazon_email)
        time.sleep(5)

        password = driver.find_element_by_name("password")
        password.send_keys(amazon_password)
        time.sleep(5)
        password.send_keys(Keys.RETURN)

    except:
        #Captcha Catch
        print("[*] Error in Price War: Thrwarted by Captchas")
        pass


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
            print("...exception in price matching")
            pass


def beat_price(price):
    price = float(price)
    new_price = round(price - 0.02, 2)
    return str(new_price)


def lower_price(inventory_item):
    current_price = inventory_item.get_attribute('value')
    print("...current price for item = ${}".format(current_price))
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
    matches = 0
    for row in items:
        index +=1
        better_price = row.find_elements_by_link_text("Match price")

        if len(better_price) >= 1:
            #Match price
            matches += 1
            print("Matching price for item {}".format(index))
            match_prices(better_price)

            #Select Inventory Item
            inventory_item = row.find_elements_by_xpath("//input[@maxlength='23']")[index]
            lower_price(inventory_item)
            print("...lowering price for item {}".format(index))


        else:
            print("[*] You are the price master! There are no current prices to beat.")
            pass

    #Save Changes
    save_changes()
    print("[*] Offered better prices for {} items in inventory. The price war is strong.".format(matches))
    print("....the price war will continue in 15 minutes.")
    time.sleep(5)

    #Close Driver
    driver.close()

if __name__=="__main__":
    def deploy_price_war():
        print("[*] DEPLOYING PRICE WAR")
        try:
            login()
            price_war()
        except:
            print("[*] Error in Price War: Will Restart in One Hour...")
            pass

    #Start Price War Loop
    starttime=time.time()
    while True:
      deploy_price_war()
      time.sleep(900 - ((time.time() - starttime) % 900))
