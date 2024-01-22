import keyboard
from PIL import ImageGrab
import pyautogui
import time
import random

def transform():
    if get_pixel():
        pyautogui.click()
        time.sleep(random.uniform(0.02, 0.05))

def get_pixel():
    x_coordinate = 375
    y_coordinate = 460
    unfiltered_color = (3, 29, 3)

    screenshot = ImageGrab.grab()

    pixel_color = screenshot.getpixel((x_coordinate, y_coordinate))

    return pixel_color == unfiltered_color

if __name__ == '__main__':
    keyboard.add_hotkey('shift', transform)
    keyboard.wait('esc')