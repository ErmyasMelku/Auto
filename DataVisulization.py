import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")

# Plot conversion rates for both groups
conversion_rates = df.groupby('Group')['Conversion'].mean()

# Bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x=conversion_rates.index, y=conversion_rates.values)
plt.title('Conversion Rates for A/B Test', fontsize=16)
plt.ylabel('Conversion Rate', fontsize=12)
plt.xlabel('Group', fontsize=12)
plt.ylim(0, 0.4)
plt.show()
