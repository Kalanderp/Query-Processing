import pandas as pd
data = {
    'Name': ['Kalander', 'Asif', 'Junaid'],
    'Age': [20, 19, 21]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df['Name'] = df['Name'].str.swapcase()
print("\nDataFrame after swapping case:")
print(df)
