from src import utils


def get_region(x1, y1, x2, y2):
    x1_ratio, y1_ratio = x1 / 1920, y1 / 1080
    x2_ratio, y2_ratio = x2 / 1920, y2 / 1080
    return get_region_based_on_resolution(x1_ratio, y1_ratio, x2_ratio, y2_ratio)


def get_last_slot_region():
    x1_ratio, y1_ratio = 1578 / 1920, 672 / 1080
    x1, y1, _, _ = get_region_based_on_resolution(x1_ratio, y1_ratio, 0, 0)
    return x1, y1


def get_region_based_on_resolution(x1_ratio, y1_ratio, x2_ratio, y2_ratio):
    screen_width, screen_height = utils.get_screen_size()
    x1 = int(screen_width * x1_ratio)
    y1 = int(screen_height * y1_ratio)
    x2 = int(screen_width * x2_ratio)
    y2 = int(screen_height * y2_ratio)
    return x1, y1, x2, y2
