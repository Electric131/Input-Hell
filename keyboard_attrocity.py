## Generic keyboard spam (Copy to use as template for other presets if you want)

import time, random
from pynput.keyboard import Key, Controller

# List of keys to press
keys = [Key.space, Key.shift, "1", "2", "3", "4", "5", "6", "7", "8", "9"]
keys += list("abcdefghijklmnopqrstuvwxyz") # Add all letters
keyboard = Controller()

time.sleep(5) # 5 second warmup time
while True:
    for i in range(100): # Spam press 100 different keys
        key = random.choice(keys) # Pick a random key
        keyboard.press(key)
        time.sleep(0.05) # Wait 0.05 seconds (100 times is 5 seconds worth of spam)
        keyboard.release(key)
    time.sleep(10) # Time in seconds to wait after spam
    