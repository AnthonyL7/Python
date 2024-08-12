import pandas as pd 
import datetime
import time
import numpy as np

from yahooquery import Ticker

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

symbol = 'AAPL'
stock = Ticker(symbol)
balance_sheet = stock.balance_sheet()
print(balance_sheet)

df_balance = pd.DataFrame(stock.balance_sheet())
df_balance['asOfDate'] = pd.to_datetime(df_balance['asOfDate'])
df_balance.set_index('asOfDate', inplace = True)

currency = df_balance['currencyCode'].iloc[0]
balance_period = df_balance['periodType'].iloc[0]

df_balance = df_balance.iloc[:, 2:]