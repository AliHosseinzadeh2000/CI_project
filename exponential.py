import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon


x = np.linspace(0, 5, 1000)
fix, ax = plt.subplots(figsize=(16, 6))
ax.plot(x, expon.cdf(x=x, loc=0, scale=1))
plt.show()
