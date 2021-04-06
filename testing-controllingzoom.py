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
time.sleep(6)
pyautogui.press("tab")
pyautogui.hotkey("shift","tab")
pyautogui.press("enter")

