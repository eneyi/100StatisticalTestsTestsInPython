# Test 14 Z-test for two correlation coefficients

def Z2PearsonCorrelation(r1,r2,ssize1,ssize2):
    z1 = 0.5 * log((1.0 + r1) /(1.0 - r1))
    z2 = 0.5 * log((1.0 + r2) /(1.0 - r2))
    sigma1 = 1.0 / sqrt(ssize1 - 3)
    sigma2 = 1.0 / sqrt(ssize2- 3)
    sigma = sqrt((sigma1 ** 2) + (sigma2 ** 2))
    statistic = abs(z1 - z2) / sigma
    return statistic