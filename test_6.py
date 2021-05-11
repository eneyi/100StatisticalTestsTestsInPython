# Test 6 Z-test for comparing two counts (Poisson distribution)

def Z2Count(time1,time2,count1,count2): 
    R1 =count1 / float(time1)
    R2 = count2 / float(time2)
    statistic = (R1 - R2) / sqrt((R1 / time1) + (R2 / time2))
    return statistic 