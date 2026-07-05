import pyautogui
import time
from src import regions, detection

BATTLE_IMAGE_PATH = 'images/battle.png'
ITEM_IMAGE_PATH = 'images/item.png'
POKEMON_CAPTURE_PATH = 'images/pokemon_capture.png'
POKEMON_NO_CAPTURE_PATH = 'images/pokemon_no_capture.png'
MILCERY = 'images/milcery.png'
PANCHAM = 'images/pancham.png'
SOLROCK = 'images/solrock.png'
LUNATONE = 'images/lunatone.png'
SNUBBULL = 'images/snubbull.png'
GLIGAR = 'images/gligar.png'
SKORUPI = 'images/skorupi.png'
RALTS = 'images/ralts.png'
MAWILE = 'images/mawile.png'
NOSEPASS = 'images/nosepass.png'
CHANSEY = 'images/chansey.png'
SWELLOW = 'images/swellow.png'
VIGOROTH = 'images/vigoroth.png'
RAPIDASH = 'images/rapidash.png'
PACHIRISU = 'images/pachirisu.png'
ONIX = 'images/onix.png'
TOXICROAK = 'images/toxicroak.png'
KRICKETUNE = 'images/kricketune.png'
ABOMASNOW = 'images/abomasnow.png'
MURKROW = 'images/murkrow.png'
BAGON = 'images/bagon.png'
MARILL = 'images/marill.png'
ROLYCOLY = 'images/rolycoly.png'
POLIWHIRL = 'images/poliwhirl.png'
SPEAROW = 'images/spearow.png'
FEAROW = 'images/fearow.png'
MAGMAR = 'images/magmar.png'
PAWNIARD = 'images/pawniard.png'


def move_up(duration):
    pyautogui.keyDown('up')
    time.sleep(duration)
    pyautogui.keyUp('up')


def move_down(duration):
    pyautogui.keyDown('down')
    time.sleep(duration)
    pyautogui.keyUp('down')


def move_left(duration):
    pyautogui.keyDown('left')
    time.sleep(duration)
    pyautogui.keyUp('left')


def move_right(duration):
    pyautogui.keyDown('right')
    time.sleep(duration)
    pyautogui.keyUp('right')


def press_key(key, wait):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    time.sleep(wait)


def press_key_multi(times, key, wait):
    for i in range(times):
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
    for i in range(28):
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
    return value != 1058667 and value != 757903 and value != 676796 and value != 762852 and value != 713175 and value != 725372


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
    pokemons = {
        "milcery": milcery(),        # Sweet Items: Strawberry Sweet - Berry Sweet - Love Sweet - Star Sweet  - Clover
                                     # Sweet - Flower Sweet - Ribbon Sweet
        "pancham": pancham(),        # Mars stone
        "solrock": solrock(),        # Sun stone
        "lunatone": lunatone(),      # Moon stone
        "snubbull": snubbull(),      # Nymph stone
        "gligar": gligar(),          # Desert stone - Because of the desert can fail
        "skorupi": skorupi(),        # Venus stone - Because of the desert can fail
        "ralts": ralts(),            # Dawn stone
        "mawile": mawile(),          # Metal stone
        "nosepass": nosepass(),      # Mineral stone
        "chansey": chansey(),        # Oval stone
        "swellow": swellow(),        # Celestial stone
        "vigoroth": vigoroth(),      # Common board
        "rapidash": rapidash(),      # Fire board
        "pachirisu": pachirisu(),    # Thunder board
        "onix": onix(),              # Stone board
        "toxicroak": toxicroak(),    # Strong board
        "kricketune": kricketune(),  # Bug board
        "abomasnow": abomasnow(),    # Ice board
        "murkrow": murkrow(),        # Dark board
        "bagon": bagon(),            # Draco board
        "marill": marill(),          # Goblin board
        "rolycoly": rolycoly(),      # Black mineral
        "poliwhirl": poliwhirl(),    # King stone
        "spearow": spearow(),        # Beautiful feather
        "magmar": magmar(),          # Amp magmar
        "pawniard": pawniard(),      # extrange disc
        "": False
    }
    return pokemons.get(pokemon, lambda: True)


def milcery():
    milcery_region = regions.get_region(1097, 33, 1213, 68)
    return detection.compare_image(MILCERY, milcery_region) == 0


