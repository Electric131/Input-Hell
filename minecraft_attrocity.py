## WARNING: Can disable mouse if deactivated at the wrong time!

import os, time, random
from pynput.keyboard import Key, Controller

devices = ["Keyboard", "Mouse", "Mouse"]
keys = ["w", "a", "s", "d", Key.space, Key.shift, "f", "q", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
keyboard = Controller()

time.sleep(5) # 5 second warmup time
while True:
    device = random.choice(devices) # Pick either keyboard or mouse to spam
    if device == "Mouse":
        # Use pnputil (Windows only afaik) to disable mouse for 5 seconds
        os.system(f'pnputil /disable-device /class "{device}"')
        time.sleep(5)
        os.system(f'pnputil /enable-device /class "{device}"')
    else:
        for i in range(100): # Spam press 100 different keys
            key = random.choice(keys)
            keyboard.press(key)
            time.sleep(0.05)
            keyboard.release(key)
    time.sleep(10) # Time in seconds to wait after spam
