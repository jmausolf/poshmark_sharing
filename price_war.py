import selenium, time, argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Your Amazon Credentials File
from credentials import *
import pdb


def login():
    url = "https://poshmark.com/login"
    driver.get(url)
    time.sleep(5)

    try:
        #Login
        print("Logging into Poshmark seller account. The price war will begin momentarily.")
        username = driver.find_element_by_name("login_form[username_email]")
        username.send_keys(poshmark_email)
        time.sleep(5)

        #pdb.set_trace()
        password = driver.find_element_by_name("login_form[password]")
        password.send_keys(poshmark_password)
        time.sleep(5)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        #import pdb; pdb.set_trace()
        #Check for Captcha
        try:
            #x = driver.find_element_by_name("base_error_message")
            captcha_fail = driver.find_element_by_xpath("//span[@class='base_error_message']")
            #captcha_fail = driver.find_element_by_xpath("//div[@class='rc-anchor-alert']")
            if len(str(captcha_fail)) > 100:
                print(("[*] Caught by Captchas: Proceed to Debugger in terminal..."))
                import pdb; pdb.set_trace()
                print(("[*] Please complete captchas, robots game before proceeding..."))
                login_pdb()
                return
            else:
                pass
        except:
            pass

        #Navigate to Seller Page
        time.sleep(10)
        seller_page = "https://poshmark.com/closet/couponingstacy?availability=available"
        driver.get(seller_page)
        #https://poshmark.com/closet/couponingstacy

    except:
        #Captcha Catch
        print("[*] Error in Price War: Thrwarted by Captchas")
        login_pdb()
        pass

def login_pdb():
    #url = "https://poshmark.com/login"
    #driver.get(url)
    #time.sleep(5)

    try:
        import pdb; pdb.set_trace()
        #pdb.set_trace()
        #Login
        #print("Logging into Poshmark seller account. The price war will begin momentarily.")
        username = driver.find_element_by_name("login_form[username_email]")
        username.clear()
        username.send_keys(poshmark_email)
        time.sleep(5)

        #pdb.set_trace()
        password = driver.find_element_by_name("login_form[password]")
        password.send_keys(poshmark_password)
        time.sleep(5)
        password.send_keys(Keys.RETURN)

        #Navigate to Seller Page
        time.sleep(5)
        seller_page = "https://poshmark.com/closet/couponingstacy?availability=available"
        driver.get(seller_page)

    except:
        #Captcha Catch
        print("[*] Error in Price War: Thrwarted by Captchas")
        pass


## USER FUNCTIONS FOR PRICE CHANGES

#from helper_functions import *
#Scroll Function
def scroll_page(n, delay=3):
    scroll = 0
    for i in range(1, n+1):
        scroll +=1
        print("scrolling page...scroll number {} of {}".format(i, n))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    #TODO get function to scoll until end

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

def get_closet_urls():
    items = driver.find_elements_by_xpath("//div[@class='item-details']")
    #Get URLs from Items
    urls = [item.find_element_by_css_selector('a').get_attribute('href') for item in items]
    return urls

def get_closet_share_icons():
    #pdb.set_trace()
    items = driver.find_elements_by_xpath("//div[@class='social-info d-fl ai-c jc-c']")
    #Get URLs from Items
    share_icons = [item.find_element_by_css_selector("a[class='share']") for item in items]
    #share_icons = [item.find_element_by_xpath("//a[@class='share']") for item in items]
    #share_icons[1].click()
    #share_icons[1].send_keys(selenium.webdriver.common.keys.Keys.SPACE)

    return share_icons

def clicks_share_followers(share_icon, delay=1.5):
    d = delay

    #First share click
    driver.execute_script("arguments[0].click();", share_icon); time.sleep(d)

    #Second share click
    share_followers = driver.find_element_by_xpath("//a[@class='pm-followers-share-link grey']")
    driver.execute_script("arguments[0].click();", share_followers); time.sleep(d)

def share(d=1):
    #shortcut to reshare in debugger mode
    [clicks_share_followers(item, d) for item in share_icons]

def open_closet_item_url(url):
    print(url)
    driver.get(url)
    time.sleep(5)



## MAIN FUNCTION TO RUN PRICE WAR

def price_war():

    #Poshmark Items Links
    items = driver.find_elements_by_xpath("//div[@class='item-details']")
    len(items)

    url_stem = "https://poshmark.com/closet/couponingstacy?availability=available"

    index = -1
    matches = 0
    #for item in items:

    #Get URLs from Items
    urls = [item.find_element_by_css_selector('a').get_attribute('href') for item in items]
	#xls_files_stems = set([f.split(".")[0] for f in os.listdir(".") if f.endswith('.xlsx')])

    for item in items:
        url = item.find_element_by_css_selector('a').get_attribute('href')
        print(url)
        driver.get(url)
        #do stuff
        #better_price = row.find_elements_by_link_text("Match price")
        time.sleep(2)


def deploy_price_war():
    print("[*] DEPLOYING PRICE WAR")

    try:
        login()
        scroll_page(5)
        return
    except:
        print("[*] Error in Price War")
        pass

        #print("....the price war will continue in {} minutes. Current time: {}".format(int(args.time/60), time.strftime('%l:%M%p %Z on %b %d, %Y')))


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", default=3600, type=float, help="time in seconds")
    args = parser.parse_args()

    #deploy_price_war()

    #Start Price War Loop
    starttime=time.time()

    while True:
        #Start Driver, Get URLS, Close
        driver = webdriver.Firefox()
        driver.implicitly_wait(0)
        deploy_price_war()

        urls = get_closet_urls()
        share_icons = get_closet_share_icons()


        #Share Listings
        #[clicks_share_followers(item) for item in share_icons]
        [clicks_share_followers(item, 3) for item in share_icons]

        time.sleep(5)

        #Open Listing URLs
        #[open_closet_item_url(url) for url in urls]

        time.sleep(5)
        driver.close()

        #Time Delay: While Loop
        time.sleep(args.time - ((time.time() - starttime) % args.time))
