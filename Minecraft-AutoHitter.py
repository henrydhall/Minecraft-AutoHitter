#!python
"""
#Minecraft Autohitter
#Created 6/18/2021 by Henry Hall for python 3.7.3 on Windows
#To be used for hitting on Minecraft while standing in front of an active farm
#to automate loot and xp collection.
#dependencies: pyautogui, time
#minecraft dependencies: skeleton or zombie spawner farm as in https://www.youtube.com/watch?v=NEMuNX0ru6Q
"""

"""
#To use:
# 1. Situate yourself in front of the area where mobs will fall.
#    a. Put food in hand so that the script will be able to eat.
# 2. Start script (if using IDLE press F5)
# 3. Enter minecraft window, aim to where you want to hit.
# 4. Once the script begins and starts hitting make sure mobs die.
# 5. Allow to run for as long as you want.
# 6. To end script see note below.
"""

"""
#Important!
#To end script: take focus away from minecraft by hitting exit,
#and move cursor to a corner of the screen for several seconds.
#make sure that it isn't while the script is trying to eat or
#it will not release the right mouse button.
"""

"""
#If you end script and mouse becomes unresponsive:
#Restart script, wait until hits begin again, and retry ending the script
#by moving the cursor to the corner of the screen.
#As of yet I have been unable to create another script to fix this problem,
#but it will be included as soon as I can figure that out.
"""

import pyautogui, time

def hitOnce():
    pyautogui.click()

def eatFood():
    pyautogui.mouseDown(button='right')
    time.sleep(2)
    pyautogui.mouseUp()

def afkXPFarm():
    time.sleep(10)
    while True:
        for i in range(0,10):
            hitOnce()
            time.sleep(1)
        eatFood()

afkXPFarm()
    
