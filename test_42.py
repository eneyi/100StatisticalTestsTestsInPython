# Test 42 The Cochran test for consistency in an n × K table of dichotomous data



def cochranstest(x, return_object=True):
    x = np.asarray(x, dtype=np.float64)
    gruni = np.unique(x)
    N, k = x.shape
    count_row_success = (x == gruni[-1]).sum(1, float)
    count_col_success = (x == gruni[-1]).sum(0, float)
    count_row_ss = count_row_success.sum()
    count_col_ss = count_col_success.sum()
    assert count_row_ss == count_col_ss  
    q_stat = ((k-1) * (k * np.sum(count_col_success**2) - count_col_ss**2)
              / (k * count_row_ss - np.sum(count_row_success**2)))

    df = k - 1
    pvalue = stats.chi2.sf(q_stat, df)


    return q_stat

