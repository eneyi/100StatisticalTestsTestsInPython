# Test 11 t-test of a regression coefficient

def tRegressionCoefficient(variancex, varianceyx, b, ssize):
    statistic = float(((b * sqrt(variancex)) / \
    sqrt(varianceyx)) * ((ssize-1) ** -0.5))
    return statistic
