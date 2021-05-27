# Test 55 The rank sum difference test for the multiple comparison of K population means

def ranksums(x, y, z):
    x, y, z = map(np.asarray, (x, y, z))
    n1 = len(x)
    n2 = len(y)
    n3 = len(z)
    alldata = np.concatenate((x, y, z))
    ranked = rankdata(alldata)
    x = ranked[:n1]
    y = ranked[:n2]
    z = ranked[:n3]
    sx = np.sum(x, axis=0)
    sy = np.sum(y, axis=0)
    sz = np.sum(z, axis=0)
    return sx,sy,sz
