from PIL import ImageOps
import pyscreenshot as ImageGrab
import pyautogui
import time
from numpy import *
import os
class Cordinates():
    replayBtn = (309,444)
    dinasaur = (136,465)
    #220 = x coordinate to check for tree
    #455 = y coordinate for half tree
    #134, 461 coordinate for bird

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')


def imageGrab():
    box = (Cordinates.dinasaur[0] + 76, Cordinates.dinasaur[1],
           Cordinates.dinasaur[0] + 100, Cordinates.dinasaur[1] + 10)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return(a.sum())

def main():
    restartGame()
    while True:
        if not imageGrab() == 3127:
            print("here comes tree")
            pressSpace()
            time.sleep(0.1)

main()