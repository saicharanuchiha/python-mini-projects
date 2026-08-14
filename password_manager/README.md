# 🔐 Password Manager GUI

A desktop credential vault and password generator built with **Python**, **Tkinter**, and **JSON data storage**, featuring instant search querying, clipboard integration, and comprehensive error handling.

---

## ✨ Features

* **⚡ One-Click Password Generator:** Generates high-entropy passwords combining randomized letters, numbers, and symbols, and automatically copies them to the clipboard via `pyperclip`.
* **🔍 Search & Query Engine:** Key-lookup feature (`find_password()`) to quickly search saved credentials by website name and display account details in popup dialogs.
* **💾 Structured JSON Data Persistence:** Serializes and updates credential records using Python's `json` module (`json.dump()`, `json.load()`, and `dict.update()`).
* **🛡️ Resilient Exception Handling:** Employs `try-except-else-finally` blocks to handle missing data files (`FileNotFoundError`) gracefully while ensuring UI fields are cleaned after saving.
* **⚠️ Form Validation:** Validates required fields before writing to disk and prompts users with Tkinter `messagebox` alerts if fields are left blank.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **GUI Framework:** Tkinter (`Canvas`, `Entry`, `Button`, `messagebox`)
* **Storage:** JSON File I/O
* **Utilities:** `pyperclip`, `random`

---

## 🚀 How to Run

1. Navigate to the project directory:
   ```bash
   cd password_manager