# Test 27 F-test for multiple comparison of contrasts between K population means

def f_test_multiple(mean1,mean2,mean3,n1,n2,n3,var):
    statistic1=(((mean1-mean2)**2)/(1/n1+1/n2))/var
    statistic2=(((mean1-mean3)**2)/(1/n1+1/n3))/var
    statistic3=(((mean2-mean3)**2)/(1/n2+1/n3))/var
    return statistic1, statistic2, statistic3
