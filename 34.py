import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
sizes = 1000 * np.random.rand(50)
plt.scatter(x, y, s=sizes)
plt.title("Scatter Plot with Different Ball Sizes")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
