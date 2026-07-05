# ReloadedFarmBot

## Description

**ReloadedFarmBot** is designed to automate repetitive tasks in **Pokémon Reloaded**, beginning with the collection of Pokémon eggs at the daycare. It also supports farming rare items from wild Pokémon (via image recognition) and automating the Game Corner minigames (slot machine and poker).

This project is **not** meant to play the game for you, but rather to improve farming efficiency for items and Pokémon that are difficult to obtain while keeping the core gameplay experience intact.

## Features

The bot has four flows, defined as functions in `main.py`. Choose which one to run by uncommenting it inside `main()`:

```python
# Uncomment the flow you want to run:
get_egg()
# get_item('spearow')
# slot_machine()
# poker_game()
```

- **`get_egg()` — Automatic Egg Collection:** Moves back and forth in the Pokémon daycare, collects eggs, and stores them in the PC. You define how many eggs to collect before starting.
- **`get_item('<pokemon>')` — Rare Item Farming:** Walks left and right in tall grass to trigger wild encounters. Uses image recognition to detect when a battle starts, identify the wild Pokémon by name, and check whether it is holding an item. If the target Pokémon appears with an item, the bot stops, so you can catch it; otherwise it escapes and keeps searching. Supported targets are listed in `POKEMON_MATCHERS` in `src/movement.py` (e.g. `milcery`, `pancham`, `ralts`, `chansey`, `spearow`, ...).
- **`slot_machine()` — Slot Machine Automation:** Repeatedly plays the Game Corner slot machine.
- **`poker_game()` — Poker Automation:** Repeatedly plays the Game Corner poker minigame.
- **Manual Interruption:** Any flow can be stopped at any time by pressing the `Delete` (`Supr`) key.

# Initial Conditions

## Egg collection (`get_egg`)

1. Complete the Star League at least once.
2. Have two compatible Pokémon for breeding at the daycare.
3. Have a Pokémon that knows the Extreme Speed ability in your party.
4. Set Extreme Speed as the ability in the ability menu (when you press 8).
5. Ensure you have a free space in your party, specifically in slot 6.
6. Start from the position just outside the daycare, where you would normally stand after collecting an egg.
7. Make sure there are empty boxes available in your PC for storing new Pokémon eggs.

Example images for conditions 4, 5, and 6 are provided in the `examples` folder.

## Item farming (`get_item`)

1. Stand in tall grass where the target Pokémon appears, with room to move left and right.
2. The `e` key must be bound to the escape action in battle.
3. Detection is calibrated for a 1920x1080 resolution; the template images in `images/` must match your game's rendering.

## Minigames (`slot_machine` / `poker_game`)

1. Start the flow with the minigame already open and ready to play.

**Note:** The script performs mouse and keyboard actions. Do not use the mouse or keyboard while the script is running, as it may cause interruptions. To stop the script, press the Delete key, and it will finish the current cycle before stopping.

# Known Issues

- Receiving a phone call in the game can interfere with the script's performance.
- The script is calibrated for a 1920x1080 resolution and has not been tested on other screen sizes or systems. Therefore, it may not function correctly on other configurations.
- Image detection compares exact difference values calibrated for specific screen regions; changes in game brightness or UI can break detection.

## Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
```

(OpenCV is only needed for the debug helper `utils.show_image_with_rectangle`; the bot runs without it.)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ReloadedFarmBot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ReloadedFarmBot
   ```

3. In `main.py`, uncomment the flow you want to run inside `main()` (by default `get_egg()` is active).

4. Run the main script:

   ```bash
   python main.py
   ```

5. For egg collection, enter the number of eggs you wish to collect when prompted.

6. You then have 5 seconds to bring the game window into focus before the flow starts.

7. Enjoy the automation as the script handles the repetitive work. Press `Delete` to stop at any time.

## Customization

### Coordinate Adjustments

The script includes default coordinate values for the screen regions used by image detection (battle indicator, Pokémon name, held item). All coordinates are expressed for 1920x1080 and scaled to your resolution via `src/regions.py`. You may need to adjust them for other setups; `utils.show_image_with_rectangle` helps visualize a capture region while calibrating.

### Adding a new target Pokémon

Add a template image to `images/` and a new entry to `POKEMON_MATCHERS` in `src/movement.py` with the image path, the screen region of the name, and the expected difference value(s) returned by `detection.compare_image`.

### Future Expansions

- **Shiny Egg Detection and Collection**
- **Movement Optimization to Minimize Farming Time**

## Contributions

Contributions are welcome! If you have ideas to improve the script or add new features, feel free to open a pull request or report an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
