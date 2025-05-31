import pyautogui
import time

# Coordinates of the three points
points = [
    (233, 592),
    (271, 747),
    (1025, 702)
]

# Number of repetitions
repeats = 200

# Delay between individual clicks (in seconds)
click_delay = 1

# Delay after each cycle of 3 clicks (in seconds)
cycle_delay = 2

print("Auto-clicker will start in 10 seconds... Don't move the mouse!")
time.sleep(10)

for i in range(repeats):
    print(f"Repeat {i + 1} of {repeats}")
    for point in points:
        pyautogui.click(point[0], point[1])
        time.sleep(click_delay)  # delay between individual clicks
    time.sleep(cycle_delay)  # delay after full cycle

print("Clicking completed ✅")
