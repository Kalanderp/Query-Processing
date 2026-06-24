import pandas as pd
import numpy as np

# Create DataFrame
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['B', 'C', 'D', 'E'])

df.insert(0, 'A', range(1, 11))

# Function to color values
def color_negative_red(value):
    if value < 0:
        return 'color:red'
    else:
        return 'color:black'

# Apply styling
styled_df = df.style.applymap(
    color_negative_red,
    subset=['B', 'C', 'D', 'E']
)

print(df)
styled_df