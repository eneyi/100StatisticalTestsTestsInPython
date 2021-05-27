# Test 49 The Wilcoxon inversion test (U-test) 

def wilcotest(data1,data2):
    stat, pval=mannwhitneyu(data1, data2)
    return stat