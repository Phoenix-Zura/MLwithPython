import numpy as np

vals = np.random.normal(0,0.5,10000)

vals = vals.tolist()
print(type(vals))

print(np.percentile(vals,50))
print(np.percentile(vals,90))

# moments
vals = np.random.normal(0,0.5,10000)
print(np.mean(vals))
print(np.var(vals))

import scipy.stats as sp 
print(sp.skew(vals))
print(sp.kurtosis(vals))