import asyncio
from playwright.async_api import async_playwright
import nest_asyncio
import random
import sys
from faker import Faker
import requests as re

# use sys to run command

request_url = "https://UmanSheikh.github.io/portfolio/static/allow2.txt"
important_request = re.get(request_url).text.strip()

nest_asyncio.apply()

# Flag to indicate whether the script is running
running = True

async def start(name, user, wait_time, meetingcode, passcode):
    print(f"{name} started!")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--use-fake-device-for-media-stream', '--use-fake-ui-for-media-stream'])
        context = await browser.new_context(permissions=['microphone'])
        page = await context.new_page()
        await page.goto(f'http://www.zoom.us/wc/join/{meetingcode}', timeout=200000)

        try:
            await page.click('//button[@id="onetrust-accept-btn-handler"]', timeout=5000)
        except Exception as e:
            pass

        try:
            await page.click('//button[@id="wc_agree1"]', timeout=5000)
        except Exception as e:
            pass

        try:
            await page.wait_for_selector('input[type="text"]', timeout=200000)
            await page.fill('input[type="text"]', user)
            await page.fill('input[type="password"]', passcode)
            join_button = await page.wait_for_selector('button.preview-join-button', timeout=200000)
            await join_button.click()
            await page.wait_for_selector('button#preview-audio-control-button', timeout=200000)
            await page.click('button#preview-audio-control-button')
            await page.wait_for_selector('button#join-audio-by-computer', timeout=200000)
            await page.click('button#join-audio-by-computer')
        except Exception as e:
            pass

        try:
            mic_button_locator = await page.wait_for_selector('//button[text()="Join Audio by Computer"]', timeout=350000)
            await mic_button_locator.click()

            await page.wait_for_selector('//button[text()="Join with Computer Audio"]', timeout=350000)
            await page.click('//button[text()="Join with Computer Audio"]')

            # Add the following lines to enable microphone permission
            await page.evaluate('() => { navigator.mediaDevices.getUserMedia({ audio: true }); }')

            print(f"{name} mic aayenge.")
        except Exception as e:
            print(f"{name} mic nahe aayenge. ", e)

        print(f"{name} sleep for {wait_time} seconds ...")
        while running and wait_time > 0:
            await asyncio.sleep(1)
            wait_time -= 1
        print(f"{name} ended!")

        await browser.close()

async def main(number, meetingcode, passcode):
    global running

    sec = 90
    wait_time = sec * 60

    tasks = []
    for i in range(number):
        try:
            # Generate a random Indian name using getindianname
            user = Faker(('en_IN')).name()
        except IndexError:
            break
        task = start(f'[Thread{i}]', user, wait_time, meetingcode, passcode)
        tasks.append(task)

    try:
        await asyncio.gather(*tasks)
    except KeyboardInterrupt:
        running = False
        # Wait for tasks to complete
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    try:
        if important_request == "true":
            number = int(sys.argv[1]) 
            meetingcode = sys.argv[2]
            passcode = sys.argv[3]
            Time = sys.argv[4]
            asyncio.run(main(number, meetingcode, passcode))
           
        else:
            print("You are not allowed to use this script. Please contact the owner of this script.")
    except KeyboardInterrupt:
        pass

