import pandas as pd
import numpy as np
import logging
import os


logging.basicConfig(filename='log/transform.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load dataset
def load_data(file_path):
    """Loads the data from a CSV file with path file_path.
    
    Parameters:
        file_path (str): The path of the file containing the data to be read.
        
    Returns:
        pd.Dataframe: The data in the file as a dataframe.
    """
    logging.info(f"Loading data from {file_path}.")
    return pd.read_csv(file_path, index_col=0)

def encode_level(df):
    """
    Encode the "Level" column with numerical values.
    
    Parameters: df (pd.DataFrame): The DataFrame containing the data.
    
    Returns: pd.DataFrame: The DataFrame with the "Level" column encoded.
    """
    df["Level"] = df["Level"].map({"Beginner": 1.0, "Intermediate": 2.0, "Advanced": 3.0})
    logging.info("Encoding 'Level' column with numerical values.")
    return df

def fill_missing_rating(row, mean_ratings_by_level):
    """Fill missing "Rating" values based on the mean rating for each Level.

    Parameters:
        row (pd.Series): A row of the DataFrame
        mean_ratings_by_level (pd.Series): The mean rating for each level.

    Returns:
        float: The filled Rating value.
    """
    try:
        if pd.isna(row["Rating"]):
            logging.info("Missing 'rating' values filled.")
            return mean_ratings_by_level[row["Level"]]
        else:
            return row["Rating"]
    except Exception as e:
        logging.error(f"Error filling missing rating for {row.name}: {e}", exc_info=True)
        raise

def handle_missing_values(df, equipment_updates):
    """ Fill missing values in the DataFrame. [WIP: Updates to be moved to reference_table]
    
    Parameters: df (pd.DataFrame): The DataFrame containing the data.
    equipment_updates (pd.DataFrame): DataFrame containing the equipment updates.
    
    Returns: pd.DataFrame: The DataFrame with missing values filled in.
    """
    logging.info("Handling missing values in the DataFrame.")
    
    # Calculate the mean rating for each level where rating is not NaN
    mean_ratings_by_level = df.groupby("Level")["Rating"].mean()
    df["Rating"] = df.apply(fill_missing_rating, axis=1, args=(mean_ratings_by_level,))

    updates = {
        637: "Bench", 638: "Bench", 639: "Rod", 699: "None", 912: "Roller", 914: "Wall",
        1207: "None", 1402: "None", 1403: "Band", 1404: "None", 1405: "Seat", 1406: "None",
        1407: "None", 1531: "None", 1532: "Seat", 1533: "None", 1624: "None", 1625: "None",
        1626: "None", 1627: "None", 1780: "Rod", 2418: "None", 2419: "Seat", 2420: "None",
        2421: "Dumbbell", 2422: "Smith machine", 2423: "None", 2763: "None", 2764: "None",
        2765: "None"
    }

    # Apply updates to df
    for index, equipment in equipment_updates.itertuples(index=False):
        df.loc[index, "Equipment"] = equipment

    
    df.loc[(df['Level'].isna()) & (df['Rating'] >= 0) & (df['Rating'] <= 4.9), 'Level'] = 'Beginner'
    df.loc[(df['Level'].isna()) & (df['Rating'] >= 5.0) & (df['Rating'] <= 7.4), 'Level'] = 'Intermediate'
    df.loc[(df['Level'].isna()) & (df['Rating'] > 7.4), 'Level'] = 'Advanced'
    df = encode_level(df)
    
    min_max_by_level = df.groupby('Level')['Rating'].agg(["min", "max"]).reset_index()
    min_max_by_level.columns = ['Level', 'MinRating', 'MaxRating']
    df = df.merge(min_max_by_level, on='Level', how='left')

    df["Rating"] = df.apply(
        lambda row: np.random.uniform(row['MinRating'], row['MaxRating']) if pd.isna(row['Rating']) else row['Rating'],
        axis=1
    )

    # Drop the temporary min and max columns
    df.drop(columns=['MinRating', 'MaxRating'], inplace=True)
    logging.info("Temporary columns dropped.")
    logging.info("Missing values handled successfully.")
    return df

body_part_factors = {
    "Abdominals": 1.0, "Adductors": 1.1, "Abductors": 1.1, "Biceps": 1.1,
    "Calves": 1.2, "Chest": 1.3, "Forearms": 1.0, "Glutes": 1.0, "Hamstrings": 1.1,
    "Lats": 1.3, "Lower Back": 1.4, "Middle Back": 1.3, "Traps": 1.1, "Neck": 1.5,
    "Quadriceps": 1.1, "Shoulders": 1.3, "Triceps": 1.2
}

equipment_factors = {
    "Bands": 1.0, "Barbell": 1.2, "Kettlebells": 1.1, "Dumbbell": 1.0, "Other": 1.0,
    "Cable": 1.1, "Machine": 1.0, "Body Only": 1.0, "Medicine Ball": 1.1, "Bench": 1.2,
    "Rod": 1.1, "E-Z Curl Bar": 1.0, "Roller": 1.0, "Wall": 1.0 
}

def calculate_safety(df, equipment_updates):
    """
    Calculate the safety score for each exercise in the DataFrame.
    
    Parameters: df (pd.DataFrame): The DataFrame containing the data.
    equipment_updates (pd.DataFrame): DataFrame containing the equipment updates.
    
    Returns: pd.DataFrame: The DataFrame with the calculate Safety scores in a new column.
    """
    df = handle_missing_values(df, equipment_updates)
    df["BodyPart_Factor"] = df["BodyPart"].map(body_part_factors)
    df["Equipment_Factor"] = df["Equipment"].map(equipment_factors)
    df["Safety"] = ((10 - df["Level"]) / 10) * df["Rating"] * df["BodyPart_Factor"] * df["Equipment_Factor"]
    return df

def transform_data(input_file, output_file, equipment_updates_file):
    """
    Transform the data by loading, processing, and calculating safety scores. This data is then saved to a CSV file.
    
    Parameters: input_file (str): The path to the input CSV file.
    output_file: (str) The path to the output CSV file.
    equipment_updates_file (str): The path to the equipment updates CSV file.
    
    Returns: None
    """
    df = load_data(input_file)
    equipment_updates = pd.read_csv(equipment_updates_file)
    df = calculate_safety(df, equipment_updates)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"Transformed data saved to {output_file}")

if __name__ == "__main__":
    transform_data("data/extracted/megaGymDataset.csv", "data/processed/processed_data.csv", "data/reference-tables/equipment_updates.csv")
