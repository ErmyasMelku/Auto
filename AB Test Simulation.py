from scipy import stats

# Grouping data by 'A' and 'B'
group_A = df[df['Group'] == 'A']['Conversion']
group_B = df[df['Group'] == 'B']['Conversion']

# Perform a two-sample t-test
t_stat, p_value = stats.ttest_ind(group_A, group_B)

# Print results
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Check if the result is statistically significant at a 95% confidence level (alpha = 0.05)
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis - There is a significant difference between A and B.")
else:
    print("Fail to reject the null hypothesis - No significant difference between A and B.")
