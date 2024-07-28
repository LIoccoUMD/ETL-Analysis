# Data Science Gym Safety Project

## Project Overview

### Business Problem
Unsafe lifting practices in gyms pose risks to member safety, which can be mitigated by providing easily accessible, data-driven visualizations of proper exercise techniques categorized by difficulty and muscle group.

### Data Sets Used
- `megaGymDataset.csv`: Contains data on various exercises, including type, body part, equipment, difficulty level, rating, and description.
- `missing_ratings.csv`: Information on entried with missing data in the ratings column. (I think this will be removed)
- `dataset-metadata.json`: Metadata for the datasets.

### Techniques Employed
- **Mean Imputation**
- **Descriptive Analysis**: Summary statistics and visualizations to understand the distribution of exercise data.
- **Clustering Analysis**: K-Means clustering to group exercises based on type, body part, difficulty level, and rating.
- **Prescriptive analysis**: *WIP*

### Expected Outputs
- Descriptive and prescriptive analysis/visualizations in clear, readable files
- Summary statistics of the exercise dataset.
- Visualization of exercises grouped into clusters according to difficulty and rating

# Setup Instructions

## Cloning the Repository
Clone the repository to your local machine using the following command:  
`git clone` https://github.com/username/inst414-final-project-luciano-iocco.git  
Create a virtual environment and select the most recent version of Python. At this point in time the current version being worked with is 3.11.1. requirements.txt contains all of the dependencies needed to run this project.

# Code Package Structure

**data/**  
    ∙ *downloaded/* : Contains raw downloaded datasets.  
    ∙ *processed/* : Contains processed data files.  
**outputs/** 
    ∙ *descriptive_analysis.csv*: Output file for descriptive_analysis script.
    ∙ *prescriptive_analysis.csv*: Output file for prescriptive_analysis script.
    ∙ 
**analysis/**  
    ∙ *descriptive_analysis.py*: Script for performing descriptive analysis and clustering.  
    ∙ *prescriptive_analysis.py*: Script for performing prescriptive analysis  
**etl/**  
    ∙ *extract.py*: Script for extracting data.  
    ∙ *transform.py*: Script for transforming data.  
**vis/**  
    ∙ *visualizations.py*: Script for generating visualizations.
