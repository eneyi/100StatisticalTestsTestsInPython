# Test 38 The χ2-test for compatibility of K counts

def tx2testofKcounts(T, V):
    R = float(sum(V)) / float(sum(T))
    freq = [((V[i] - (T[i] * R)) ** 2) / float(T[i] * R)
    for i in range(len(V))]
    statistic = sum(freq)
    return statistic