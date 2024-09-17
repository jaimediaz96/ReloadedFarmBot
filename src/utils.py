import pyautogui
import cv2
import numpy as np
from PIL import ImageDraw, Image
from src import detection


def get_screen_size():
    return pyautogui.size()


def draw_rectangle(image, region):
    draw = ImageDraw.Draw(image)
    x1, y1, x2, y2 = region
    draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
    return image


def show_image_with_rectangle(x1, y1, x2, y2):
    image = detection.capture_region(x1, y1, x2, y2)
    open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imshow("Captured Region with Rectangle", open_cv_image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()


def normalize_brightness(image):
    np_image = np.array(image, dtype=np.float32)
    mean_brightness = np.mean(np_image)
    normalized_image = np_image - mean_brightness
    normalized_image = np.clip(normalized_image, 0, 255).astype(np.uint8)
    return Image.fromarray(normalized_image)


def calculate_difference_sum(image1, image2):
    np_image1 = np.array(image1)
    np_image2 = np.array(image2)
    difference = np.abs(np_image1 - np_image2)
    return np.sum(difference)
