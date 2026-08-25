import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = ""
NEWS_API_KEY = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_price = response.json()
data = stock_price["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_closing_price = float(data_list[0]["4. close"])
day_before_yesterday = float(data_list[1]["4. close"])

diff_in_close = yesterday_closing_price - day_before_yesterday
up_down = None
if diff_in_close> 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((diff_in_close / day_before_yesterday) * 100)

if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{abs(diff_percent)}%\nHeadline: {article['title']}.\nBrief: {article['description']}"
        for article in three_articles
    ]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="YOUR_TWILIO_NUMBER",
            to="YOUR_PHONE_NUMBER"
        )
