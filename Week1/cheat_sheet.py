# Hypothesis Testing in Scipy

# One-Sample T-Test (Comparing a sample mean to a constant mean)
scipy.stats.ttest_1samp(dataset, known_mean(population), axis=0, nan_policy='propagate')

# Two-Sample Independent T-Test (Comparing the means of two independent samples)
scipy.stats.ttest_ind(a, b, axis=0, equal_var=True, nan_policy='propagate')

# Paired T-Test (Comparing the means of two related/dependent samples)
scipy.stats.ttest_rel(a, b, axis=0, nan_policy='propagate')