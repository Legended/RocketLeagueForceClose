from os import popen, chdir, system
from win32gui import GetWindowText, GetForegroundWindow
from pynput import keyboard

def detect():
    while True:
        if 'RocketLeague.exe' in popen('tasklist').read():
            run_script()
            break

def run_script():
    combo = {keyboard.Key.alt_l, keyboard.Key.f4}
    current = set()

    def on_press(key):
        if key in combo:
            current.add(key)
            if all(k in current for k in combo):
                if 'Rocket League' in GetWindowText(GetForegroundWindow()):
                    system("taskkill /IM RocketLeague.exe /F")
                    listener.stop()

    def on_release(key):
        try:
            current.remove(key)
        except KeyError:
            pass

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    try:
        popen('RocketLeague.exe')
    except FileNotFoundError as e:
        print(e)
    chdir('C:/Windows/System32')
    detect()
