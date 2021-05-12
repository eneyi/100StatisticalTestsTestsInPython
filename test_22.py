# Test 22 F-test for K population means (analysis of variance)

def Ftestkpop(varT, var2, K, N): 
    statistic = float((var2 / (K- 1))) / ((varT - var2)/(N-K))
    return statistic