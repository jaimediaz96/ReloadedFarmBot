from functools import lru_cache

from PIL import Image
from src import utils, regions
import pyautogui

ELDER_IMAGE_PATH = 'images/elder_image.png'


def capture_region(x1, y1, x2, y2):
    screen = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    return screen


@lru_cache(maxsize=None)
def load_template(image_path):
    image = Image.open(image_path).convert('L')
    return utils.normalize_brightness(image)


def compare_image(image_path, region, show_log=False):
    x1, y1, x2, y2 = region
    image = load_template(image_path)
    current_screen = capture_region(x1, y1, x2, y2).convert('L')
    current_screen = utils.normalize_brightness(current_screen)
    value = utils.calculate_difference_sum(image, current_screen)
    if show_log:
        print(f"diff = {value}")
    return value


def is_elder_present():
    region = regions.get_region(475, 410, 585, 600)
    return compare_image(ELDER_IMAGE_PATH, region) != 0
