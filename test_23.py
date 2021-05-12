# Test 23 The Z-test for correlated proportions

def Ztestcorrprop(b,c,N):
    cal1=(b-c)/N
    delta=sqrt(((b+c)-((b-c)**2)/N)/(N*(N-1)))
    statistic=cal1/delta
    return statistic