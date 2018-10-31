import cv2,time,pyautogui
import numpy as np
import pygame.time
from PIL import ImageGrab
import webbrowser
webbrowser.open_new("http://www.trex-game.skipser.com/")
restart=(680,390)
time.sleep(10)
pyautogui.click(restart)
jumps=0
clo=pygame.time.Clock()
tt=time.time()
pyautogui.keyDown("space")
pyautogui.keyUp("space")
import pynput
b=pynput.keyboard.Controller()
space=pynput.keyboard.Key.space
down=pynput.keyboard.Key.down
while(1):
    imgt=ImageGrab.grab((550,395,560,425))
    #print(sum(imgt.getcolors()[0][1]))
    if 700>sum(imgt.getcolors()[0][1]):
        jumps=jumps+1
        print(jumps)
        b.press(space)
########        pyautogui.keyDown("space")
########        time.sleep(0.05)
########        pyautogui.keyUp("space")
##    else:
##        imgb=ImageGrab.grab((590,395,600,400))
##        if 700>sum(imgb.getcolors()[0][1]):
##            jumps=jumps+1
##            print(jumps)
##            b.press(down)
########            pyautogui.keyDown("down")
########            time.sleep(0.5)
########            pyautogui.keyUp("down")
####    print(time.time()-tt)
####    tt=time.time()
    #clo.tick(30)
