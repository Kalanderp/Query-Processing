import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title("Scatter Plot of Random Distribution")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
