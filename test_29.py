# Test 29 The Link–Wallace test for multiple comparison of K population means (equal sample sizes)

def linkwallacetest(wmean1,wmean2,wmean3,Ovmean,n):
    statistic=(n*Ovmean)/(wmean1+wmean2+wmean3)
    return statistic