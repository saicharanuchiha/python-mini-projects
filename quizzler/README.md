# 🧠 Quizzler Trivia Desktop App

A dynamic desktop trivia quiz application built with **Python**, **Tkinter**, and the **Open Trivia Database API**[cite: 4, 5]. The app features an object-oriented architecture[cite: 1, 2, 3, 4], live API question fetching[cite: 5], HTML entity decoding[cite: 3], and real-time visual feedback[cite: 4].

---

## ✨ Features

* **🌐 Dynamic REST API Ingestion:** Fetches real-time boolean (True/False) trivia questions directly from the Open Trivia DB API using the `requests` library[cite: 5].
* **🧹 HTML Entity Decoding:** Automatically decodes raw HTML entities in questions (e.g., `&quot;`, `&#039;`) into clean readable text using Python's built-in `html.unescape()`[cite: 3].
* **🧩 Modular OOP Architecture:** Organized cleanly across dedicated modules:
  * `Question`: Data model defining question text and answer attributes[cite: 2].
  * `QuizBrain`: State machine managing score tracking, progression, and answer validation[cite: 3].
  * `QuizInterface`: GUI controller managing Tkinter window states, canvas text, and click events[cite: 4].
* **🎯 Python Type Hinting:** Implements explicit datatype annotations (`quiz_brain: QuizBrain`) to catch interface bugs and ensure type safety[cite: 4].
* **⏱️ Visual Response Feedback:** Flashes the Tkinter `Canvas` green for correct answers and red for incorrect answers, resetting after a 1000ms delay via `window.after()`[cite: 4].
* **🔒 End-of-Quiz Safety:** Automatically disables answer buttons upon reaching the final question to prevent out-of-range execution[cite: 4].

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **GUI Framework:** Tkinter[cite: 4]
* **Networking & Data:** `requests`[cite: 5], `html`[cite: 3]
* **Data Source:** Open Trivia Database API[cite: 5]

---

## 🚀 How to Run

1. Navigate to the project directory:
   ```bash
   cd quizzler