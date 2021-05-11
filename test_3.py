# Test 3 Z-test for two population means (variances known and unequal)

def Z2Mean2Variance(smean1:float, smean2:float, pvar1:float, pvar2:float, ssize1:float, ssize2:float): 
    statistic = ((smean1 - smean2) - (pmean1 - pmean2)) / sqrt((pvar1 / ssize1) + (pvar2 / ssize2))
    return statistic