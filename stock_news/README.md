# 📈 Stock Trading News Alert Service

An automated financial monitoring pipeline built with **Python**, the **Alpha Vantage Stock API**, **NewsAPI**, and the **Twilio SMS/WhatsApp API**. The script calculates day-over-day closing price fluctuations for a target equity and automatically fetches and dispatches contextual market news headlines when volatility exceeds a threshold.

---

## ✨ Features

* **📊 Market Data Ingestion:** Fetches daily stock time-series data using the Alpha Vantage REST API.
* **📐 Volatility Threshold Analysis:** Extracts consecutive closing prices via list comprehension, calculating day-over-day percentage changes.
* **📰 Contextual News Scraping:** Automatically triggers NewsAPI queries targeted at the company name (`qInTitle`) when price movements exceed $\pm 5\%$.
* **📱 Automated Message Delivery:** Formats and delivers top news articles (headline + description) with directional indicators (🔺/🔻) via Twilio SMS or WhatsApp.
* **🔐 Secure Environment Variables:** Protects API keys, account credentials, and phone numbers via `os.environ`.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **APIs:** Alpha Vantage API, NewsAPI, Twilio REST API
* **Libraries:** `requests`, `twilio`, `os`

---

## 🚀 How to Run

1. Navigate to the project directory:
   ```bash
   cd stock_news