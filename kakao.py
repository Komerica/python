import pyautogui
import keyboard
import time

# Set the minimum duration and sleep time to 0.01 seconds
pyautogui.MINIMUM_DURATION = 0.01
pyautogui.MINIMUM_SLEEP = 0.01

# Sleep for 5 seconds
time.sleep(5)

while True:
    # Click the mouse 25 times per second
    for i in range(25):
        pyautogui.click()
    # Check if the "Ctrl + Alt + Shift + S" key combination has been pressed
    if keyboard.is_pressed('ctrl+alt+shift+s'):
        # If the key combination has been pressed, stop clicking and exit the program
        break
    time.sleep(0.01)
