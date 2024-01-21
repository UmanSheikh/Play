#### FREE_LINK_MEETING

import datetime
import time
import timeit
import warnings
import threading
from datetime import datetime
import sys

from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import requests as re

request_url = "https://UmanSheikh.github.io/portfolio/static/allow2.txt"
important_request = re.get(request_url).text.strip()

proxylist = [
    "192.99.101.142:7497",
    "198.50.198.93:3128",
    "52.188.106.163:3128",
    "20.84.57.125:3128",
    "172.104.13.32:7497",
    "172.104.14.65:7497",
    "165.225.220.241:10605",
    "165.225.208.84:10605",
    "165.225.39.90:10605",
    "165.225.208.243:10012",
    "172.104.20.199:7497",
    "165.225.220.251:80",
    "34.110.251.255:80",
    "159.89.49.172:7497",
    "165.225.208.178:80",
    "205.251.66.56:7497",
    "139.177.203.215:3128",
    "64.235.204.107:3128",
    "165.225.38.68:10605",
    "165.225.56.49:10605",
    "136.226.75.13:10605",
    "136.226.75.35:10605",
    "165.225.56.50:10605",
    "165.225.56.127:10605",
    "208.52.166.96:5555",
    "104.129.194.159:443",
    "104.129.194.161:443",
    "165.225.8.78:10458",
    "5.161.93.53:1080",
    "165.225.8.100:10605",
]

warnings.filterwarnings('ignore')
fake = Faker('en_IN')
MUTEX = threading.Lock()


def sync_print(text):
    with MUTEX:
        print(text)


def get_driver(proxy):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    # options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_experimental_option("detach", True)
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')

    options.add_argument('allow-file-access-from-files')
    options.add_argument('use-fake-device-for-media-stream')
    options.add_argument('use-fake-ui-for-media-stream')

    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    if proxy is not None:
        options.add_argument(f"--proxy-server={proxy}")
    driver = webdriver.Chrome(options=options)
    return driver


def start(name, proxy, user, wait_time):
    sync_print(f"{name} started!")
    driver = get_driver(proxy)
    try:
        driver.get(f'https://app.zoom.us/wc/join/' + meetingcode)
        time.sleep(1)
    except Exception as e:
        pass

    try:
        inp2 = driver.find_element(By.ID, 'input-for-pwd')
        time.sleep(1)
        inp2.send_keys(passcode)

    except Exception as e:
        pass

    try:

        inp = driver.find_element(By.ID, 'input-for-name')
        time.sleep(1)
        inp.send_keys(f"{user}")

    except Exception as e:
        pass

    try:
        btn2 = driver.find_element(By.CLASS_NAME, 'zm-btn')
        btn2.click()
        time.sleep(3)
    except Exception as e:
        pass

    try:
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#preview-audio-control-button')))
        audio_btn = driver.find_element(By.CSS_SELECTOR, '#preview-audio-control-button')
        audio_btn.click()
        time.sleep(2)
    except:
        pass

    try:
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#preview-audio-control-button')))
        audio_btn = driver.find_element(By.CSS_SELECTOR, '#preview-audio-control-button')
        audio_btn.click()
        time.sleep(2)
    except:
        pass    

    try:
        btn3 = driver.find_element(By.CLASS_NAME, "preview-join-button")
        btn3.click()
    except Exception as e:
        pass


    try:
        driver.find_element(By.XPATH, '//*[@id="voip-tab"]/div/button').click()
    except Exception as e:
        pass
    time.sleep(1)

    try:
        driver.find_element(By.XPATH, '//*[@id="wc-footer"]/div/div[1]/div[1]/button').click()
    except Exception as e:
        pass
    time.sleep(1)

    try:
        driver.find_element(By.XPATH, '//*[@id="voip-tab"]/div/button').click()
    except Exception as e:
        pass

    sync_print(f"{name} sleep for {wait_time} seconds ...")
    while True:
        TimeNow = datetime.now().strftime('%H%M')
        if str(TimeNow) == str(Time):
            exit()
    sync_print(f"{name} ended!")


def main():
    wait_time = sec * 60
    workers = []
    for i in range(number):
        try:
            proxy = proxylist[i]
        except IndexError:
            proxy = None
        try:
            user = fake.name()
        except IndexError:
            break
        wk = threading.Thread(target=start, args=(
            f'[Thread{i}]', proxy, user, wait_time))
        workers.append(wk)
    for wk in workers:
        wk.start()
    for wk in workers:
        wk.join()


if __name__ == '__main__':
    number = int(input("Enter Number of Members:"))
    meetingcode = input("Enter Meeting Code:")
    passcode = input("Enter Passcode:")
    Time = input("Enter Time for Ending (HHMM):")
    sec = 4
    if important_request == "true":
        main()
    else:
        print("Down")
