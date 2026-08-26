# 🏋️ Workout Habit Tracker (Pixela API)

An automated habit tracking and quantitative logging script built with **Python**, **Requests**, and the **Pixela REST API**. The application handles full HTTP lifecycle operations (`POST`, `PUT`, `DELETE`) with custom HTTP header authentication, enabling automated data logging and streak visualization directly on an interactive GitHub-style commit graph.

---

## ✨ Features

* **🔐 Header-Based Authentication:** Passes API authentication securely via custom HTTP headers (`X-USER-TOKEN`) rather than URL query parameters.
* **📅 Dynamic Date Serialization:** Uses Python's `datetime.now().strftime("%Y%m%d")` to format UTC-compliant date strings dynamically.
* **📦 Complex Data Payloads:** Serializes custom metadata dictionaries using `json.dumps()` to pass nested structures into Pixela's `optionalData` field.
* **🌐 Dynamic User Input:** Accepts command-line prompts (`input()`) for workout duration and exercise variations.
* **🔄 HTTP Lifecycle Management:** Built to handle user registration (`POST`), graph definition (`POST`), pixel data logging (`POST`), and pixel updates (`PUT`).

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Networking & Data:** `requests`, `json`, `datetime`
* **API Service:** [Pixela API](https://pixe.la/)

---

## 🚀 How to Run

1. Navigate to the project directory:
   ```bash
   cd habit_tracker