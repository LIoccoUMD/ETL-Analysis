import pandas as pd

# Load the processed data
data_path = "data/processed/processed_data.csv"
df = pd.read_csv(data_path)

# Perform prescriptive analytics

# Save prescriptive analysis as CSV
output_file = "data/outputs/prescriptive_analysis.csv"
df.to_csv(output_file)
print("Prescriptive analysis saved.")
