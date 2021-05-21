import pyautogui

# Faster: Moves mouse pointer by 200 pixels
# SLOWER: Moves mouse pointer by 20 pixels
FASTER=200
SLOWER=20


class gui_control:
    def __init__(self):
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        pyautogui.size()

    # Moves the Mouse and Clicks in appropriate text field.

    def conjunctiva(self):
        pyautogui.moveTo(100, 100, 2)

    def cornea(self,recognizer, src):
        pass

    def lens(self,recognizer, src):
        pass

    def iris(self,recognizer, src):
        pass
