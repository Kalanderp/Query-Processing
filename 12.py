import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['A', 'B', 'C', 'D'])
styled_df = df.style.set_properties(
    **{
        'background-color': 'black',
        'color': 'yellow'
    }
)
print(df)
styled_df
