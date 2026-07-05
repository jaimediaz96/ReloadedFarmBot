from PIL import Image
from src import utils, regions
import pyautogui

ELDER_IMAGE_PATH = 'images/elder_image.png'


def capture_region(x1, y1, x2, y2):
    screen = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    return screen


def compare_image(image_path, region, show_log=False):
    x1, y1, x2, y2 = region
    image = Image.open(image_path).convert('L')
    image = utils.normalize_brightness(image)
    current_screen = capture_region(x1, y1, x2, y2).convert('L')
    current_screen = utils.normalize_brightness(current_screen)
    value = utils.calculate_difference_sum(image, current_screen)
    if show_log:
        print(f"diff = {value}")
    return value


def is_elder_present():
    region = regions.get_region(475, 410, 585, 600)
    diff = compare_image(ELDER_IMAGE_PATH, region)
    if diff != 0:
        return True
    return False
