import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


domain = np.linspace(-2, 2, 1000)
plt.plot(domain, norm.pdf(domain, 0, 1))
plt.title('Standard Normal')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
