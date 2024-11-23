import pandas as pd

# Load the dataset
data=pd.read_csv("C:\MY\Work\Projects\Fraud Detection System\Fraud.csv")

# Shuffle the rows randomly
data = data.sample(frac=1, random_state=42)  # Consistent shuffling for reproducibility

# Separate data based on isFraud values
data_0 = data[data["isFraud"] == 0]
data_1 = data[data["isFraud"] == 1]

# Select the desired proportions
data_0 = data_0.iloc[:75000, :]  # 75% of 0 values
data_1 = data_1.iloc[:25000, :]  # 25% of 1 values

# Combine the selected data
new_data = pd.concat([data_0, data_1], ignore_index=True)

# Shuffle the combined dataset again for randomness
new_data = new_data.sample(frac=1, random_state=42)

# Save the new dataset to a CSV file
new_data.to_csv("new_dataset.csv", index=False)

