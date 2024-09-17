# ReloadedFarmBot

## Description

**ReloadedFarmBot** is designed to automate repetitive tasks in **Pokémon Reloaded**, beginning with the collection of Pokémon eggs at the daycare. The initial focus is on automating egg farming, allowing players to efficiently farm eggs. Future updates will expand automation to include farming for rare items and shiny eggs.

This project is **not** meant to play the game for you, but rather to improve farming efficiency for items and Pokémon that are difficult to obtain while keeping the core gameplay experience intact.

## Features

- **Automatic Egg Collection:** The script moves back and forth in the Pokémon daycare, collects eggs, and compares them to determine if they are new or duplicates. New eggs are automatically saved, while duplicates are discarded.
- **Manual Interruption:** The script can be stopped at any time by pressing the `Supr` key.
- **Customizable Egg Count:** Players can define how many eggs they want to collect before starting the script.

# Initial Conditions

To ensure the script works properly, make sure the following conditions are met before running:

1. Complete the Star League at least once.
2. Have two compatible Pokémon for breeding at the daycare.
3. Have a Pokémon that knows the Extreme Speed ability in your party.
4. Set Extreme Speed as the ability in the ability menu (when you press 8).
5. Ensure you have a free space in your party, specifically in slot 6.
6. Start from the position just outside the daycare, where you would normally stand after collecting an egg.
7. Make sure there are empty boxes available in your PC for storing new Pokémon eggs.

Example images for conditions 4, 5, and 6 are provided in the `examples` folder.

**Note:** The script will perform mouse and keyboard actions. Do not use the mouse or keyboard while the script is running, as it may cause interruptions. To stop the script, press the Delete key, and it will finish the current cycle before stopping.

# Known Issues

- Receiving a phone call in the game can interfere with the script's performance.
- The script is calibrated for a 1920x1080 resolution and has not been tested on other screen sizes or systems. Therefore, it may not function correctly on other configurations.

## Requirements

Ensure you have the following libraries installed:

```bash
pip install pyautogui pillow imageio keyboard
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ReloadedFarmBot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ReloadedFarmBot
   ```

3. Run the main script:

   ```bash
   python main.py
   ```

4. Enter the number of eggs you wish to collect when prompted by the script.

5. Once the egg count is set, you have 15 seconds to bring the game window into focus.

6. Enjoy the automation as the script handles the repetitive work.

## Customization

### Coordinate Adjustments

The script includes default coordinate values for the screen region where eggs appear. You may need to adjust these according to your screen resolution and the egg's position in the game.

### Future Expansions

This project is designed to be modular, with future updates planned to include:

- **Rare Item Farming Automation**
- **Shiny Egg Detection and Collection**
- **Movement Optimization to Minimize Farming Time**

## Contributions

Contributions are welcome! If you have ideas to improve the script or add new features, feel free to open a pull request or report an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
