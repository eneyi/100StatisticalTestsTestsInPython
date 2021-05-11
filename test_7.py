# Test 7 t-test for a population mean (variance unknown)

def t1Mean(smean, pmean, svar, ssize):
    statistic = float((smean - pmean) / (svar / sqrt(ssize)))
    return statistic