# Test 35 The Kolmogorov–Smirnov test for goodness of fit

from scipy import stats
x = np.linspace(-15, 15, 9)
stats.kstest(x, 'norm')

