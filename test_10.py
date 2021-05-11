# Test 10 t-test for two population means (method of paired comparisons)

def tPaired(smean1, smean2, svar, ssize):
    statistic = float((smean1 - smean2) / (svar / sqrt(ssize)))
    return statistic 