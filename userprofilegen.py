import pandas as pd
import numpy as np
import random
import string
from datetime import datetime, timedelta

class UserDataGenerator:
    def __init__(self):
        self.valid_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'aol.com']
        self.spam_domains = ['tempmail.com', 'fakeemail.net', 'disposable.cc', 'throwaway.com', 'spam.xyz']
        self.carriers = ['Airtel', 'Verizon', 'T-Mobile', 'AT&T', 'Vodafone', 'Sprint']
        self.first_names = ['John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia', 'James', 'Ava', 'Alexander', 'Isabella']
        self.last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']

    def generate_user_id(self):
        """Generate a random user ID"""
        letters = ''.join(random.choices(string.ascii_lowercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=4))
        return f"{letters}{numbers}"

    def generate_name(self):
        """Generate a random full name"""
        return f"{random.choice(self.first_names)} {random.choice(self.last_names)}"

    def generate_age(self):
        """Generate a random age between 18 and 80"""
        return random.randint(18, 80)

    def generate_email_data(self, is_valid=True):
        """Generate email-related data"""
        if is_valid:
            domain = random.choice(self.valid_domains)
            domain_validation = True
        else:
            domain = random.choice(self.spam_domains)
            domain_validation = random.choice([True, False])

        name = ''.join(random.choices(string.ascii_lowercase, k=8))
        email_id = f"{name}@{domain}"
        
        return {
            "id": email_id,
            "domain": domain.split('.')[0],
            "breach_history": random.randint(0, 5),
            "isValid": is_valid,
            "domainValidation": domain_validation if not is_valid else True,
            "Microsoft": random.choice([True, False]),
            "LinkedIn": random.choice([True, False]),
            "Meta": random.choice([True, False]),
            "DisposableId": not is_valid,
            "emailAge": random.randint(1, 10)
        }

    def generate_phone_data(self):
        """Generate phone-related data"""
        return {
            "number": ''.join(random.choices(string.digits, k=10)),
            "carrier": random.choice(self.carriers),
            "disposableSim": random.choice([True, False]),
            "phoneAge": random.randint(1, 5)
        }

    def generate_user(self):
        """Generate a complete user record"""
        is_valid = random.random() < 0.8  # 80% valid emails
        
        user_data = {
            "user_id": self.generate_user_id(),
            "name": self.generate_name(),
            "age": self.generate_age(),
            "email": self.generate_email_data(is_valid),
            "phone": self.generate_phone_data()
        }
        
        return user_data

    def generate_dataset(self, num_users=100):
        """Generate multiple user records"""
        users = []
        for _ in range(num_users):
            users.append(self.generate_user())
        return users

def flatten_json(nested_json):
    """Flatten nested JSON structure for DataFrame creation"""
    flat_data = {}
    
    def flatten(x, prefix=''):
        if isinstance(x, dict):
            for k, v in x.items():
                if isinstance(v, dict):
                    flatten(v, f"{prefix}{k}_")
                else:
                    flat_data[f"{prefix}{k}"] = v
        
    flatten(nested_json)
    return flat_data

# Generate the dataset
generator = UserDataGenerator()
users = generator.generate_dataset(100)

# Flatten and convert to DataFrame
flat_users = [flatten_json(user) for user in users]
df = pd.DataFrame(flat_users)

# Validate constraints
assert all(df[df['email_isValid'] == True]['email_domainValidation'] == True), \
    "Constraint violation: isValid=True must have domainValidation=True"

# Print some statistics
print("\nDataset Statistics:")
print(f"Total users: {len(df)}")
print("\nEmail validity distribution:")
print(df['email_isValid'].value_counts(normalize=True))
print("\nDomain distribution:")
print(df['email_domain'].value_counts())
print("\nCarrier distribution:")
print(df['phone_carrier'].value_counts())

# Save to CSV
df.to_csv('synthetic_user_data.csv', index=False)
print("\nData saved to 'synthetic_user_data.csv'")

# Display first few records
print("\nSample Records:")
print(df.head(2).to_string())