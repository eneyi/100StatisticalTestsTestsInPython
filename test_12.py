# Test 12 t-test of a correlation coefficient

def tPearsonCorrelation(r, ssize): 
    statistic = float((r * sqrt(ssize - 2)) / sqrt(1 - (r **2))) 
    return statistic