import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ARTICLES_TO_FETCH = 3
PRICE_THRESHOLD = 0.05

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY_STOCKS = os.environ.get('API_KEY_STOCKS')
API_KEY_NEWS = os.environ.get('API_KEY_NEWS')

stocks_params = {
    "function" : "TIME_SERIES_INTRADAY",
    "symbol" : STOCK,
    "interval" : "60min",
    "apikey" : API_KEY_STOCKS
}

stock_data = requests.get(url=STOCK_ENDPOINT, params=stocks_params)
stock_data.raise_for_status()

stock_data_json = stock_data.json()

close_prices_list = []
for stock_date in stock_data_json['Time Series (60min)']:
    if stock_date[11:19] == '20:00:00':
        close_prices_list.append(stock_data_json['Time Series (60min)'][stock_date]['4. close'])

alert_price = False
diff_prices = float(close_prices_list[0]) - float(close_prices_list[1])
if abs(diff_prices) >= float(close_prices_list[1]) * PRICE_THRESHOLD:
    alert_price = True

news_params = {
    "q" : STOCK,
    "apiKey" : API_KEY_NEWS
}

news_data = requests.get(NEWS_ENDPOINT, news_params)
news_data.raise_for_status()

news_data_json = news_data.json()

articles = []

i = 0
while i < ARTICLES_TO_FETCH:
    articles.append(news_data_json['articles'][i])
    i += 1

if alert_price:
    symbol = f"🔺" if diff_prices > 0 else f"🔻"
    news = "\n".join([f"Headline: {article['title']}\nBrief: {article['description']}" for article in articles])
    message = f"{STOCK}: {symbol}{abs(round(diff_prices, 4))}%\n" \
              f"{ARTICLES_TO_FETCH} articles fetched: \n" \
              f"{news}"
else:
    message = f"{STOCK} price has not increased or decreased {PRICE_THRESHOLD*100}% during the last 24h"
print(message)
