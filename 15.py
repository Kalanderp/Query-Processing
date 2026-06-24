import pandas as pd
import numpy as np
data = {
    'A': [1, np.nan, np.nan, 4, np.nan],
    'B': [np.nan, np.nan, 3, 4, np.nan],
    'C': [1, 2, np.nan, 4, np.nan],
    'D': [1, np.nan, 3, 4, 5]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
result = df[df.isnull().sum(axis=1) >= 2]

print("\nRows with at least 2 NaN values:")
print(result)
