# 🎴 Flash Card Capstone App

An interactive desktop language-learning flash card application built with **Python**, **Tkinter**, and **Pandas**. The app tests vocabulary retention with automatic card flips and dynamically saves your learning progress to disk.

---

## ✨ Features

* **🎨 Responsive Canvas GUI:** Layered images and typography using Tkinter's `Canvas` widget for smooth front/back flash card transitions.
* **⏱️ Asynchronous Flip Timer:** Non-blocking 3-second delay using `window.after()` and `window.after_cancel()` to automatically flip cards and display English translations.
* **📊 Pandas Data Pipeline:** Ingests vocabulary datasets and dynamically transforms DataFrame records for real-time quiz logic.
* **💾 Smart Progress Persistence:** 
  * Marking a word as "known" (✓) removes it from the current study pool.
  * Automatically exports remaining words to `words_to_learn.csv` so progress is never lost between sessions.
* **🛡️ Resilient Error Handling:** Uses `try-except-else` blocks to load custom progress files first, gracefully falling back to the default dataset if no save file exists.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **GUI Framework:** Tkinter
* **Data Processing:** Pandas
* **Storage:** CSV File I/O

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/saicharanuchiha/python-mini-projects.git](https://github.com/saicharanuchiha/python-mini-projects.git)