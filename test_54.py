# Test 54 The Kruskall–Wallis rank sum test of K populations (H-test)



def KruskallWallis(*args):
    output = argstoarray(*args)
    ranks = ma.masked_equal(rankdata(output, use_missing=False), 0)
    sumrk = ranks.sum(-1)
    ngrp = ranks.count(-1)
    ntot = ranks.count()
    H = 12./(ntot*(ntot+1)) * (sumrk**2/ngrp).sum() - 3*(ntot+1)
    # Tie correction
    ties = count_tied_groups(ranks)
    T = 1. - sum(v*(k**3-k) for (k,v) in ties.items())/float(ntot**3-ntot)
    if T == 0:
        raise ValueError('All numbers are identical in kruskal')

    H /= T
    df = len(output) - 1
    #prob = distributions.chi2.sf(H, df)
    return H

