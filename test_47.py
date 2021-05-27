# Test 47 The signed rank test for a mean

def signrank(data,checkval):
    rank, pVal = stats.wilcoxon(data - checkval)
    return rank

