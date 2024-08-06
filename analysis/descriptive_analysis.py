import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
import numpy as np

# Rename this file


# Load the processed data
df = pd.read_csv("data/processed/processed_data.csv")

# Display descriptive statistics
def summary_statistics(df):
    df.info()  
    df = df.describe()
    return df

# Transforms beginner, intermediate, advanced into numerical data, 1, 2, and 3 respectively
def encode_level(df):
    df["Level"] = df["Level"].map({"Beginner": 1.0, "Intermediate": 2.0, "Advanced": 3.0})
    return df

def handle_missing_values(df):
    df.loc[(df['Level'].isna()) & (df['Rating'] >= 0) & (df['Rating'] <= 4.9), 'Level'] = 'Beginner'
    df.loc[(df['Level'].isna()) & (df['Rating'] >= 5.0) & (df['Rating'] <= 7.4), 'Level'] = 'Intermediate'
    df.loc[(df['Level'].isna()) & (df['Rating'] > 7.4), 'Level'] = 'Advanced'
    df = encode_level(df)
    # Calculate min and max rating for each level
    min_max_by_level = df.groupby('Level')['Rating'].agg(["min", "max"]).reset_index()
    min_max_by_level.columns = ['Level', 'MinRating', 'MaxRating']

    # Merge the min and max values back to the original dataframe
    df = df.merge(min_max_by_level, on='Level', how='left')

    # Fill missing values with random values within the min-max range
    df["Rating"] = df.apply(
        lambda row: np.random.uniform(row['MinRating'], row['MaxRating']) if pd.isna(row['Rating']) else row['Rating'],
        axis=1
    )
    
    # Drop the temporary min and max columns
    df.drop(columns=['MinRating', 'MaxRating'], inplace=True)
    # Remove any remaining NA values
    print(df["BodyPart"].unique())
    # df.dropna(axis=0,how="any", inplace=True)
    return df

handle_missing_values(df)

# K-means - to be put inside of a function later
def kmeans(df):
    df = handle_missing_values(df)
    x = df.drop(columns=["Desc", "RatingDesc", "Title", "Type", "Equipment"])


# Save the summary statistics
output_file = "data/outputs/descriptive_analysis.csv"
# df.to_csv(output_file)
df.to_csv(output_file)
print("Descriptive analysis saved.")


# kmeans(df)