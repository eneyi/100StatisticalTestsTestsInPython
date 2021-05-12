# Test 17 F-test for two population variances (with correlated observations)

def F2CorrelatedObs(r, var1, var2, ssize1, ssize2): 
    statistic = float(((var1 / var2)- 1) / (((((var1 / var2) + 1) ** 2)- (4 * (r ** 2) * (var1 / var2))) ** 0.5))
    return statistic