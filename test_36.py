# Test 36 The Kolmogorov–Smirnov test for comparing two populations

from scipy import stats
np.random.seed(30032021) 
rvs1 = stats.norm.rvs(size=200, loc=0., scale=1)
rvs2 = stats.norm.rvs(size=300, loc=0.5, scale=1.5)
stats.ks_2samp(rvs1, rvs2)