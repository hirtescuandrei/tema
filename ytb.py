from re import T
import pyautogui
import time 
import keyboard
 
def cautare_google():
    time.sleep(5)
    if pyautogui.locateAllOnScreen(r'D:\temaMAP\1.png',confidence=0.7) !=None:
        camp_google = pyautogui.locateOnScreen(r'D:\temaMAP\1.png',confidence=0.7) 
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('https://www.youtube.com')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")
            
cautare_google()
 
def cautare_yt():
    time.sleep(5)
    if pyautogui.locateAllOnScreen(r'D:\temaMAP\2.png',confidence=0.7) !=None:
        camp_yt = pyautogui.locateOnScreen(r'D:\temaMAP\2.png',confidence=0.7) 
        pyautogui.click(camp_yt)
        time.sleep(1)
        pyautogui.write('test')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")
            
cautare_yt()
 
def click_canal():
    time.sleep(3)
    if pyautogui.locateAllOnScreen(r'D:\temaMAP\test.png',confidence=0.7) !=None:
        camp_canal = pyautogui.locateOnScreen(r'D:\temaMAP\test.png',confidence=0.7) 
        pyautogui.click(camp_canal)


    else:


        print("Imaginea nu este pe ecran")
 

    click_canal()
 
def abonare_canal():
    time.sleep(3)
    if pyautogui.locateAllOnScreen(r'D:\temaMAP\subscribe.jpg',confidence=0.7) !=None:
        camp_abonare = pyautogui.locateOnScreen(r'D:\temaMAP\subscribe.jpg',confidence=0.7) 
        pyautogui.click(camp_abonare)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")
        
abonare_canal()

