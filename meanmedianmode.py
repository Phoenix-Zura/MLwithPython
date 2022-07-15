#mean median mode
import numpy as np

#creating 10000 datapoints around mean of 27000 and standard deviation of 15000
incomes = np.random.normal(27000,15000,10000)
print(np.mean(incomes))

#data is split into packets of 50 and see and plot of the data
import matplotlib.pyplot as plt
#plt.hist(incomes,50)
#plt.show()

print(np.median(incomes))

from scipy import stats
print(stats.mode(incomes))
