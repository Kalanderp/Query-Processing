import pandas as pd
df = pd.read_csv("E:\Activity\order.csv")
df['Sale_amt'] = df['Sale_amt'].replace(',', '', regex=True).astype(float)
pivot_table = pd.pivot_table(
    df,
    values='Sale_amt',
    index=['Region', 'Manager', 'SalesMan'],
    aggfunc='sum'
)
print(pivot_table)
