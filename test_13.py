# Test 13 Z-test of a correlation coefficient

def ZPearsonCorrelation(ssize,sr,pr):
    Z1 = 0.5 * log((1 + sr) / (1 - sr))
    meanZ1 = 0.5 * log((1 + pr) / (1 - pr))
    sigmaZ1 = 1.0 / sqrt(ssize - 3)
    statistic = (Z1 - meanZ1) / sigmaZ1
    return statistic