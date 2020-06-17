import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n) 

plt.bar(X, +y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, y1):     
    plt.text(x, y + 0.03, '%.2f' % y, ha='center', va='bottom', fontdict={"size":9, "stretch":0})

for x, y in zip(X, y2):     
    plt.text(x, -y-0.15, '%.2f' % y, ha='center', va='bottom', fontdict={"size":9, "stretch":0})

plt.xticks([])
plt.yticks([])
plt.ylim(-1.25, +1.25)

plt.show()