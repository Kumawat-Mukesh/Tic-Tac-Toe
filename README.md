# Tic Tac Toe - Python Console Game

A simple console-based Tic Tac Toe game implemented in Python. Two players can compete against each other by taking turns marking spaces on a 3x3 grid with their respective symbols (X or O). The objective is to form a row, column, or diagonal of their symbols to win the game. The game also detects a draw and allows players to play again if desired.

## Features

- Two-player mode
- 3x3 grid display
- Input validation for moves
- Detects winner or draw
- Option to play again after the game ends

## Getting Started

### Prerequisites

- Python 3.10 installed on your system

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kumawat-Mukesh/Tic-Tac-Toe
   ```
2. Navigate to the project directory:
  ```bash
   cd Tic-Tac-Toe
   ```
3. Run the game:
   ```bash
   python3 TicTacToe.py
   ```

## How to Play

1. The game will prompt the current player (Player X or Player O) to choose a position on the grid by entering a number between 1 and 9.

   - The grid positions are numbered as follows:
      ```bash 
       1 | 2 | 3
      ---|---|---
       4 | 5 | 6
      ---|---|---
       7 | 8 | 9
      ```

2. The player's symbol (X or O) will be placed in the chosen position if it's available.

3. The game will then check for a winner or a draw:
   - If a player wins, the game announces the winner and ends.
   - If the board is full with no winner, the game announces a draw and ends.

4. After the game ends, players are asked if they want to play again:


## Example

```bash 
Player X, choose a position (1-9): 5
 X |   |  
---|---|---
   | X |  
---|---|---
   |   |  

Player O, choose a position (1-9): 1
 O |   |  
---|---|---
   | X |  
---|---|---
   |   |  

...

Player X wins!

```
