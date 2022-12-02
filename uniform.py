import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform


x = 0.3
a = 0
b = 1

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(np.linspace(a-1, b+1, num=10000),
        [uniform.pdf(x, a, b) for x in np.linspace(a-1, b+1, num=10000)])
plt.show()
