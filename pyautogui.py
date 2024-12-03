import pyautogui 
import time
time.sleep(9)
sentence = "today is good"
res = sentence.split("")
for word in res:
    pyautogui.write(word)
    pyautogui.press("enter")
