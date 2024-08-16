import os
import logging

# Set up logging
logging.basicConfig(
    filename='log/gym_project.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

def run_step(step_name, script_path):
    """
    Runs a step in the ETL process and logs the outcome.

    Parameters:
        step_name (str): The name of the step being run.
        script_path (str): The path to the script to execute for this step.

    Returns:
        None
    """
    try:
        logging.info(f"Running {step_name} step")
        print(f"Running {step_name} step")
        os.system(f"python {script_path}")
        logging.info(f"{step_name} step completed successfully")
    except Exception as e:
        logging.error(f"Error during {step_name} step: {e}", exc_info=True)
        print(f"Error during {step_name} step: {e}")

if __name__ == "__main__":
    # Step 1: Extract Data
    run_step("Extract", "etl/extract.py")

    # Step 2: Transform Data
    run_step("Transform", "etl/transform.py")

    # Step 3: Evaluate Model
    run_step("Prescriptive Analysis", "analysis/prescriptive_analysis.py")
    run_step("KNN Model", "analysis/knn_regression_and_summary.py")

    # Step 4: Generate Visualizations
    run_step("Visualization", "vis/visualizations.py")

    logging.info("Finished running all steps.")
    print("Finished running.")
