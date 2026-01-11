# Connect 4 in Python

---

## Project Overview

This project is a **Python implementation of the classic Connect 4 game**, enhanced with two unique gameplay features that add strategic depth:

1. **Remove a Row** – Players can remove all counters from a selected row, potentially clearing space or disrupting an opponent’s strategy.
2. **Remove a Counter** – Players can remove a single counter from the board, allowing them to block a winning move or create new opportunities.

These mechanics introduce an additional layer of **strategy and unpredictability**, encouraging players to adapt dynamically during play. To maintain balance and fairness, these special abilities are restricted (for example, they may only be remembered once per game or under specific conditions).

---

## Programming Paradigm

This project is implemented using a **procedural programming paradigm**:

- The game logic is organised into **functions** rather than classes.
- Game state (such as the board and player turns) is managed using **data structures** like lists and variables.
- Control flow is driven by function calls, loops, and conditional statements.
- This approach emphasizes **step-by-step execution** and clear logical flow rather than object abstraction.

The procedural style provides a straightforward and readable structure, making the game logic easy to follow and modify.

---

## Features

- Standard Connect 4 gameplay
- Turn-based play between two players
- Board represented using Python lists
- Special abilities:
  - Remove an entire row
  - Remove a single counter
- Board state printed to the console after each move
- Win detection for horizontal, vertical, and diagonal connections

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/JerryA01/connect4-python.git
cd connect4-python
