# Test 52 The Wilcoxon–Mann–Whitney rank sum test of two populations
def ranksums(x, y):
    x, y = map(np.asarray, (x, y))
    n1 = len(x)
    n2 = len(y)
    alldata = np.concatenate((x, y))
    ranked = rankdata(alldata)
    x = ranked[:n1]
    y = ranked[:n2]
    sx = np.sum(x, axis=0)
    sy = np.sum(y, axis=0)
    R=min(sx,sy)
    N=len(x)+len(y)
    n=len(x)
    Rprime=n*(N+1)-R
    return Rprime