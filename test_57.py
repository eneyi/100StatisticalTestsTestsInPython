# Test 57 F-test for testing main effects and interaction effects in a two-way classification 
model = ols('III ~ I + II + I:II', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
anova_table