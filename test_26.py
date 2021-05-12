# Test 26 F-test for the overall mean of K subpopulations (analysis of variance)

def Ftestovermean(var1,pmean, N,K):
    x1=1505
    x2=1528
    x3=1564
    x4=1498
    x5=1600
    x6=1470
    xT=((x1+x2+x3+x4+x5+x6)/6)
    statistic=((N*((xT-pmean)**2))/(var1/(K-1)))
    return statistic