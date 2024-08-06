import os
# placeholder main function
def main():
    return 1

# only execute when the script is run directly
if __name__ == "__main__":
    main()

# Step 1: Extract Data
print("Running Extract Step")
os.system("python etl/extract.py")

# Step 2: Transform Data
print("Running Transform Step")
os.system("python etl/transform.py")

# Step 3: Evaluate Model
print("Running Evaluation")
os.system("python analysis/descriptive_analysis.py")
os.system("python analysis/prescriptive_analysis.py")

# Step 4: Generate Visualizations
print("Running Visualization")
os.system("python vis/visualizations.py")

print("Finished running.")
