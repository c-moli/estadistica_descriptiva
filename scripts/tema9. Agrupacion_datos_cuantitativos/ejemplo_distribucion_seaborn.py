import seaborn as sb
import random
from scipy import stats
import matplotlib.pyplot as plt

vals = [1,2,3,5,7,8,9,10]
freqs = (random.randint(5,20) for _ in vals)
data = []
for k, v in zip(vals, freqs):
    data.extend([k]*v)

sb.distplot(data, fit=stats.norm, kde = True)
sb.set_style("darkgrid")
plt.show()