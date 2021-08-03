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

def fixRightClick():
    time.sleep(5)
    pyautogui.mouseUp()
    print("Attempted to restore mouse control. Run again if unsuccessful")

fixRightClick()
