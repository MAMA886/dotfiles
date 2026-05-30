import time, sys
import win32gui, win32con, win32clipboard, pyautogui

time.sleep(6)

hwnd = None
def callback(h, _):
    global hwnd
    if 'Visual Studio Code' in win32gui.GetWindowText(h):
        hwnd = h
win32gui.EnumWindows(callback, None)
if not hwnd:
    sys.exit(0)

# Bring VS Code to front
win32gui.SetForegroundWindow(hwnd)
time.sleep(2)

# Click sidebar input area
# VS Code window: sidebar right ~35%, input near bottom
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
w = right - left
h = bottom - top
# Input is in sidebar ~75% from left, ~97% from top
click_x = left + int(w * 0.75)
click_y = top + int(h * 0.97)
pyautogui.click(click_x, click_y)
time.sleep(0.5)

# Copy "what model" to clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText('what model')
win32clipboard.CloseClipboard()
time.sleep(0.3)

# Paste and send in old conversation
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.3)
pyautogui.press('enter')
