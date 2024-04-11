
# Mastermind Game

This repository contains the Python implementation of the classic game Mastermind, a code-breaking game for one player against a computer. In this game, the computer generates a secret code consisting of a sequence of 4 colors. The player attempts to guess the code within a set number of tries.

## Game Description

The Mastermind game is based on the original board game where one player, the codemaker, sets a secret code, and the other player, the codebreaker, tries to match the code within a limited number of guesses. In this implementation:

- The computer acts as the codemaker and generates a secret code of 4 colors.
- The codebreaker (player) tries to guess the secret code.
- The possible colors are Red, Green, Yellow, Blue, Orange, and White.
- The player has 10 attempts to guess the correct color combination.
- After each guess, the game provides feedback on the number of correctly guessed colors and how many of them are in the correct position.

## How to Play

1. Clone or download this repository to your local machine.
2. Ensure you have Python installed on your computer.
3. Navigate to the directory containing the game script.
4. Run the script using Python:
   ```
   python game.py
   ```
5. The game will prompt you to enter your guesses. Each guess should consist of a sequence of 4 color initials (e.g., "RGBY" for Red, Green, Blue, Yellow).
6. Follow the game's feedback and try to crack the code in 10 guesses or fewer.

## Setup

No additional setup or libraries are required beyond having Python installed on your computer.

## Notes

- This game is a fun way to test your logic and deduction skills.
- Feel free to explore the code and understand how the game logic is implemented.
- If you encounter any issues or have suggestions for improvements, please feel free to contribute to the repository or open an issue.

Good luck, and have fun playing Mastermind!
