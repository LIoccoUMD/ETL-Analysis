import pandas as pd
import logging

logging.basicConfig(filename="analysis/prescriptive_analysis.log", level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting prescriptive analysis.")

# Load the processed data
data_path = "data/processed/processed_data.csv"
logging.info(f"Loading processed data from {data_path}.")
df = pd.read_csv(data_path)

# Perform prescriptive analytics


# Save prescriptive analysis as CSV
output_file = "data/outputs/prescriptive_analysis.csv"
df.to_csv(output_file)
print("Prescriptive analysis saved.")
