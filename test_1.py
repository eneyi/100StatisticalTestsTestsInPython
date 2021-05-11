# Test 1 Z-test for a population mean (variance known)

def Z1Mean1Variance(smean:float, pmean:float, pvar:float, ssize:int):
    statistic = abs(smean - pmean)/ (pvar / sqrt(ssize))
    return statistic