import pandas as pd
import numpy as np

# Assuming your existing DataFrame is called 'df'
df = pd.read_csv('Trim_Fraud.csv')

# Generate user IDs (user_1 to user_100) repeated enough times to cover all rows
users_needed = 83213  # total number of rows
user_ids = [f'user_{i}' for i in range(1, 101)]  # creates list ['user_1', 'user_2', ..., 'user_100']

# Calculate how many complete sets of users we need
complete_sets = users_needed // 100 + 1

# Create the full list of user IDs repeated enough times and then truncate to exact length needed
full_user_list = (user_ids * complete_sets)[:users_needed]

# Randomly shuffle the user IDs
shuffled_user_ids = np.random.permutation(full_user_list)

# Add the new column to the DataFrame
df['user_id'] = shuffled_user_ids

# Verify the results
print("\nShape of DataFrame:", df.shape)  # Should show (83213, 12)
print("\nNumber of unique user IDs:", df['user_id'].nunique())  # Should show 100
print("\nSample of first few rows:")
print(df.head())

# Optional: check distribution of user assignments
user_distribution = df['user_id'].value_counts()
print("\nDistribution of users (first few):")
print(user_distribution.head())

# Save the updated DataFrame if needed
df.to_csv('txn_mapped.csv', index=False)