def pancham():
    pancham_region = regions.get_region(1100, 36, 1220, 67)
    return detection.compare_image(PANCHAM, pancham_region) == 0


def solrock():
    solrock_region = regions.get_region(1100, 35, 1205, 67)
    return detection.compare_image(SOLROCK, solrock_region) == 0


def lunatone():
    lunatone_region = regions.get_region(1100, 35, 1227, 68)
    return detection.compare_image(LUNATONE, lunatone_region) == 0


def snubbull():
    snubbull_region = regions.get_region(1100, 35, 1227, 68)
    return detection.compare_image(SNUBBULL, snubbull_region) == 0


def gligar():
    gligar_region = regions.get_region(1104, 38, 1187, 65)
    return detection.compare_image(GLIGAR, gligar_region) == 0


def skorupi():
    skorupi_region = regions.get_region(1101, 45, 1208, 65)
    return detection.compare_image(SKORUPI, skorupi_region) == 0


def ralts():
    ralts_region = regions.get_region(1100, 36, 1170, 65)
    return detection.compare_image(RALTS, ralts_region) == 0


def mawile():
    mawile_region = regions.get_region(1100, 36, 1199, 66)
    return detection.compare_image(MAWILE, mawile_region) == 0


def nosepass():
    nosepass_region = regions.get_region(1100, 36, 1227, 66)
    return detection.compare_image(NOSEPASS, nosepass_region) == 0


def chansey():
    chansey_region = regions.get_region(1100, 36, 1217, 66)
    return detection.compare_image(CHANSEY, chansey_region) == 0


def swellow():
    swellow_region = regions.get_region(1100, 36, 1219, 67)
    return detection.compare_image(SWELLOW, swellow_region) == 0


def vigoroth():
    vigoroth_region = regions.get_region(1100, 36, 1222, 67)
    return detection.compare_image(VIGOROTH, vigoroth_region) == 0


def rapidash():
    rapidash_region = regions.get_region(1100, 36, 1225, 67)
    return detection.compare_image(RAPIDASH, rapidash_region) == 0


def pachirisu():
    pachirisu_region = regions.get_region(1100, 36, 1230, 67)
    return detection.compare_image(PACHIRISU, pachirisu_region) == 0


def onix():
    onix_region = regions.get_region(1100, 36, 1170, 67)
    return detection.compare_image(ONIX, onix_region) == 0


def toxicroak():
    toxicroak_region = regions.get_region(1100, 36, 1230, 67)
    return detection.compare_image(TOXICROAK, toxicroak_region) == 0


def kricketune():
    kricketune_region = regions.get_region(1100, 36, 1245, 67)
    return detection.compare_image(KRICKETUNE, kricketune_region) == 0


def abomasnow():
    abomasnow_region = regions.get_region(1100, 36, 1265, 67)
    return detection.compare_image(ABOMASNOW, abomasnow_region) == 0


def murkrow():
    murkrow_region = regions.get_region(1100, 36, 1225, 67)
    return detection.compare_image(MURKROW, murkrow_region) == 0


def bagon():
    bagon_region = regions.get_region(1100, 36, 1190, 67)
    return detection.compare_image(BAGON, bagon_region) == 0


def marill():
    marill_region = regions.get_region(1100, 36, 1190, 67)
    return detection.compare_image(MARILL, marill_region) == 0


def rolycoly():
    rolycoly_region = regions.get_region(1100, 36, 1225, 67)
    return detection.compare_image(ROLYCOLY, rolycoly_region) == 0


def poliwhirl():
    poliwhirl_region = regions.get_region(1100, 36, 1235, 67)
    return detection.compare_image(POLIWHIRL, poliwhirl_region) == 0


def spearow():
    spearow_region = regions.get_region(1100, 36, 1215, 67)
    fearow_region = regions.get_region(1100, 36, 1200, 67)
    value_spearow = detection.compare_image(SPEAROW, spearow_region)
    value_fearow = detection.compare_image(FEAROW, fearow_region)
    print(f"spearow = {value_spearow} fearow {value_fearow}")
    return value_spearow == 12791 or value_fearow == 10898


def magmar():
    magmar_region = regions.get_region(1100, 36, 1205, 67)
    return detection.compare_image(MAGMAR, magmar_region) == 0


def pawniard():
    pawniard_region = regions.get_region(1100, 36, 1230, 67)
    return detection.compare_image(PAWNIARD, pawniard_region) == 0
