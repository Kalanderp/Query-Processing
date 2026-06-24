import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"E:\Activity\fdata.csv")
plt.figure(figsize=(8,6))
plt.plot(df['Date'], df['Open'], label='Open')
plt.plot(df['Date'], df['High'], label='High')
plt.plot(df['Date'], df['Low'], label='Low')
plt.plot(df['Date'], df['Close'], label='Close')
plt.title('Alphabet Inc Financial Data (Oct 3, 2016 - Oct 7, 2016)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
