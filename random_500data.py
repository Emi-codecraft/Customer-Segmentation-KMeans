import pandas as pd
import random

# Number of customers
num_customers = 500  

# Generate random customer data
data = {
    "CustomerID": range(1, num_customers + 1),
    "Gender": [random.choice(["Male", "Female"]) for _ in range(num_customers)],
    "Age": [random.randint(18, 70) for _ in range(num_customers)],
    "Annual Income (k$)": [random.randint(15, 150) for _ in range(num_customers)],
    "Spending Score (1-100)": [random.randint(1, 100) for _ in range(num_customers)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save as CSV
csv_filename = "customers.csv"
df.to_csv(csv_filename, index=False)

print(f"CSV file '{csv_filename}' with {num_customers} records has been generated successfully! 🚀")
