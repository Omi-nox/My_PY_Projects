# Interactive Command-Line Quiz Application

A Python-based command-line quiz application that allows users to take a customized quiz with a dynamic scoring system, custom error handling, and animated loading screens.

## 🎓 About the Project
I am an AI Technology student learning Python! This mini-project is part of my learning journey to master core programming concepts, logic building, and terminal-based user interfaces.

## 🚀 Features

*   **Custom Question Selection:** Users can choose how many questions they want to attempt.
*   **Randomization:** Questions are shuffled automatically using Python's `random` module.
*   **Robust Error Handling:** Features a custom exception (`MyCustomError`) to handle empty inputs or invalid options seamlessly.
*   **Interactive UI:** Includes terminal animations like typing delays and dynamic borders that match question lengths.
*   **Instant Feedback:** Provides immediate results for each question and a comprehensive final scorecard with percentages.

## 🛠️ Prerequisites

Make sure you have Python installed on your system:
*   Python 3.x

## 💻 How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   ```

2. Navigate to the project directory:
   ```bash
   cd quiz-app
   ```

3. Ensure your `questions` list data is defined in the script, then run:
   ```bash
   python main.py
   ```

## 🏗️ Code Architecture

The application is built using modular functions:
*   `inp(opt1)`: Validates user input and enforces uppercase consistency.
*   `check(opt1, choice)`: Evaluates the user's choice against the correct answer and tracks scores.
*   `ques(questions, no)`: Handles the core game loop, shuffles data, and prints the final report card.
