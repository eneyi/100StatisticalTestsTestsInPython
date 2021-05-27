# Test 44 The χ2-test for independence in a p × q table

def chitestind(obs):
    stat, p, dof, expected = chi2_contingency(obs)
    return stat
