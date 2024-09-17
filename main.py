import time
import threading
import keyboard
from src import movement, detection, regions

# Define constants
ELDER_IMAGE_PATH = 'images/elder_image.png'
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
    print(f"Starting ... Press DELETE to stop.")

    delete_thread = threading.Thread(target=listen_for_delete, daemon=True)
    delete_thread.start()
    time.sleep(15)

    while True:
        if stop_flag.is_set():
            break
        if collected_eggs == egg_count:
            stop_flag.set()
            break
        # movement.slot_machine()
        # movement.poker_game()
        movement.create_egg()
        region = regions.get_elder_region()
        if detection.is_elder_present(ELDER_IMAGE_PATH, region):
            print("The elder has appeared! Collecting the egg...")
            movement.collect_egg()
            collected_eggs += 1
        else:
            print("The elder is not here yet.")

        print(f"Collected {collected_eggs} eggs.")

    delete_thread.join()


if __name__ == "__main__":
    main()
