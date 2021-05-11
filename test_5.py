#Test 5 Z-test for the equality of two proportions (binomial distribution)
def Z2Proportion(spro1,spro2,ssize1,ssize2):
    P = ((spro1 * ssize1) + (spro2 * ssize2)) / (ssize1 + ssize2)
    statistic = (spro1 - spro2) / (P * (1.0 - P) * ((1.0 / ssize1) + (1.0 / ssize2))) ** 0.5
    return statistic