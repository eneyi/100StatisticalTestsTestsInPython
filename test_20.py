# Test 20 Fisher’s cumulant test for normality of a population

from scipy.stats import skew
from scipy.stats import kurtosis 
import numpy as np  
import pylab as p  
  
x1 = np.linspace( -5, 5, 1000 ) 
y1 = 1./(np.sqrt(2.*np.pi)) * np.exp( -.5*(x1)**2  ) 