import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Read the original CSV
df = pd.read_csv('synthetic_clickstream.csv')

# Define simplified event types
simplified_events = ['Mouse Click', 'Key Press', 'Scroll Up', 'Scroll Down']

# Create random mapping
unique_events = df['event_type'].unique()
event_mapping = {event: random.choice(simplified_events) for event in unique_events}

# Transform the data
df['event_type'] = df['event_type'].map(event_mapping)

# Save the transformed dataset
df.to_csv('transformed_clickstream.csv', index=False)

# Print the mapping and distribution
print("Event type mapping:")
for old, new in event_mapping.items():
    print(f"{old} -> {new}")

print("\nNew event type distribution:")
print(df['event_type'].value_counts())