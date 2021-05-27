# Test 45 The sign test for a median
def signtes(samp,median):
    A=sum(i > median for i in samp)
    B=sum(i < median for i in samp)
    statistic=A+B
    return statistic