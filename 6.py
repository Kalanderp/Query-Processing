import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"E:\Activity\alphabet_data.csv")
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
filtered = df[(df['Date'] >= '2020-04-01') &
              (df['Date'] <= '2020-05-01')]
plt.scatter(filtered['Volume'],
            filtered['Close'])
plt.title('Alphabet Inc. Trading Volume vs Close Price')
plt.xlabel('Trading Volume')
plt.ylabel('Close Price')
plt.grid(True)
plt.show()
