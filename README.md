# World Simulation

## Object-Oriented Programming Project in Python
This project is a grid-based ecological simulation where different species of animals and plants interact, reproduce, and compete for survival. This project utilizes **Tkinter** for the graphical interface.

---

### Key Features
* **Engine**: Written in Python using Object-Oriented Programming principles.
* **GUI**: Built with the `tkinter` library for grid visualization and user interaction.
* **Dynamic Logs**: A real-time text area reports events like births, combat, and plant spreading.
* **Persistence**: Full support for saving the current world state to a `save.txt` file and loading it back later via CSV-style formatting.
* **Manual Interaction**: Users can manually add organisms to the map by clicking on empty grid squares and selecting from a dropdown menu.

---

### Organisms

#### Plants
Plants have a chance to spread to adjacent tiles during their turn.

| Plant | Strength | ID | Special Behavior |
| :--- | :---: | :---: | :--- |
| **Grass (Trawa)** | 0 | **T** | Standard plant. |
| **Sow Thistle (Mlecz)** | 0 | **M** | Makes three attempts to spread in one turn. |
| **Guarana** | 0 | **G** | Increases the strength of the animal that eats it by 3. |
| **Belladonna (Jagody)** | 99 | **J** | Kills the animal that eats it. |
| **Sosnowsky's Hogweed (Barszcz)** | 10 | **B** | Kills all animals in its vicinity during its turn. |

#### Animals
Animals move once per turn and reproduce if they collide with a member of the same species.

| Animal | Strength | Initiative | ID | Special Behavior |
| :--- | :---: | :---: | :---: | :--- |
| **Wolf (Wilk)** | 9 | 5 | **W** | High strength predator. |
| **Sheep (Owca)** | 4 | 4 | **O** | Standard herbivore. |
| **Fox (Lis)** | 3 | 7 | **L** | Won't move into a field occupied by a stronger organism. |
| **Turtle (Zolw)** | 2 | 1 | **Z** | 75% chance to stay in place; reflects attacks from organisms with strength < 5. |
| **Antelope (Antylopa)** | 4 | 4 | **A** | Moves 2 fields at once; 50% chance to escape from a fight. |
| **CyberSheep (CyberOwca)** | 11 | 4 | **K** | Specialized organism designed to hunt Sosnowsky's Hogweed. |

---

### Human Controls & Special Ability
The player controls the **Human (C)** using the keyboard.

* **Movement**: Use the **Arrow Keys** (Up, Down, Left, Right) to move the character around the grid.
* **Special Ability**: Activated by pressing the **'1'** key.
* **Ability Logic**: Once activated, the Human gains a temporary status effect tracked by `licznik` and `cooldown` variables. 

---
<img width="570" height="858" alt="image" src="https://github.com/user-attachments/assets/1e9ae4fe-6d26-4607-9a47-0939aedfadc4" />


### How to Use

#### 1. Running the Simulation
When the script starts, you will be prompted in the console to enter the map dimensions:
```bash
Podaj szerokosc mapy: 15
Podaj wysokosc mapy: 15
```

#### 2. Interaction
* **Next Turn**: Click the "Wykonaj Ture" button or press an arrow key to progress the simulation.
* **Add Organism**: Click on any empty square in the grid to open a menu and manually place a new organism.
* **Save/Load**: Use the "Zapisz" and "Wczytaj" buttons to save the current grid to `save.txt` or load a previous session.

#### 3. Legend (Colors)
The grid uses specific hex codes to identify organisms:

* **Antelope (A)**: `#A88319`
* **Sheep (O)**: `#EDC3C7`
* **Wolf (W)**: `#75736E`
* **Fox (L)**: `#D98A02`
* **Turtle (Z)**: `#BDA573`
* **Grass (T)**: `#07F20B`
* **Sow Thistle (M)**: `#E1E81A`
* **Belladonna (J)**: `#0B083D`
* **Guarana (G)**: `#DB6556`
* **Sosnowsky's Hogweed (B)**: `#B0DEA2`
* **CyberSheep (K)**: `#00CCFF`
* **Human (C)**: `#F2E5CB`
