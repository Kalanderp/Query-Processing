import pandas as pd
df = pd.read_csv("E:\Activity\sales.csv")
pivot_table = pd.pivot_table(
    df,
    values='Sale_Value',
    index='Item',
    aggfunc=['max', 'min']
)
print(pivot_table)
