import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
import plotly.express as px
import matplotlib.pyplot as plt

# Rename this file


# Load the processed data
df = pd.read_csv("data/processed/processed_data.csv")

# Display descriptive statistics
def summary_statistics(df):
    df.info()  
    df = df.describe()
    return df

# K-means - to be put inside of a function later
def knearest(df):
    x = df.drop(columns=["Desc", "RatingDesc", "Title", "Type", "Equipment", "BodyPart", "Safety"])
    y = df["Safety"]
    df = df.dropna()
    
    imputer = SimpleImputer(strategy="mean")
    imputer_y = SimpleImputer(strategy='mean')
    
    x = imputer.fit_transform(x)
    y = imputer_y.fit_transform(y.values.reshape(-1, 1)).ravel()
    
    param_grid = {"n_neighbors": range(1,15)}
    knn = KNeighborsRegressor()
    grid_search = GridSearchCV(knn, param_grid, cv=5, scoring="neg_mean_squared_error")
    grid_search.fit(x,y)
    optimal_k = grid_search.best_params_["n_neighbors"]
    print("Best parameters found: ", grid_search.best_params_)
    
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)
    knn_regressor = KNeighborsRegressor(optimal_k)
    knn_regressor.fit(X_train,y_train)
    y_pred = knn_regressor.predict(X_test)
    knn_mse = mean_squared_error(y_test, y_pred)
    print("K-Nearest Neighbor")
    print("MeanSquaredError [MSE]:", knn_mse)
    
    # Graph using plotly
    fig = px.scatter(x=y_test, y=y_pred, labels={'x': 'Actual Safety', 'y': 'Predicted Safety'}, title="Actual vs Predicted Safety", 
                     color=y_test,
                     color_continuous_scale=px.colors.sequential.algae)
    fig.update_traces(marker=dict(size=10, line=dict(width=0.5, color='darkviolet')), selector=dict(mode='markers'))
    fig.update_layout(template="presentation", plot_bgcolor="white", paper_bgcolor="white",
                      xaxis=dict(range=[min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]),
                      yaxis=dict(range=[min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]))  # Change theme
    fig.show()   

# knearest(df)


# Save the summary statistics
def save_summary_statistics(df):
    output_file = "data/outputs/descriptive_analysis.csv"
    df.to_csv(output_file)
    print("Descriptive analysis saved.")

if __name__ == "__main__":
    save_summary_statistics(df)
    knearest(df)
    df.to_csv("data/outputs/descriptive_analysis.csv", index=False)
    print("Descriptive analysis and KNN regression completed.")