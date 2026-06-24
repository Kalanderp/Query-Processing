import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['A', 'B', 'C', 'D'])
df.iloc[1, 2] = np.nan
df.iloc[4, 1] = np.nan
df.iloc[7, 3] = np.nan
styled_df = df.style.highlight_null(color='red')
print(df)
styled_df
