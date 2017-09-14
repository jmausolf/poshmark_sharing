import selenium, time, argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Your Credentials File
from credentials import *
import pdb


def login():
    url = "https://poshmark.com/login"
    driver.get(url)
    time.sleep(5)

    try:
        #Login
        print("[*] logging into Poshmark seller account...the share war will begin momentarily...")
        username = driver.find_element_by_name("login_form[username_email]")
        username.send_keys(poshmark_email)
        time.sleep(5)

        password = driver.find_element_by_name("login_form[password]")
        password.send_keys(poshmark_password)
        time.sleep(5)

        password.send_keys(Keys.RETURN)
        time.sleep(5)

        #Check for Captcha
        try:
            captcha_fail = driver.find_element_by_xpath("//span[@class='base_error_message']")
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

    except:
        #Captcha Catch
        print("[*] ERROR in Share War: Thrwarted by Captchas")
        login_pdb()
        pass


def login_pdb():

    try:
        import pdb; pdb.set_trace()

        #Login
        username = driver.find_element_by_name("login_form[username_email]")
        username.clear()
        username.send_keys(poshmark_email)
        time.sleep(5)

        password = driver.find_element_by_name("login_form[password]")
        password.send_keys(poshmark_password)
        time.sleep(5)
        password.send_keys(Keys.RETURN)

        #Navigate to Seller Page
        time.sleep(5)
        seller_page = "https://poshmark.com/closet/couponingstacy?availability=available"
        driver.get(seller_page)

    except:
        print("[*] ERROR in Share War: Thrwarted by Captchas")
        pass


def scroll_page(n, delay=3):
    scroll = 0
    print("[*] scrolling through all items in closet...")
    for i in range(1, n+1):
        scroll +=1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)


def get_closet_urls():
    items = driver.find_elements_by_xpath("//div[@class='item-details']")
    urls = [item.find_element_by_css_selector('a').get_attribute('href') for item in items]
    return urls


def get_closet_share_icons():
    items = driver.find_elements_by_xpath("//div[@class='social-info d-fl ai-c jc-c']")
    share_icons = [item.find_element_by_css_selector("a[class='share']") for item in items]
    return share_icons


def clicks_share_followers(share_icon, delay=1):
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


def deploy_share_war(n=3):
    print("[*] DEPLOYING SHARE WAR")

    try:
        login()
        scroll_page(n)
        share_icons = get_closet_share_icons()

        print("[*] sharing PoshMark listings for {} items in closet...".format(len(share_icons)))
        print("[*] please wait...")

        #Share Listings
        [clicks_share_followers(item) for item in share_icons]

        print("[*] closet successfully shared...posh-on...")
        pass

    except:
        print("[*] ERROR in Share War")
        pass


    print("[*] the share war will continue in {} minutes...current time: {}".format(int(args.time/60), time.strftime('%l:%M%p %Z on %b %d, %Y')))


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", default=3600, type=float, help="time in seconds")
    parser.add_argument("-n", "--number", default=3, type=int, help="number of closet scrolls")
    args = parser.parse_args()

    #Start Share War Loop
    starttime=time.time()

    while True:
        #Start Driver, Get URLS, Close
        driver = webdriver.Firefox()
        driver.implicitly_wait(0)

        #Run Main App
        deploy_share_war(args.number)

        time.sleep(5)
        driver.close()

        #Time Delay: While Loop
        time.sleep(args.time - ((time.time() - starttime) % args.time))
