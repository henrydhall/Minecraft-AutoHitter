# Minecraft-AutoHitter
Created 6/18/2021 by Henry Hall for Python 3.7.3 on Windows.
Module Dependencies: time, pyautogui
Minecraft dependencies: skeleton or zombie spawner farm as in https://www.youtube.com/watch?v=NEMuNX0ru6Q
It might work for other farms as well, just make sure you're safe to afk and you can hit the mobs.

## Usage:
1. Stand in front of the area where mobs fall.
2. Put food in hand so that the script will be able to eat.
3. Start script.
4. Enter Minecraft window, aim to where you want to hit.
5. The script will start hitting after 10 seconds.
6. The script hits 10 times and then eats 1 food item.
7. Make sure that the script is hitting mobs.
8. Allow to run as long as you want.
9. While the script is hitting, not when it's eating, click exit, and quickly move the cursor to a corner of the screen.

## If mouse becomes unresponsive:
The script should detect that there could be mouse control issues. 
When prompted run the MouseFixerScript.py script by entering 'y'.
Make the Minecraft window activate and exit any menus.
After 5 second the script will run and fix mouse control.

If you have mouse control issues, but are not prompted to run the Mouse
1. Start the script.
2. Enter the minecraft window and enter gameplay (not in any menus).
3. The script will run after 5 seconds and fix mouse control.

## Future updates:
I will be testing other possible solutions to the right mouse button becoming unresponsive, and adding popups to confirm when the script has started and when it ends.

## TODO
* Fix documents.
* Refactor.
* Fix mouse problems more effectively.
* Make requirements file.
* Get virtual environment going. 
