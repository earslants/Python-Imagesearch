import cv2
import numpy as np
import pyautogui
import time
from python_imagesearch import imagesearch
from matplotlib import pyplot as plt

def openZoom(meetingId,meetingPw,name):
    # Zoom app image
    zoom = imagesearch.imagesearch('Images/zoom.png')
    # Join image
    join = imagesearch.imagesearch('Images/join.png')
    # ID image
    id = imagesearch.imagesearch('Images/id.png')
    # Close video checkbox
    videoCb = imagesearch.imagesearch('Images/videoCb.png')
    # Close voice checkbox
    sesCb = imagesearch.imagesearch('Images/sesCb.png')
    # Password screen
    pwScreen = imagesearch.imagesearch('Images/pwScreen.png')

    if zoom[0] != -1:
        pyautogui.moveTo(zoom)
        time.sleep(0.1)
        pyautogui.doubleClick()
    else:
        while zoom[0] == -1:
            zoom = imagesearch.imagesearch('Images/zoom.png')
            if zoom[0] != -1:
                pyautogui.moveTo(zoom)
                time.sleep(0.1)
                pyautogui.doubleClick()
                break

    while join[0] == -1:
        join = imagesearch.imagesearch('Images/join.png')
        time.sleep(1)
        if join[0] != -1:
            pyautogui.moveTo(join[0]+120,join[1]+15)
            time.sleep(0.1)
            pyautogui.click()
            break

    # in meeting id screen

    while id[0] == -1:
        id = imagesearch.imagesearch('Images/id.png')
        if id[0] != -1:
            pyautogui.moveTo(id[0]+73,id[1]+26)
            x,y = id[0]+73,id[1]+26
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.write(meetingId)
            time.sleep(1)
            pyautogui.moveTo(x,y+70)
            time.sleep(0.1)
            pyautogui.tripleClick()
            pyautogui.write(name)
            time.sleep(1)
            videoCb = imagesearch.imagesearch('Images/videoCb.png')
            if videoCb != -1:
                pyautogui.moveTo(videoCb[0]+3,videoCb[1]+2)
                time.sleep(0.2)
                pyautogui.click()
            time.sleep(1)
            sesCb = imagesearch.imagesearch('Images/sesCb.png')
            if sesCb != -1:
                pyautogui.moveTo(sesCb[0]+3,sesCb[1]+2)
                time.sleep(0.2)
                pyautogui.click()
                time.sleep(0.2)
                pyautogui.moveTo(20,20)
            time.sleep(1)
            checkbox = imagesearch.imagesearch('Images/checkbox.png')
            if checkbox[0] != -1:
                join2 = imagesearch.imagesearch('Images/join2.png')
                pyautogui.moveTo(join2[0] + 10, join2[1] + 10)
                time.sleep(0.1)
                pyautogui.click()
            time.sleep(1)
            break

    while pwScreen[0] == -1:
        pwScreen = imagesearch.imagesearch('Images/pwScreen.png')
        if pwScreen[0] != -1:
            time.sleep(0.5)
            pyautogui.write(meetingPw)

        time.sleep(1)
        join3 = imagesearch.imagesearch('Images/join3.png')
        if join3[0] != -1:
            pyautogui.moveTo(join3[0]+20,join3[1]+10)
            time.sleep(0.2)
            pyautogui.click()
        time.sleep(1)
        break

if __name__ == '__main__':

    meetingId = input("Please enter Meeting ID : ")
    meetingPw = input("Please enter Meeting Password : ")
    name = input("Please enter your name : ")

    openZoom(meetingId,meetingPw,name)




