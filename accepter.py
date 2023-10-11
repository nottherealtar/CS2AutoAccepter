import ctypes
import pyautogui
import time
import win32api
from python_imagesearch.imagesearch import imagesearch

def get_screen_size():
    """
    Get the screen size of the user's display.
    """
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screensize

def click_image(image_path):
    """
    Search for an image on the screen and click it once found.
    """
    while True:
        pos = imagesearch(image_path)
        if pos[0] != -1:
            win32api.SetCursorPos((pos[0], pos[1]))
            pyautogui.leftClick()
            break

def main():
    """
    Main function to execute the script.
    """
    while True:
        print("Choose resolution.")
        print("1.: Automatic")
        print("2.: 1280x1024")
        print("3.: Exit")
        try:
            x = int(input())
            if x == 1:
                screen_width, screen_height = get_screen_size()
                print(f"Detected screen resolution: {screen_width}x{screen_height}")
                click_image("accept19201080.png")
            elif x == 2:
                click_image("accept12801024.png")
            elif x == 3:
                exit()
            else:
                print("This isn't a valid option.")
                time.sleep(3)
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(3)

if __name__ == "__main__":
    main()
