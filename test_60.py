# Test 60 Friedman’s test for multiple treatment of a series of subjects

# compare samples
stat, p = friedmanchisquare(data1, data2, data3, data4)
print('Statistics=%.3f, p=%.3f' % (stat, p))
