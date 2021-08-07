#!python
"""
#MouseFixerScript
#Created 7/27/2021 by Henry Hall for python 3.7.3 on Windows
#Used in case of loss of mouse control using Minecraft-Autohitter script
#Dependencies: pyautogui, time
"""

"""
#To use:
# 1. Start script
# 2. Open Minecraft and enter gameplay.
#   a. Basically make sure you're not in inventory or the pause menu.
# 3. The script will run after 5 seconds and will return mouse control for the window to normal
"""

import pyautogui, time

def countDown(delay = 5):
    print( f"Mouse fixer will run in {delay} seconds." )
    for i in range(0,delay):
        print( delay - i )
        time.sleep(1)

def fixRightClick():
    countDown()
    pyautogui.mouseUp()
    print("Attempted to restore mouse control. Run again if needed.")

if __name__ == '__main__':
    fixRightClick()
