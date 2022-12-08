from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pickle
from os.path import exists
from sys import platform
import time
import random

def VirtualClick(driver, click_object):
    size = click_object.size
    sizeList = list(size.values())
    height_rand = random.randint(1,int(sizeList[0])-1)
    width_rand = random.randint(1,int(sizeList[1])-1)
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(click_object, width_rand, height_rand)
    action.click()
    action.perform()
    return True

opening_line = "AUUUUUU!"
number_of_swipes = 1000000

if platform == "linux" or platform == "linux2":
    chromedriver_path = "/usr/local/bin/chromedriver" # COLAR A PASTA DO WEBDRIVER AQUI 
else:
    chromedriver_path = "mac/chromedriver" # COLAR A PASTA DO WEBDRIVER AQUI 

service = Service(executable_path=chromedriver_path)
web = 'https://bumble.com/app'
options = Options()
driver = webdriver.Chrome(options=options, executable_path=chromedriver_path)

driver.get(web)

# if exists("cookies.pkl"):
#     cookies = pickle.load(open("cookies.pkl", "rb"))
# else:
#     pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
#     cookies = pickle.load(open("cookies.pkl", "rb"))
# if cookies:
#     for cookie in cookies:
#         driver.add_cookie(cookie)

print('Tu tem 20 segundos pra fazer o login')
for num in range(1, 21):
    print(f"Tu tem {20-num} segundos pra fazer o login")
    time.sleep(1)
print('Iniciando a bagaca')

for i in range(number_of_swipes):
    try:
        time.sleep(2)
        like_button = driver.find_element(by='xpath', value='/html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]')
        VirtualClick(driver, like_button)
        print("Gostei")

        # its_match_window = driver.find_element(by='xpath', value='//textarea[@placeholder="Say something nice!"]')
        # its_match_window.send_keys(opening_line)
        # time.sleep(1)

        # send_message_button = driver.find_element(by='xpath', value='//button/span[text()="Send"]')
        # send_message_button.click()
        # time.sleep(1)

        # close_its_match_window = driver.find_element(by='xpath', value='//button[@title="Back to Tinder"]')
        # close_its_match_window.click()

    except Exception as e:
        time.sleep(10)
        pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
        print('erro')
        print(e)
