# https://pyautogui.readthedocs.io/en/latest/quickstart.html
# open email in a tab on main screen, run this program on a monitor.
# if you have the same resolution as me, it will work
import pyautogui as gui

gui.PAUSE = 0.1

while(True):
    gui.moveTo(140, 90+110, duration=0.5)
    gui.click()
    gui.moveTo(1330, 380+110, duration=0.5)
    gui.click()
    gui.typewrite("YOUREMAIL@gmail.com", interval=0.01)
    gui.moveRel(0, 30, duration=0.5)
    gui.doubleClick()
    gui.typewrite("This is an automated message", interval=0.01)
    gui.moveRel(0, 34, duration=0.5)
    gui.click()
    gui.typewrite("Your car's extended warranty has expired", interval=0.01)
    gui.moveTo(1293, 893+110, duration=0.5)
    gui.click()