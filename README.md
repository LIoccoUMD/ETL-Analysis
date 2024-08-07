# Gym Safety ETL and Analysis

## Project Overview

This project involves extracting, transforming, and analyzing a dataset of gym exercises. The analysis includes calculating safety scores for exercises, evaluating models, and generating visualizations. The process is automated through a series of Python scripts.

### Business Problem
Unsafe lifting practices in gyms pose risks to member safety, which can be mitigated by providing easily accessible, data-driven visualizations of proper exercise techniques categorized by difficulty and muscle group.

### Data Sets Used
- `megaGymDataset.csv`: Contains data on various exercises, including type, body part, equipment, difficulty level, rating, and description.
- `missing_ratings.csv`: Information on entried with missing data in the ratings column.
- `dataset-metadata.json`: Metadata for the datasets.

### Techniques Employed
- **Mean Imputation**: Handling missing values by imputing the mean rating for each exercise level.  
- **Encoding Categorical Variables**  
- **K-Nearest Neighbor to predict safety scores**  
    - GridSearchCV to find the optimal number of neighbors

### Expected Outputs
- Descriptive and prescriptive analysis/visualizations in clear, readable files
- Summary statistics of the exercise dataset.
- Visualization of exercises grouped into clusters
- Recommendations of exercises based on their difficulty.

# Setup Instructions

## Cloning the Repository
Clone the repository to your local machine using the following command:  
`git clone https://github.com/username/inst414-final-project-luciano-iocco.git`  
Create a virtual environment and select the most recent version of Python. The current working Python version is 3.11.1. requirements.txt contains all of the dependencies   needed to run this project. Install the required packages using `python -m pip install -r requirements.txt`  
Run the main script to execute the ETL process and analysis (effectively run the entire program) `python main.py`

## Logging

Logging is configured to write to "gym_project.log". The log includes detailed information about each step of the process, including any errors that occur along with 
their time, level, and a message.

# Code Package Structure

∙ gym_project.log: Contains logging information recorded during runtime.  
**data/**  
    ∙ *downloaded/* : Contains raw downloaded datasets.  
    ∙ *processed/* : Contains processed data files.  
**outputs/**  
    ∙ *descriptive_analysis.csv*: Output file for descriptive_analysis script.  
    ∙ *prescriptive_analysis.csv*: Output file for prescriptive_analysis script.  
**analysis/**  
    ∙ *descriptive_analysis.py*: Performs descriptive statistical analysis.    
    ∙ *prescriptive_analysis.py*: Evaluates models and provides recommendations. (WIP -- currently all done in descriptive_analysis.py)  
**etl/**  
    ∙ *extract.py*: Loads the raw dataset in a DataFrame  
    ∙ *transform.py*: Processes the raw data, handles missing values and calculates safety scores for exercises.  
**vis/**  
    ∙ *visualizations.py*: Generates visualizations to help understand the data and results.  

