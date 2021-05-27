# Test 41 The χ2-test for consistency in a K × 2 table



def ChisquareKx2table(c1, c2, k):
    z = sum(c1)
    nx = sum(c2)
    n = [c1[i] + c2[i] for i in range(len(c1))]
    Total = sum(n)
    A = [x ** 2 for x in c1]
    B = sum([float(A[i]) / float(n[i]) for i in range(len(A))])
    C = (B - (float(z ** 2) / (float(Total))))
    D = float(Total ** 2) / float(z * (Total - z))
    statistic = D * C
    return statistic

