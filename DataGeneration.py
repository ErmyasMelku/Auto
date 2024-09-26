import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Number of users for each version
n_users = 1000

# Simulate conversion rates for the control (A) and test (B) groups
conversion_rate_A = 0.3  # 30% conversion for A
conversion_rate_B = 0.35  # 35% conversion for B

# Generate random data for users in group A (control)
data_A = np.random.binomial(1, conversion_rate_A, n_users)

# Generate random data for users in group B (test)
data_B = np.random.binomial(1, conversion_rate_B, n_users)

# Create a DataFrame
df = pd.DataFrame({
    'UserID': np.arange(1, 2*n_users + 1),
    'Group': ['A']*n_users + ['B']*n_users,
    'Conversion': np.concatenate([data_A, data_B])
})

# Save to a CSV file for the project
df.to_csv('ab_test_data.csv', index=False)

print(df.head())
