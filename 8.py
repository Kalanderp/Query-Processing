import pandas as pd
df = pd.read_csv("E:\Activity\device.csv")
pivot_table = pd.pivot_table(
    df,
    values='Unit_Sold',
    index='Item',
    aggfunc='sum'
)
print(pivot_table)
