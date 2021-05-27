# Test 33 The w/s-test for normality of a population

def w_stest(var1,var2,range1,range2):
    stddev1=sqrt(var1)
    stddev2=sqrt(var2)
    statistic1=(range1)/(stddev1)
    statistic2=(range2)/(stddev2)
    return statistic1,statistic2
