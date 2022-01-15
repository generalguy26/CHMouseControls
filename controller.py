# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:26:25 2021

@author: generalguy
"""

from pynput import mouse

import pyvjoy

from PIL import Image
import numpy as np

j = pyvjoy.VJoyDevice(1)
current = None
mouseState = None

r = {1:1, 2:2, 3:3, 4:4, 5:5}

img = Image.open("CHmap V2.jpg", "r")

def coordToButton(x,y):
    rgbval = img.getpixel((x,y))
    if np.all(rgbval == (0, 255, 1)):
        return 1
    elif np.all(rgbval == (254, 0, 0)):
        return 2
    elif np.all(rgbval == (255, 255, 1)) or np.all(rgbval == (255, 255, 0)):
        return 3
    elif np.all(rgbval == (0, 0, 254)):
        return 4
    elif np.any(rgbval == (241, 90, 37)):
        return 5
    else:
        return None
    

def on_move(x, y):                                              #when mouse is moved, x y are coordinates of mouse
    global current                                              #old region of screen mouse is in
    try:
        new = coordToButton(x,y)                                 #determine what region mouse is currently in
        if new != current and current != None and mouseState:   #if new region is different than old region and the mouse is being clicked
                                                                #and the old region is defined
            j.set_button(current, 0)                            #turn off the old button
            current = new                                       #set the old value to the new value

            print(current)
            j.set_button(current, 1)                            #turn on the new button
        elif current == None and mouseState and new is not None:  #else if this is the first time mouse region is being recorded
            current = new                                       #set the current mouse region
            print(current)
            j.set_button(current, 1)                            #turn on the button corresponding to that region
    except:
        pass

def on_click(x, y, button, pressed):
    global mouseState
    mouseState = pressed
    print(pressed)
    if pressed:
        new = coordToButton(x,y)                                 #determine what region mouse is currently in
        print(new)
        if new is not None:
            j.set_button(new, 1)
    if not pressed:
        j.reset_buttons()

def on_release(key):
    pass
l2 = mouse.Listener(on_move=on_move, on_click=on_click)
l2.start()

def stopL():
    l2.stop()
    
input()
stopL()