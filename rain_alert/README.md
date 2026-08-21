# 🌧️ Automated Rain Alert SMS

An automated meteorological notification service built with **Python**, the **OpenWeatherMap API**, and the **Twilio SMS API**. The service monitors upcoming 12-hour forecast windows, evaluates weather condition codes, and dispatches automated SMS alerts when rain or inclement weather is detected.

---

## ✨ Features

* **📡 Weather Forecast Ingestion:** Fetches granular 3-hour forecast chunks from the OpenWeatherMap API via the `requests` library.
* **🔍 Predictive Slice Filtering:** Slices incoming forecast JSON payloads (`weather_data["list"][:4]`) to evaluate upcoming weather windows.
* **⚠️ Meteorological Code Parsing:** Evaluates condition codes (`id < 700`) to detect drizzle, rain, thunderstorms, and snow.
* **📱 Automated SMS Delivery:** Dispatches custom SMS alerts to your phone using the Twilio REST API client.
* **🔐 Secure Credential Management:** Protects sensitive API keys, Account SIDs, and Auth Tokens using environment variables (`os.environ`).

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **APIs:** OpenWeatherMap API, Twilio REST API
* **Libraries:** `requests`, `twilio`, `os`

---

## 🚀 How to Run

1. Navigate to the project directory:
   ```bash
   cd rain_alert