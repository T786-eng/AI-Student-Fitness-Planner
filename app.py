import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(page_title="AI Fitness Planner", page_icon="🥗")

# Load Data
@st.cache_data
def load_data():
    # Ensure fitness_data.csv is in the same folder
    return pd.read_csv('fitness_data.csv')

df = load_data()

# UI Header
st.title("🎓 AI Personalized Workout & Diet Planner")
st.markdown("### Budget-friendly fitness for students")
st.divider()

# Sidebar for Inputs
st.sidebar.header("Personalize Your Plan")
goal = st.sidebar.selectbox("What is your goal?", ["Weight Loss", "Muscle Gain", "Maintenance"])
diet_pref = st.sidebar.radio("Dietary Preference", ["Vegetarian", "Non-Vegetarian"])
budget = st.sidebar.select_slider("Budget Level", options=["Low", "Medium"])

# Logic Trigger
if st.sidebar.button("Generate My Plan"):
    col1, col2 = st.columns(2)

    # Filter Diet
    diet_plan = df[(df['Type'] == 'Diet') & 
                   (df['Goal'] == goal) & 
                   (df['Constraint'] == diet_pref) & 
                   (df['Budget'] == budget)]

    # Filter Workout
    workout_plan = df[(df['Type'] == 'Workout') & 
                      (df['Goal'] == goal) & 
                      (df['Budget'] == budget)]

    with col1:
        st.subheader("🍎 Diet Plan")
        if not diet_plan.empty:
            for item in diet_plan['Name']:
                st.success(f"**{item}**")
        else:
            st.info("No specific match. Focus on high-protein home food!")

    with col2:
        st.subheader("🏋️ Workout Routine")
        if not workout_plan.empty:
            for item in workout_plan['Name']:
                st.warning(f"**{item}**")
        else:
            st.info("Try 30 mins of daily walking/HIIT.")
    
    st.balloons()
else:
    st.info("👈 Enter your details in the sidebar and click 'Generate My Plan'")

# Footer for Internship
st.divider()
st.caption("Developed for Edunet (IBM SkillsBuild) Internship Project submission.")