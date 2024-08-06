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
    print(df["Equipment"].unique())
    # df.dropna(axis=0,how="any", inplace=True)
    return df

body_part_factors = {
    "Abdominals": 1.0,
    "Adductors": 1.1,
    "Abductors": 1.1,
    "Biceps": 1.1,
    "Calves": 1.2,
    "Chest": 1.3,
    "Forearms": 1.0,
    "Glutes": 1.0,
    "Hamstrings": 1.1,
    "Lats": 1.3,
    "Lower Back": 1.4,
    "Middle Back": 1.3,
    "Traps": 1.1,
    "Neck": 1.5,
    "Quadriceps": 1.1,
    "Shoulders": 1.3,
    "Triceps": 1.2
}

equipment_factors = {
    "Bands": 1.0,
    "Barbell": 1.2,
    "Kettlebells": 1.1,
    "Dumbbell": 1.0,
    "Other": 1.0,
    "Cable": 1.1,
    "Machine": 1.0,
    "Body Only": 1.0,
    "Medicine Ball": 1.1,
    "Bench": 1.2,
    "Rod": 1.1,
    "E-Z Curl Bar": 1.0,
    "Roller": 1.0,
    "Wall": 1.0 
}

def calculate_safety(df):
    df = handle_missing_values(df)
    df["BodyPart_Factor"] = df["BodyPart"].map(body_part_factors)
    df["Equipment_Factor"] = df["Equipment"].map(equipment_factors)
    df["Safety"] = ((10 - df["Level"]) / 10) * df["Rating"] * df["BodyPart_Factor"] * df["Equipment_Factor"]
    print(df.head())
    return df

df = calculate_safety(df)



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