import pandas as pd
import yfinance as yf
import time
from datetime import datetime
from datetime import timedelta

stock_id = "tsla"

stock = yf.Ticker(stock_id)

now = datetime.now()
now = now.strftime("%H:%M:%S")
now2 = datetime.now() - timedelta(minutes=5)
now2 = now2.strftime("%H:%M:%S")
print(now, now2)

df = stock.history(start = now2, end = now).close

print(df)


