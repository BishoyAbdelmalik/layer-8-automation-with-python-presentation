import pyautogui
import time
pyautogui.press("win")
pyautogui.write("paint")
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("win","up")
x=100
y=200
pyautogui.moveTo(x,y)

for i in range(10):
    x+=500-(i*50)
    pyautogui.dragTo(x,y)
    y+=500-(i*50)
    pyautogui.dragTo(x,y)
    x-=500-(i*50)
    pyautogui.dragTo(x,y)
    y-=500-((i+1)*50)
    pyautogui.dragTo(x,y)
