# ⏱️ Pomodoro Desktop Timer App

A clean, responsive desktop productivity timer built with **Python** and **Tkinter**, implementing the Pomodoro Technique with visual session tracking and non-blocking asynchronous countdowns.

---

## ✨ Features

* **🎨 Layered Canvas GUI:** Uses Tkinter's `Canvas` widget to render the tomato graphic and overlay the countdown timer text with dynamic color states.
* **⏱️ Asynchronous Execution:** Implements non-blocking timer loops using `window.after()` and `window.after_cancel()`, keeping the GUI fully responsive without freezing the event loop.
* **🔄 Automatic Interval Progression:** Seamlessly cycles through:
  * **Work:** 25-minute focus session (Green)
  * **Short Break:** 5-minute recovery interval (Pink)
  * **Long Break:** 20-minute extended rest after 4 work cycles (Red)
* **✅ Visual Checkmark Tracking:** Automatically updates checkmarks (`✓`) on the interface as completed focus blocks accumulate.
* **🛡️ Re-trigger & Overlap Prevention:** Guards against duplicate countdown threads when clicking "Start" repeatedly.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **GUI Framework:** Tkinter
* **Core Modules:** `math`

---

## 🚀 How to Run

1. Navigate to the project directory:
   ```bash
   cd pomodoro