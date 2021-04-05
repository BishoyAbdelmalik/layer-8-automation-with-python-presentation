from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pyautogui
import asyncio
import websockets
import json
import time
import shutil
import os

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("https://csun.zoom.us/my/bishoyabdelmalik?pwd=bDJvanR6ZHdJRnFZU21zYzhxZUdqQT09")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
driver.quit()
pyautogui.press("win")
pyautogui.write("obs")
pyautogui.press("enter")

async def record():
    uri = "ws://localhost:4444"
    async with websockets.connect(uri) as websocket:
        msg = {"request-type":"StartRecording","message-id":"recordingstart"}
        msg = json.dumps(msg)
        await websocket.send(msg)
        print(f"> {msg}")

        response = await websocket.recv()
        print(f"< {response}")
asyncio.get_event_loop().run_until_complete(record())
time.sleep(10)
async def stop_recording():
    uri = "ws://localhost:4444"
    async with websockets.connect(uri) as websocket:
        msg = {"request-type":"StopRecording","message-id":"recordingstop"}
        msg = json.dumps(msg)
        await websocket.send(msg)
        print(f"> {msg}")

        response = await websocket.recv()

        response = await websocket.recv()
        response = json.loads(response)
        location = response["recordingFilename"]
        print(f"< {location}")
        time.sleep(5)
        os.system('taskkill /f /im obs64.exe')

        shutil.move(os.path.abspath(location), os.getcwd()+"\\"+os.path.basename(location))

        
asyncio.get_event_loop().run_until_complete(stop_recording())
