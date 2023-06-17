import matplotlib.pyplot as plt
import numpy as np
# Creating dataset
#np.random.seed(10)
data = [10.1, 12.2, 9.3, 12.4, 13.7, 10.8, 11.6, 10.1, 11.2, 11.3, 12.2, 12.6, 11.5, 9.2, 14.2, 11.1, 13.3, 11.8, 7.1, 10.5]                     #np.random.normal(100, 20, 200)

fig = plt.figure(figsize=(10, 7))

# Creating plot
plt.boxplot(data)

# show plot
plt.show()