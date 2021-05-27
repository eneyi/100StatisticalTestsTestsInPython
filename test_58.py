# Test 58 The Spearman rank correlation test (paired observations) 

def SpearmanCorrelation(R,ssize):
    statistic = (6.0 * R) - (ssize * ((ssize ** 2) - 1.0))
    statistic = statistic / (ssize * (ssize + 1.0) * sqrt(ssize - 1.0))
    return statistic