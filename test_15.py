# Test 15 χ2-test for a population variance

def ChiSquarePopVar(values, ssize, pv):
    mean = sum(values)/ssize
    freq = [float((values[i] - mean) ** 2)
    for i in range(len(values))]
    sv = float((sum(freq)/(ssize-1)))
    statistic = float((((ssize - 1) * sv) / pv))
    return statistic
