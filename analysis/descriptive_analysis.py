import pandas as pd
import plotly

# Load the processed data
data_path = 'data/processed/processed_data.csv'
df = pd.read_csv(data_path)

# Perform descriptive statistics
def summary_statistics(df):
    df.info()  
    print(df.describe())
    return

def plot (df, columns, output_dir):
    return






# Save the summary statistics
output_file = 'data/outputs/descriptive_analysis.csv'
# df.to_csv(output_file)
df.to_csv(output_file)
print("Descriptive analysis saved.")

