#  Computer Guessing Game

A simple, fun, and interactive command-line game built with **Python**. The computer picks a secret number, and you have to guess it within a limited number of tries!

##  Features
- **Time Tracking:** Tells you exactly when you started, when you finished, and the total time played.
- **Error Handling:** Don't worry about typing mistakes! The game handles invalid inputs (like letters instead of numbers) without crashing.
- **Smart Hints:** Tells you if your guess is "Too High" or "Too Small" to help you win.
- **Replay ability :** Option to play again immediately after a game ends.

##  How to Play
1. Run the script: `python guess_game.py`
2. Select difficulty level
3. Enter your name to start.
4. You have **5 guesses**. Try to find the number between **1 and 100**.
5. Follow the hints provided after each wrong guess.

##  Requirements
- Python 3.x
- `random` and `time` modules (Built-in)

## Code Logic
The project uses:
- **Functions:** To keep the code clean (`starting`, `ending`, `guess_game`).
- **Try-Except Blocks:** To catch `ValueError` (invalid input) and `KeyboardInterrupt`.
- **Loops:** A `while` loop to manage the guessing turns and the game restart logic.


*Created with love for Python beginners to understands concept and logic .*
