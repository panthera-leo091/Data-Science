import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.arange(1, 10, 2)
y = np.arange(2, 11, 2) + x
plt.plot(x, y)

plt.title("Avanish Singh is uning pandas and numpy", fontdict={"fontname": "Comic Sans MS", "fontsize": 20})

plt.xlabel("X-axis", fontdict={"fontname": "Times New Roman", "fontsize": 10})
plt.ylabel("Y-axis", fontdict={"fontname": "Arial", "fontsize": 15})

# plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20])
# plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 19, 20])

plt.show()