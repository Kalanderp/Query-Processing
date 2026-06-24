import numpy as np
import matplotlib.pyplot as plt
men_means = (22, 30, 33, 30, 26)
women_means = (25, 32, 30, 35, 29)
groups = ['G1', 'G2', 'G3', 'G4', 'G5']
x = np.arange(len(groups))
width = 0.35
plt.bar(x - width/2, men_means, width,
        color='green', label='Men')
plt.bar(x + width/2, women_means, width,
        color='red', label='Women')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(x, groups)
plt.legend()
plt.show()
