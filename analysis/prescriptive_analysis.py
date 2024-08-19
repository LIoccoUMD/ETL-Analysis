import pandas as pd
import logging
import os

logging.basicConfig(filename="log/prescriptive_analysis.log", level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting prescriptive analysis.")

# Load the processed data
data_path = "data/processed/processed_data.csv"
logging.info(f"Loading processed data from {data_path}.")
df = pd.read_csv(data_path)

# Save prescriptive analysis as CSV
output_file = "data/outputs/prescriptive_analysis.csv"
os.makedirs(os.path.dirname(output_file), exist_ok=True)
df.to_csv(output_file)
print("Prescriptive analysis saved.")
