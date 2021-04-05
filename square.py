import pyautogui
import time
import random
pyautogui.press("win")
pyautogui.write("paint")
pyautogui.press("enter")
time.sleep(3)
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

    
# r = 50
# centrex = 960
# centrey = 540

# y = centrey - r
# x = math.sqrt((r ** 2) - ((y - centrey) ** 2)) + centrex

# oldx = x
# oldy = y

# for i in range(r):
#     pyautogui.moveTo(x, y)
#     x = math.sqrt((r ** 2) - ((y - centrey) ** 2)) + centrex
#     pyautogui.dragTo(x, y)
#     tempx = centrex - math.sqrt((r ** 2) - ((y - centrey) ** 2))
#     tempoldx = centrex - math.sqrt((r ** 2) - ((oldy - centrey) ** 2))
#     pyautogui.moveTo(tempoldx, oldy)
#     pyautogui.dragTo(tempx, y)
#     pyautogui.dragTo(x, y) # comment this line if you want to disable fill

#     oldx = x
#     oldy = y

#     y = y + 1