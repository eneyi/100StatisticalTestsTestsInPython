# Test 34 Cochran’s test for variance outliers

def cochrantest(var):
    statistic=max(var)/np.sum(var)
    return statistic