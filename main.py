import time
import threading
import keyboard
from src import movement

stop_flag = threading.Event()


def get_egg_count():
    while True:
        try:
            return int(input("Enter the number of eggs you want to collect: "))
        except ValueError:
            print("Invalid input. Please enter a number.")


def listen_for_delete():
    while not stop_flag.is_set():
        if keyboard.is_pressed('delete'):
            print("DELETE pressed. Stopping script.")
            stop_flag.set()
            break
        time.sleep(0.1)


def wait_for_game_focus(seconds=5):
    print(f"Waiting {seconds} seconds... bring the game window into focus.")
    time.sleep(seconds)
    print("Starting... Press DELETE to stop.")


def get_egg():
    egg_count = get_egg_count()
    collected_eggs = 0
    wait_for_game_focus()

    while not stop_flag.is_set():
        if collected_eggs == egg_count:
            stop_flag.set()
            break
        movement.create_egg()
        collected_eggs += 1
        print(f"Collected {collected_eggs} eggs.")


def get_item(pokemon='spearow'):
    wait_for_game_focus()

    while not stop_flag.is_set():
        movement.move_right(0.5)
        # movement.move_up(0.5)
        if movement.look_for_pokemon_with_item(pokemon):
            stop_flag.set()
            break
        movement.move_left(0.5)
        # movement.move_down(0.5)
        if movement.look_for_pokemon_with_item(pokemon):
            stop_flag.set()
            break


def slot_machine():
    wait_for_game_focus()

    while not stop_flag.is_set():
        movement.slot_machine()


def poker_game():
    wait_for_game_focus()

    while not stop_flag.is_set():
        movement.poker_game()


def main():
    delete_thread = threading.Thread(target=listen_for_delete, daemon=True)
    delete_thread.start()

    # Uncomment the flow you want to run:
    # get_egg()
    get_item('spearow')
    # slot_machine()
    # poker_game()

    stop_flag.set()
    delete_thread.join()
    movement.press_key('space', 0.1)


if __name__ == "__main__":
    main()
