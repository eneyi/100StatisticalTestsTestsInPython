# Test 48 The signed rank test for two means (paired observations)

def signrankmtest(data1,data2):
    stat, pval=stats.wilcoxon(data1, data2)
    return stat