# Test 19 Chi-square test for an assumed population variance

def Chisq2Variance(ssize, svar, pvar):
    statistic = float((ssize-1) * svar/pvar)
    return statistic