import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E:\Activity\Alphabet.csv")

df['Date'] = pd.to_datetime(df['Date'])

filtered = df[(df['Date'] >= '2023-01-01') &
              (df['Date'] <= '2023-12-31')]

plt.plot(filtered['Date'], filtered['Close'])
plt.title('Alphabet Inc Stock Price')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()
