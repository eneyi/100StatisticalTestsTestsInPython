# Test 53 The Siegel–Tukey rank sum dispersion test of two variances

def SiegelTukey(n1,n2):
    statistics=(min(sum(n1),sum(n2))-len(n1)*(len(n1)+len(n2)+1)/2+1/2)/sqrt(len(n1)*len(n2)*(len(n1)+len(n2)+1)/12)
    return statistics