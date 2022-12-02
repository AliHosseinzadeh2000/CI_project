import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import poisson


x_rvs = pd.Series(poisson.rvs(1.2, size=100000, random_state=2))
data = x_rvs.value_counts().sort_index().to_dict()

fig, ax = plt.subplots(figsize=(16, 6))
ax.bar(range(len(data)), list(data.values()), align='center')

plt.xticks(range(len(data)), list(data.keys()))
plt.show()
