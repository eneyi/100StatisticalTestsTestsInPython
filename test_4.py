#Test 4 Z-test for a proportion (binomial distribution)

def Z1Proportion(spro:float, ppro:float, ssize:int):
    statistic = (abs(ppro - spro) - (1 / (2 * ssize))) / sqrt((ppro * (1 - spro)) / ssize)
    return statistic