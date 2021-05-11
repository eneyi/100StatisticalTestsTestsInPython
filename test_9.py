# Test 9 t-test for two population means (variances unknown and unequal)

def t2Mean2UnequalVariance(smean1, smean2, svar1, svar2, ssize1, ssize2,
    pmean1=0.0, pmean2=0.0):
    statistic = float(((smean1 - smean2) - (pmean1 - pmean2)) / \
    sqrt((svar1 / ssize1) + (svar2 / ssize2)))
    df = float((((svar1 / ssize1) + (svar2 / ssize2)) ** 2) / \
    (((svar1 ** 2) / ((ssize1 ** 2) * (ssize1 - 1))) + \
    ((svar2 ** 2) / ((ssize2 ** 2) * (ssize2 - 1))))) 
    return statistic 