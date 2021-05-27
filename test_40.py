# Test 40 The χ2-test for consistency in a 2 × 2 table

def Chisq2x2(s1, s2, ssize):
    s1c1 = s1[0]
    s1c2 = s1[1]
    s2c1 = s2[0]
    s2c2 = s2[1]
    statistic = (float(ssize - 1) * ((float(s1c1 * s2c2) - \
    float(s1c2 * s2c1))**2)) / (float(s1c1 + s1c2) * float(s1c1 +
    s2c1) * float(s1c2 + s2c2) * float(s2c1 + s2c2))
    return statistic
