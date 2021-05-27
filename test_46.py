# Test 46 The sign test for two medians (paired observations)

def signtesttwomedns(x,y):
    comapare=x < y
    plus=np.sum(comapare)
    minm=len(x)-plus
    statistic=min(plus,minm)
    return statistic