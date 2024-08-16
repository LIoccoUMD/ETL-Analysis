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

def knearest(df):
    """ Performs K-Nearest Neighbors with the optimal number of neighbors calculated by a GridSearch and evaluated with negative mean squared error.
    Plots the actual vs. predicted safety values.
    
    Parameters: df: The DataFrame containing the data.
    
    Returns: None
    """
    x = df.drop(columns=["Desc", "RatingDesc", "Title", "Type", "Equipment", "BodyPart", "Safety"])
    y = df["Safety"]
    df = df.dropna()
    
    imputer = SimpleImputer(strategy="mean")
    imputer_y = SimpleImputer(strategy="mean")
    
    x = imputer.fit_transform(x)
    y = imputer_y.fit_transform(y.values.reshape(-1, 1)).ravel()
    
    # Calculate optimal k_value
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
    
    y_min = min(y_test.min(), y_pred.min())
    y_max = max(y_test.max(), y_pred.max())
    
    
    # Plotly graph
    fig = px.scatter(x=y_test, y=y_pred, labels={"x": "Actual Safety", "y": "Predicted Safety"}, title="Actual vs Predicted Safety", 
                     color=y_test, trendline="ols", trendline_color_override="darkviolet",
                     color_continuous_scale=px.colors.sequential.algae)
    fig.update_traces(marker=dict(size=10, line=dict(width=0.5, color="black")), selector=dict(mode="markers"))
    fig.update_layout(template="presentation", plot_bgcolor="white", paper_bgcolor="white",
                      xaxis=dict(range=[y_min,y_max]),
                      yaxis=dict(range=[y_min,y_max]))
    fig.show()   

def save_summary_statistics(df):
    """Save the summary statistics of the parameter df to a CSV file.
    Parameters: df: The DataFrame for which to save summary statistics.
    
    Returns: None
    """
    output_file = "data/outputs/descriptive_analysis.csv"
    df.to_csv(output_file)
    print("Descriptive analysis saved.")

if __name__ == "__main__":
    save_summary_statistics(df)
    knearest(df)
    df.to_csv("data/outputs/descriptive_analysis.csv", index=False)
    print("Descriptive analysis and KNN regression completed.")