import selenium, time, argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Your Amazon Credentials File
from credentials import *


def login():
    #url = "https://poshmark.com/closet/couponingstacy?availability=available"
    url = "https://poshmark.com/login"
    driver.get(url)

    try:
        #Login
        print("Logging into Poshmark seller account. The price war will begin momentarily.")
        username = driver.find_element_by_name("login_form[username_email]")
        username.send_keys(poshmark_email)
        time.sleep(5)

        password = driver.find_element_by_name("login_form[password]")
        password.send_keys(poshmark_password)
        time.sleep(5)
        password.send_keys(Keys.RETURN)

        #Navigate to Seller Page
        seller_page = "https://poshmark.com/closet/couponingstacy?availability=available"
        driver.get(seller_page)

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
    new_price = round(price - 0.01, 2)
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
            pass

    #Save Changes
    save_changes()
    print("[*] Offered better prices for {} items in inventory. The price war is strong.".format(matches))



if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", default=900, type=float, help="time in seconds")
    args = parser.parse_args()

    def deploy_price_war():
        print("[*] DEPLOYING PRICE WAR")

        #import pdb; pdb.set_trace()
        try:
            login()
            #price_war()
        except:
            print("[*] Error in Price War")
            pass

        print("....the price war will continue in {} minutes. Current time: {}".format(int(args.time/60), time.strftime('%l:%M%p %Z on %b %d, %Y')))


    #Start Price War Loop
    starttime=time.time()

    while True:
        #Start Driver, Run, Close
        driver = webdriver.Firefox()
        driver.implicitly_wait(0)
        deploy_price_war()
        time.sleep(15)
        driver.close()

        #Time Delay: While Loop
        time.sleep(args.time - ((time.time() - starttime) % args.time))
