import time
import threading
import keyboard
from src import movement

stop_flag = threading.Event()


def get_egg_count():
    try:
        count = int(input("Enter the number of eggs you want to collect: "))
        return count
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_egg_count()


def listen_for_delete():
    while not stop_flag.is_set():
        if keyboard.is_pressed('delete'):
            print("DELETE pressed. Stopping script.")
            stop_flag.set()
            break
        time.sleep(0.1)


def main():
    egg_count = get_egg_count()
    collected_eggs = 0
    print(f"Waiting...")

    delete_thread = threading.Thread(target=listen_for_delete, daemon=True)
    delete_thread.start()
    time.sleep(5)
    print(f"Starting ... Press DELETE to stop.")

    while True:
        if stop_flag.is_set():
            break
        if collected_eggs == egg_count:
            stop_flag.set()
            break
        # movement.move_right(0.5)
        # # movement.move_up(0.5)
        # if movement.look_for_pokemon_with_item('spearow'):
        #     stop_flag.set()
        #     break
        # movement.move_left(0.5)
        # # movement.move_down(0.5)
        # if movement.look_for_pokemon_with_item('spearow'):
        #     stop_flag.set()
        #     break
        # movement.slot_machine()
        # movement.poker_game()
        movement.create_egg()
        collected_eggs += 1
        print(f"Collected {collected_eggs} eggs.")

    delete_thread.join()
    movement.press_key('space', 0.1)


if __name__ == "__main__":
    main()
