
#  CLI To-Do List App (Python)

A lightweight, terminal-based To-Do List application built from scratch using Python. This project focuses on **File Handling**, **Error Management**, and the **Pathlib** library for robust file system interactions.

## Features

- **Dynamic Task Numbering:** Automatically reads the last task number from the file so you never lose track.
- **Smart Deletion:** Deletes tasks by their number and automatically re-indexes the remaining tasks (1, 2, 3...).
- **Persistent Storage:** Saves all your tasks in a dedicated `To_Do_app/report.txt` file.
- **Robust Exception Handling:** Gracefully handles empty inputs, strings instead of numbers, and missing files.
- **Clean UI:** Simple menu-driven interface for seamless navigation.

##  Tech Stack

- **Language:** Python 3.x
- **Libraries:** `pathlib` (Object-oriented filesystem paths)

##  Project Structure

```text
To_Do_app/
└── report.txt      # Your tasks are stored here
main.py             # Main application logic

```
### How It Works

View Tasks: Reads the report.txt and displays all saved chores.

Add Task: Checks if a file exists; if not, creates one and appends the new task with an auto-incremented ID.

Delete Task: Removes a specific task and shifts the IDs of subsequent tasks to maintain a clean sequence.

Error Handling: Uses try-except blocks to prevent crashes when users enter invalid data or leave inputs empty.

**Installation & Usage*
Clone the repository:
bash
git clone https://github.com


**Run the application:**
bash
python main.py


### What I Learned

During this project, I mastered:

Handling Global Variables across functions.

Managing file pointers using with open() in different modes (r, w, a).

Using Match-Case (Python 3.10+) for cleaner menu logic.

Implementing custom Exceptions and input validation.
Built with pure heart by [M.Umar]





