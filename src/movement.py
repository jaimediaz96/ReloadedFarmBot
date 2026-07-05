import pyautogui
import time
from src import regions, detection

BATTLE_IMAGE_PATH = 'images/battle.png'
ITEM_IMAGE_PATH = 'images/item.png'
POKEMON_CAPTURE_PATH = 'images/pokemon_capture.png'
POKEMON_NO_CAPTURE_PATH = 'images/pokemon_no_capture.png'

# Each Pokémon maps to one or more matchers: (image_path, region coords, expected diff values).
# A Pokémon is detected if ANY of its matchers returns a diff value in the expected set.
# The expected values are calibrated for 1920x1080 — do not change them without recalibrating.
POKEMON_MATCHERS = {
    "milcery": [('images/milcery.png', (1097, 33, 1213, 68), {0})],          # Sweet Items: Strawberry, Berry, Love,
                                                                              # Star, Clover, Flower, Ribbon Sweet
    "pancham": [('images/pancham.png', (1100, 36, 1220, 67), {0})],          # Mars stone
    "solrock": [('images/solrock.png', (1100, 35, 1205, 67), {0})],          # Sun stone
    "lunatone": [('images/lunatone.png', (1100, 35, 1227, 68), {0})],        # Moon stone
    "snubbull": [('images/snubbull.png', (1100, 35, 1227, 68), {0})],        # Nymph stone
    "gligar": [('images/gligar.png', (1104, 38, 1187, 65), {0})],            # Desert stone - can fail in the desert
    "skorupi": [('images/skorupi.png', (1101, 45, 1208, 65), {0})],          # Venus stone - can fail in the desert
    "ralts": [('images/ralts.png', (1100, 36, 1170, 65), {0})],              # Dawn stone
    "mawile": [('images/mawile.png', (1100, 36, 1199, 66), {0})],            # Metal stone
    "nosepass": [('images/nosepass.png', (1100, 36, 1227, 66), {0})],        # Mineral stone
    "chansey": [('images/chansey.png', (1100, 36, 1217, 66), {0})],          # Oval stone
    "swellow": [('images/swellow.png', (1100, 36, 1219, 67), {0})],          # Celestial stone
    "vigoroth": [('images/vigoroth.png', (1100, 36, 1222, 67), {0})],        # Common board
    "rapidash": [('images/rapidash.png', (1100, 36, 1225, 67), {0})],        # Fire board
    "pachirisu": [('images/pachirisu.png', (1100, 36, 1230, 67), {0})],      # Thunder board
    "onix": [('images/onix.png', (1100, 36, 1170, 67), {0})],                # Stone board
    "toxicroak": [('images/toxicroak.png', (1100, 36, 1230, 67), {0})],      # Strong board
    "kricketune": [('images/kricketune.png', (1100, 36, 1245, 67), {0})],    # Bug board
    "abomasnow": [('images/abomasnow.png', (1100, 36, 1265, 67), {0})],      # Ice board
    "murkrow": [('images/murkrow.png', (1100, 36, 1225, 67), {0})],          # Dark board
    "bagon": [('images/bagon.png', (1100, 36, 1190, 67), {0})],              # Draco board
    "marill": [('images/marill.png', (1100, 36, 1190, 67), {0})],            # Goblin board
    "rolycoly": [('images/rolycoly.png', (1100, 36, 1225, 67), {0})],        # Black mineral
    "poliwhirl": [('images/poliwhirl.png', (1100, 36, 1235, 67), {0})],      # King stone
    "spearow": [('images/spearow.png', (1100, 36, 1215, 67), {12791}),       # Beautiful feather
                ('images/fearow.png', (1100, 36, 1200, 67), {10898})],
    "magmar": [('images/magmar.png', (1100, 36, 1205, 67), {0})],            # Amp magmar
    "pawniard": [('images/pawniard.png', (1100, 36, 1230, 67), {0})],        # extrange disc
}


def hold_key(key, duration):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)


def move_up(duration):
    hold_key('up', duration)


def move_down(duration):
    hold_key('down', duration)


