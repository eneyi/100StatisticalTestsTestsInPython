# Test 56 The rank sum maximum test for the largest K population means 

def rankmax(*args):
    output = argstoarray(*args)
    ranks = ma.masked_equal(rankdata(output), 0)
    sumrk = ranks.sum(-1)
    return sumrk