import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import plotly.express as px

# Load the processed data
data_path = "data/processed/processed_data.csv"
df = pd.read_csv(data_path)

# Perform descriptive statistics
def summary_statistics(df):
    df.info()  
    df = df.describe()
    return df

# Encodes categorical features into numerical data
def encode_features(df, columns):
    le = LabelEncoder()
    for column in columns:
        df[column] = le.fit_transform(df[column])
    return df

categorical_columns = ['Type', 'BodyPart', 'Level']  # Replace with actual categorical column names
df = encode_features(df, categorical_columns)

# K-means - to be put inside of a function later
features = df[["Type", "BodyPart", "Level", "Rating"]]
kmeans = KMeans(n_clusters=4)
df["cluster"] = kmeans.fit_predict(features)

fig = px.scatter(df, x="Level", y="BodyPart", color="cluster", title="Exercise Clusters")
fig.show()


# Save the summary statistics
output_file = "data/outputs/descriptive_analysis.csv"
# df.to_csv(output_file)
df.to_csv(output_file)
print("Descriptive analysis saved.")

