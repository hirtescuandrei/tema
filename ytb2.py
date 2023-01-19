import pyautogui
import time
import keyboard


def cautare_google():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'D:\temaMAP\cod.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\temaMAP\cod.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('https://youtube.com')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")

def cautare_youtube():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'D:\temaMAP\cod2.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\temaMAP\cod2.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('life of boris')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")

def cautare_boris():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'D:\temaMAP\cod3.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\temaMAP\cod3.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")

def cautare_subscribe():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'D:\temaMAP\cod4.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\temaMAP\cod4.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")  

def coordonate():
    print(pyautogui.position())

col=1

while not keyboard.is_pressed('esc'):
    coordonate()



cautare_google()
cautare_youtube()
cautare_boris()
cautare_subscribe()