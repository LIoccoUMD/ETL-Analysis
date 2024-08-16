import pandas as pd
import matplotlib.pyplot as plt
import logging

logging.basicConfig(filename='vis/visualizations.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to randomly select exercises based on safety rating ranges
def select_random_exercises(df):
    try:
        body_parts = df["BodyPart"].unique().tolist()
        body_part_options = ", ".join(body_parts)
        num_exercises = int(input("Enter the number of exercises you would like to see for each level: "))
        body_part = input(f"Enter the body part you're interested in. Possible values are {body_part_options} : ").strip()
        
        df_filter = df[df["BodyPart"].str.contains(body_part, case=False, na=False)]
        
        if df_filter.empty:
            raise ValueError(f"No exercises found for the body part '{body_part}'.")
        
        beginner_exercises = df_filter[(df_filter["Safety"] >= 0) & (df_filter["Safety"] <= 5)].sample(num_exercises)
        intermediate_exercises = df_filter[(df_filter["Safety"] > 5) & (df_filter["Safety"] <= 7.5)].sample(num_exercises)
        advanced_exercises = df_filter[(df_filter["Safety"] > 7.5) & (df_filter["Safety"] <= 10)].sample(num_exercises)
        
        exercises = {
            "Beginner": beginner_exercises["Title"].tolist(),
            "Intermediate": intermediate_exercises["Title"].tolist(),
            "Advanced": advanced_exercises["Title"].tolist()
        }
        
        logging.info("Successfully selected exercises for each difficulty.")
        
    except ValueError as e:
        logging.error(f"Error selecting exercises: {e}")
        raise
    
    return exercises

def create_visualization(exercises):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")

    ax.axis("off")
    difficulties = ["Beginner", "Intermediate", "Advanced"]
    colors = ["green", "orange", "red"]
    y_positions = [0.8, 0.5, 0.2]
    ax.set_aspect("equal")

    # Draw circles and text for each difficulty level
    for i, (difficulty, color) in enumerate(zip(difficulties, colors)):
        circle = plt.Circle((0.2, y_positions[i]), 0.13, color="none", ec=color, lw=2)
        ax.add_patch(circle)

        # Add difficulty text inside the circle with matching color
        ax.text(0.2, y_positions[i], difficulty, ha="center", va="center", fontsize=14, color=color, fontweight="bold")

        # List exercises associated with the difficulty, matching text color to the difficulty
        exercise_list = "\n".join(exercises[difficulty])
        ax.text(0.5, y_positions[i], exercise_list, ha="left", va="center", fontsize=12, color=color)

    fig.canvas.manager.set_window_title("Infographic")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("data/processed/processed_data.csv")
    exercises = select_random_exercises(df)
    create_visualization(exercises)
