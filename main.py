import pandas as pd

def generate_plan():
    # Load the dataset
    try:
        df = pd.read_csv('fitness_data.csv')
    except FileNotFoundError:
        print("Error: fitness_data.csv not found!")
        return

    print("--- AI Personalized Workout & Diet Planner ---")
    
    # User Inputs
    goal = input("Enter your goal (Weight Loss/Muscle Gain/Maintenance): ")
    diet_pref = input("Dietary Preference (Vegetarian/Non-Vegetarian): ")
    budget = input("Budget Level (Low/Medium): ")

    # AI Filtering Logic
    diet_plan = df[(df['Type'] == 'Diet') & 
                   (df['Goal'] == goal) & 
                   (df['Constraint'] == diet_pref) & 
                   (df['Budget'] == budget)]

    workout_plan = df[(df['Type'] == 'Workout') & 
                      (df['Goal'] == goal) & 
                      (df['Budget'] == budget)]

    # Output Generation
    print("\n" + "="*30)
    print("YOUR PERSONALIZED PLAN")
    print("="*30)
    
    print("\n[Recommended Diet]")
    if not diet_plan.empty:
        print(diet_plan[['Name', 'Budget']].to_string(index=False))
    else:
        print("No specific match found. Stick to high-protein home-cooked meals.")

    print("\n[Recommended Workout]")
    if not workout_plan.empty:
        print(workout_plan[['Name', 'Constraint']].to_string(index=False))
    else:
        print("Try daily 30-minute HIIT sessions.")
    
    print("\n" + "="*30)
    print("Project submitted for Edunet/IBM SkillsBuild Internship.")

if __name__ == "__main__":
    generate_plan()