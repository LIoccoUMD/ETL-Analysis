import kaggle

# Place json file in .kaggle user folder
kaggle.api.authenticate()

# Download dataset to specified path and unzip
kaggle.api.dataset_download_files("niharika41298/gym-exercise-data", path='data\downloaded', unzip=True)

kaggle.api.dataset_metadata("niharika41298/gym-exercise-data", path="data\downloaded")