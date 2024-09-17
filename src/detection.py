from PIL import Image
from src import utils
import pyautogui


def capture_region(x1, y1, x2, y2):
    screen = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    return screen


def is_elder_present(elder_image_path, region):
    x1, y1, x2, y2 = region
    elder_image = Image.open(elder_image_path).convert('L')
    elder_image = utils.normalize_brightness(elder_image)
    current_screen = capture_region(x1, y1, x2, y2).convert('L')
    current_screen = utils.normalize_brightness(current_screen)
    diff = utils.calculate_difference_sum(elder_image, current_screen)
    if diff == 0:
        return True
    if diff == 3912725:
        return True
    if 3306633 <= diff <= 4200168:
        return True
    return False
