# 💰 Personal Expense Tracker CLI App

A smart, lightweight, and interactive Command Line Interface (CLI) application built in Python to manage and track daily expenses. It automatically saves your financial data in a structured `JSON` format.

## 🚀 Features

*   **🔒 Automated Storage**: Loads and saves expenses automatically using local `expenses.json`.
*   **📊 View Reports**: Clean, tabular terminal formatting for displaying descriptions, categories, amounts, and dates.
*   **➕ Add Expenses**: Input description, category filtering, and robust numeric validation.
*   **🔍 Filter by Category**: Instantly filter your spending to trace where your budget is going.
*   **🗑️ Flexible Deletion**: Delete individual transaction items safely by index or wipe the data file cleanly.
*   **🛡️ Error Handling**: Smooth handling for empty inputs, strings instead of integers, or runtime interruptions.
*   **⏳ UX Polish**: Beautiful startup loading bar visuals to improve user interactive feel.

## 🛠️ Tech Stack

*   **Language**: Python 3.x
*   **Core Modules**: `json`, `pathlib`, `datetime`, `time`

## 📂 Project Structure

```text
expense_tracker/
│
├── expense_tracker.py   # Main application script logic
└── expenses.json        # Auto-generated database storage file
```

## ⚙️ Installation & Usage

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com
    cd YOUR_REPOSITORY_NAME/Small_Projects/expense_tracker
    ```

2.  **Run the Application**:
    ```bash
    python expense_tracker.py
    ```

## 📋 How It Works

Upon launch, the application checks for an existing `expenses.json` file. If not found, it gracefully initiates an empty slate. The interactive menu lets you control your database seamlessly:

*   **Option 1**: Generates a visually formatted terminal budget summary sheet.
*   **Option 4**: Queries your collection based on exact category matches (e.g., `food`, `transport`).
*   **Option 5**: Securely `unlinks` the active JSON database storage tracking reference.
