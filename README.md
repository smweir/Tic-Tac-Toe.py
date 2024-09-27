This Python program implements a simple Tic-Tac-Toe game using tkinter. The game allows two players to alternate turns, placing either "X" or "O" on the grid until one player wins or the game results in a tie.

Features:
Two-Player Gameplay: Players take turns clicking on buttons to mark "X" or "O" on the 3x3 grid.
Win Detection: Automatically checks for winning combinations (rows, columns, diagonals) for both "X" and "O".
Tie Condition: Detects when all buttons are clicked without a winner and declares a tie.
Graphical User Interface: Built using tkinter, allowing players to interact with a simple grid layout.

How It Works:
Start the Game: A 3x3 grid of buttons is displayed on the screen.
Player Moves: Players click on empty buttons to place their symbol ("X" or "O").
Win or Tie Detection: The game checks after each move for a winning combination or if the game ends in a tie.
Error Handling: If a player tries to click an already taken spot, an error message is shown.
