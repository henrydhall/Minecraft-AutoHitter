#!python
"""
#Minecraft Autohitter
#Created 6/18/2021 by Henry Hall for python 3.7.3 on Windows
#To be used for hitting on Minecraft while standing in front of an active farm
#to automate loot and xp collection.
#dependencies: pyautogui, time, pyinputplus
#other dependencies: MouseFixerScript.py (included in git repository).
#minecraft dependencies: skeleton or zombie spawner farm as in https://www.youtube.com/watch?v=NEMuNX0ru6Q
"""

"""
#To use:
# 1. Situate yourself in front of the area where mobs will fall.
#    a. Put food in hand so that the script will be able to eat.
#    b. You'll have 10 seconds before the script begins clicking.
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
#Enter 'y' where prompted and put focus on Minecraft window and get out of any menus.
#If you are not prompted to run the script you will need to run the script on your own.
#But honestly if you've made it this far you should know how to run it.
"""

import pyautogui, time, pyinputplus, MouseFixerScript

def hitOnce():
    pyautogui.click()

def eatFood():
    pyautogui.mouseDown(button='right')
    time.sleep(2)
    pyautogui.mouseUp()

def afkXPFarm():
    eating = False
    time.sleep(10)
    while True:
        try:
            for i in range(0,10):
                hitOnce()
                time.sleep(1)
            eating = True
            eatFood()
            eating = False
        except pyautogui.FailSafeException:
            if eating:
                print("Mouse control might be abnormal in active Minecraft session.")
                print("Run MouseFixerScript.py to correct problems.")
                runMouseFixerScript = input("Enter 'y' to run MouseFixerScript.py now: ")
                if runMouseFixerScript == "y":
                    MouseFixerScript.fixRightClick()
            if not eating:
                print("Ended script.")
                print("  Mouse control should be normal.")
            break
    
afkXPFarm()
    
