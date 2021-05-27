# Test 31 Bartlett’s test for equality of K variances

def Bartlettstest(group_n,group_variance):
    pool_var = 1 / (np.sum((group_n - 1))) * np.sum((group_n - 1) * group_variance)
    x2_num = np.sum(group_n - 1) * np.log(pool_var) - np.sum((group_n - 1) * np.log(group_variance))
    x2_den = 1 + 1 / (3 * (k + 1)) * (np.sum(1 / (group_n - 1)) - 1 / (np.sum(group_n-1)))
    x2 = x2_num / x2_den
    return x2