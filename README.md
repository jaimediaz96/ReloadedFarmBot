# ReloadedFarmBot

## Description

**ReloadedFarmBot** is designed to automate repetitive tasks in Pokémon Reloaded, beginning with the collection of Pokémon eggs at the daycare. The initial focus is on automating egg farming, allowing players to efficiently farm eggs. Future updates will expand automation to include farming for rare items and shiny eggs.

This project is not intended to automatically complete the game, but rather to improve the efficiency of obtaining difficult-to-acquire items, maintaining the integrity of the core gameplay experience.

## Features

- **Automatic Egg Collection:** The script moves back and forth in the Pokémon daycare, collects eggs, and compares them to determine if they are new or duplicates. New eggs are automatically saved, while duplicates are discarded.
- **Manual Interruption:** The script can be stopped at any time by pressing the `Escape` key.
- **Customizable Egg Count:** Players can define how many eggs they want to collect before starting the script.

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

5. Enjoy the automation as the script handles the repetitive work.

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
