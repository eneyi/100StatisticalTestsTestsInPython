# Test 39 Fisher’s exact test for consistency in a 2 × 2 table

import scipy.stats as stats
oddsratio, pvalue = stats.fisher_exact([[8, 2], [1, 5]])
pvalue
