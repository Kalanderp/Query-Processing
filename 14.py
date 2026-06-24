import pandas as pd
import numpy as np
data = {
    'A': [10, np.nan, 30, 40],
    'B': [50, 60, np.nan, 80],
    'C': [90, 100, 110, np.nan]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df.fillna(0, inplace=True)
print("\nDataFrame after replacing NaN values:")
print(df)
