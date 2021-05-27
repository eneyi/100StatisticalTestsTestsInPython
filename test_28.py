# Test 28 Tukey test for multiple comparison of K population means (unequal sample sizes)

def tukeytest(Cvalue,s,N):
    statistic=((Cvalue*s)/sqrt(N))
    return statistic