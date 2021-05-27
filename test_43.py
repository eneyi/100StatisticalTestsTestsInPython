# Test 43 The χ2-test for consistency in a 2 × K table

def Chisquare2xKtable(s1, s2):
    N1 = sum(s1)
    N2 = sum(s2)
    Total = N1 + N2
    n =[s1[i] + s2[i] for i in range(len(s1))]
    e1 = [float(N1 * x) / float(N1 + N2) for x in n]
    e2 = [float(N2 * x) / float(N1 + N2) for x in n]
    A = [((s1[i] - e1[i]) **2) / e1[i] for i in range(len(s1))]
    B = [((s2[i] - e2[i]) **2) / e2[i] for i in range(len(s2))]
    statistic = sum([A[i] + B[i] for i in range(len(A))])
    return statistic