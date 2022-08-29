import mouse
import win32api, win32con
import pyautogui
import time
import keyboard

print(pyautogui.position())
# mouse.move(100, 100, absolute=False, duration=0.2)
# mouse.click('left')

#
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


while True:
    click(1250, 728)
    click(1250, 728)
    time.sleep(0.5)
    click(1618, 962)

    password = "0911"
    keyboard.write(password)
    keyboard.press("enter")
    time.sleep(0.5)
    click(1658, 848)
