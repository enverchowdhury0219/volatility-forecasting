import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fetch data
ticker = 'SPY'
start_date = '2020-08-01'
end_date = '2023-08-01'

df = yf.download(ticker, start=start_date, end=end_date)

#renaming close column to price
df = df[['Close']].rename(columns={'Close': 'Price'})

# Log returns
df['LogReturn'] = np.log(df['Price'] / df['Price'].shift(1))
df = df.dropna()

# Plot
plt.figure(figsize=(12, 4))
plt.plot(df.index, df['LogReturn'], label='Log Returns')
plt.title('Daily Log Returns of SPY')
plt.xlabel('Date')
plt.ylabel('Log Return')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

