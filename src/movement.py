import pyautogui
import time
from src import regions


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
    for i in range(30):
        move_left(1)
        move_right(1)
    move_right(0.2)
    extreme_vel()
    move_left(0.38)
    move_down(0.5)
    move_up(0.5)
    time.sleep(2)


def collect_egg():
    move_left(0.51)
    extreme_vel()
    move_down(0.1)
    press_key_multi(7, 'z', 0.8)
    time.sleep(1.5)
    move_up(0.2)
    move_right(0.3)
    extreme_vel()
    move_left(0.38)
    move_down(0.5)
    move_right(0.7)
    move_up(0.2)
    press_key_multi(4, 'z', 0.5)
    press_key_multi(3, 'up', 0.2)
    x, y = regions.get_last_slot_region()
    right_click_at_position(x, y)
    press_key_multi(2, 'down', 0.3)
    press_key_multi(2, 'z', 0.3)
    press_key_multi(2, 'x', 0.5)
    move_left(0.68)
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
