import pandas as pd

# Load the processed data
data_path = 'data/processed/processed_data.csv'
df = pd.read_csv(data_path)

# Perform descriptive statistics
df = df.describe()

# Save the summary statistics
output_file = 'data/outputs/summary_statistics.csv'
# df.to_csv(output_file)
df.to_csv(output_file)
print("Descriptive analysis saved.")
