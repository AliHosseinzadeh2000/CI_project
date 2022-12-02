import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min


x = np.linspace(0, 5, 1000)
fix, ax = plt.subplots(figsize=(16, 6))
ax.plot(x, weibull_min.pdf(c=0.80, x=x, loc=0, scale=1))
plt.show()
