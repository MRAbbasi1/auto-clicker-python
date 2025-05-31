import pyautogui
import time

print("Move the mouse to the desired point (you have 5 seconds)(Make sure target is static | fullscreen)...")
time.sleep(5)
x, y = pyautogui.position()
print(f"Coordinates: {x}, {y}")
