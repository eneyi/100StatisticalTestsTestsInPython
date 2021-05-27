# Test 37 The χ2-test for goodness of fit

def ChisqFit(observed, expected):
    freq = [float((observed[i] - expected[i]) ** 2) / (float(expected[i]))
    for i in range(len(observed))]
    statistic = 0.0
    for x in freq: statistic = statistic + x
    return statistic