def move_left(duration):
    hold_key('left', duration)


def move_right(duration):
    hold_key('right', duration)


def press_key(key, wait):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    time.sleep(wait)


def press_key_multi(times, key, wait):
    for _ in range(times):
        press_key(key, wait)


def extreme_vel():
    press_key('8', 0.1)
    press_key('z', 0.3)


def right_click_at_position(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(button='right')


def create_egg():
    extreme_vel()
    move_up(0.2)
    for _ in range(28):
        move_left(1)
        move_right(1)
    move_right(0.2)
    press_key('b', 0)
    move_left(0.38)
    move_down(0.5)
    move_up(0.8)
    press_key('up', 1)
    collect_egg()


def collect_egg():
    move_left(0.51)
    extreme_vel()
    move_down(0.2)
    press_key_multi(7, 'z', 0.8)
    time.sleep(1)
    move_up(0.3)
    move_right(0.3)
    press_key('b', 0.1)
    move_left(0.38)
    move_down(0.5)
    move_right(0.8)
    move_up(0.2)
    press_key_multi(4, 'z', 0.5)
    press_key_multi(3, 'up', 0.2)
    x, y = regions.get_last_slot_region()
    right_click_at_position(x, y)
    time.sleep(0.2)
    press_key_multi(2, 'down', 0.3)
    press_key_multi(2, 'z', 0.5)
    press_key_multi(2, 'x', 0.5)
    time.sleep(0.2)
    move_left(0.7)
    press_key('up', 1)


def slot_machine():
    press_key('space', 1.2)
    press_key('z', 0.1)
    press_key('x', 0.1)
    press_key('c', 1)


def poker_game():
    press_key_multi(3, 'z', 0.5)
    press_key_multi(2, 'left', 0.3)
    press_key('down', 0.3)
    press_key('z', 3.5)
    press_key('z', 0.5)
    press_key_multi(2, 'left', 0.3)
    press_key('down', 0.3)
    press_key('z', 3)
    press_key('z', 0.5)
    press_key_multi(3, 'up', 0.3)
    press_key_multi(2, 'left', 0.3)
    press_key('up', 0.3)
    press_key('z', 4.5)
    press_key('z', 3)


def look_for_pokemon_with_item(pokemon):
    if not in_battle():
        return False

    if not_capture():
        return waiting()

    if not look_for_pokemon(pokemon):
        return escape()

    if have_item():
        return waiting()

    if is_capture():
        return escape()

    return waiting()


def in_battle():
    battle_region = regions.get_region(786, 38, 797, 52)
    return detection.compare_image(BATTLE_IMAGE_PATH, battle_region) == 5149


def have_item():
    item_region = regions.get_region(1053, 32, 1091, 68)
    value = detection.compare_image(ITEM_IMAGE_PATH, item_region)
    print(f"have_item = {value}")
    return value != 30701


def not_capture():
    pokemon_no_capture_region = regions.get_region(1518, 30, 1617, 91)
    value = detection.compare_image(POKEMON_NO_CAPTURE_PATH, pokemon_no_capture_region)
    print(f"pokemon_no_capture_region = {value}")
    return value not in {1058667, 1004869, 901868, 757903, 676796, 674281, 762852, 713175, 725372, 888754, 800270}


def is_capture():
    pokemon_capture_region = regions.get_region(1535, 28, 1595, 89)
    value = detection.compare_image(POKEMON_CAPTURE_PATH, pokemon_capture_region)
    print(f"is_capture = {value}")
    return value == 490131


def escape():
    press_key('e', 0.1)
    press_key_multi(2, 'z', 0.1)
    return False


def waiting():
    return True


def look_for_pokemon(pokemon):
    matchers = POKEMON_MATCHERS.get(pokemon)
    if matchers is None:
        print(f"Unknown Pokemon '{pokemon}', treating as no match.")
        return False

    for image_path, coords, expected_values in matchers:
        region = regions.get_region(*coords)
        value = detection.compare_image(image_path, region)
        if expected_values != {0}:
            print(f"{image_path} = {value}")
        if value in expected_values:
            return True
    return False
