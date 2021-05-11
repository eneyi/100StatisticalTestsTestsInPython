# Test 2 Z-test for two population means (variances known and equal)
def Z2Mean1Variance(smean1:float, smean2:float, pmean1:float, pmean2:float, pvar:float, ssize1:int, ssize2:int):
    statistic = ((smean1 - smean2) - (pmean1 - pmean2))/ (pvar * sqrt((1.0 / ssize1) + (1.0 / ssize2)))
    return statistic