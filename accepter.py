python
import pyautogui
import time
import win32api
from python_imagesearch.imagesearch import imagesearch

def get_screen_size():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screensize

def click_image(image_path, screen_width, screen_height):
    while True:
        pos = imagesearch(image_path)
        if pos[0] != -1:
            x, y = pyautogui.locateCenterOnScreen(image_path)
            win32api.SetCursorPos((x, y))
            pyautogui.leftClick()
            break

def main():
    while True:
        print("Choose resolution.")
        print("1.: Automatic")
        print("2.: 1280x1024")
        print("3.: Exit")
        x = int(input())
        if x > 3:
            print("This isn't a valid option.")
            time.sleep(3)
        elif x < 1:
            print("This isn't a valid option.")
            time.sleep(3)
        elif x == 1:
            screen_width, screen_height = get_screen_size()
            print(f"Detected screen resolution: {screen_width}x{screen_height}")
            click_image("accept19201080.png", screen_width, screen_height)
        elif x == 2:
            click_image("accept12801024.png", 1280, 1024)
        elif x == 3:
            exit()

if __name__ == "__main__":
    main()
