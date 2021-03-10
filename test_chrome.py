from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options

class SendMessageFacebook:
    
    def __init__(self, filename, msg_content):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 1 
        })

        fh = open(filename)
        link =" "

        # Step 1) Open Firefox 
        browser = webdriver.Chrome(chrome_options=option, executable_path=r'C:/Users/USER/Desktop/facebook-automation/chromedriver.exe')

        # Step 2) Navigate to Facebook
        browser.get("http://www.facebook.com")

        # Step 3) Search & Enter the Email or Phone field & Enter Password
        username = browser.find_element_by_css_selector(f'[data-testid="royal_email"]')
        password = browser.find_element_by_css_selector(f'[data-testid="royal_pass"]')
        submit   = browser.find_element_by_css_selector(f'[data-testid="royal_login_button"]')
        username.send_keys("cokolat004@yahoo.co.uk")
        password.send_keys("Silent1/")

        # Step 4) Click Login
        submit.click()
        time.sleep(1)

        while(link):
            link = fh.readline()
            browser.get(link)
            time.sleep(3)

            message = browser.find_element_by_css_selector(f'[aria-label="Message"]')
            time.sleep(1)

            message.click()
            time.sleep(5)

            actions = browser.find_element_by_css_selector(f'[aria-label="Aa"]')
            time.sleep(3)

            actions.send_keys(msg_content)
            actions.submit()
            time.sleep(3)

        browser.quit()