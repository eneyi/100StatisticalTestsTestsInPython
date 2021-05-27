# Test 50 The median test of two populations 

def MedianTestfor2Pop(s1, s2):
    ls1 = s1[0]
    rs1 = s1[1]
    ls2 = s2[0]
    rs2 = s2[1]
    N = ls1 + ls2 + rs1 + rs2
    statistic = float(((abs((ls1*rs2)-(ls2*rs1))-(N * 0.5))**2)*N) / \
    ((ls1+ls2)*(ls1+rs1)*(ls2+rs2)*(rs1+rs2))
    return statistic