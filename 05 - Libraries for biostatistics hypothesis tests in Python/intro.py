# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 10:47:38 2025

@author: natha
@version 1.00
"""
from scipy import stats
# sample data
data1 = [1, 2, 3, 4]
data2 = [5, 6, 7, 8]

# perform t-test
t_statistic, p_value = stats.ttest_ind(data1, data2)

# print result
print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")

# chi-square test
from scipy.stats import chisquare

# sample data 
observed = [10, 20]
expected = [15, 15]

# perform chi-square test
chi2_statistic, p_value = chisquare(observed, f_exp=expected)

# print result
print(f"chi-2-statistic: {chi2_statistic}")
print(f"p-value: {p_value}")
















