# Test 8 t-test for two population means (variance unknown but equal)

def t2Mean2EqualVariance(smean1, smean2, svar1, svar2, ssize1, ssize2,
    pmean1=0.0, pmean2=0.0):
    df = ssize1 + ssize2 - 2
    pvar = float((((ssize1 - 1) * svar1) + ((ssize2 - 1) * svar2)) / df)
    statistic = float(((smean1 - smean2) - (pmean1 - pmean2)) / ((sqrt(pvar)) * sqrt((1.0 / ssize1) + (1.0 / ssize2))))
    return statistic
