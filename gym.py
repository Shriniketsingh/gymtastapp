import streamlit as st

# Set up the app's configuration
st.set_page_config(page_title="Gym Task Manager", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for cool color theme and font
st.markdown("""
    <style>
        /* Background and text colors */
        .main {
            background-color: #202020;
            color: #f1f1f1;
            font-family: 'Poppins', sans-serif;
        }
        .stSidebar {
            background-color: #1a1a1a;
        }
        .stButton>button {
            background-color: #00adb5;
            color: #f1f1f1;
            border-radius: 8px;
            font-weight: bold;
            font-family: 'Poppins', sans-serif;
        }
        /* Header styles */
        h1, h2, h3, h4 {
            color: #00adb5;
            font-family: 'Poppins', sans-serif;
        }
        /* Customize scrollbar */
        ::-webkit-scrollbar {
            width: 12px;
        }
        ::-webkit-scrollbar-thumb {
            background: #393e46;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #00adb5;
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Chest Day", "Back Day", "Leg Day", "Achievements", "Settings"])

# Dashboard
if page == "Dashboard":
    st.title("Gym Task Manager Dashboard 💪")
    st.write("Overview of your daily muscle group targets and progress.")

# Chest Day
elif page == "Chest Day":
    st.title("Chest Day Workouts 🏋️‍♂️")
    st.write("Target Muscle Groups: Chest, Triceps, Shoulders")
    # Input fields for setting tasks and limits
    task = st.text_input("Set Your Chest Day Task")
    sets_reps = st.text_input("Sets x Reps")
    notes = st.text_area("Notes")
    limit = st.number_input("Set Your Daily Limit", min_value=1, max_value=100, value=10)
    
    if st.button("Add Task"):
        st.write(f"Task added: {task} - {sets_reps}")
        st.write(f"Limit: {limit} sets/reps")
        st.write(f"Notes: {notes}")

# Back Day
elif page == "Back Day":
    st.title("Back Day Workouts 💪")
    st.write("Target Muscle Groups: Back, Biceps, Lats")
    # Input fields for setting tasks and limits
    task = st.text_input("Set Your Back Day Task")
    sets_reps = st.text_input("Sets x Reps")
    notes = st.text_area("Notes")
    limit = st.number_input("Set Your Daily Limit", min_value=1, max_value=100, value=10)
    
    if st.button("Add Task"):
        st.write(f"Task added: {task} - {sets_reps}")
        st.write(f"Limit: {limit} sets/reps")
        st.write(f"Notes: {notes}")

# Leg Day
elif page == "Leg Day":
    st.title("Leg Day Workouts 🦵")
    st.write("Target Muscle Groups: Quads, Hamstrings, Glutes")
    # Input fields for setting tasks and limits
    task = st.text_input("Set Your Leg Day Task")
    sets_reps = st.text_input("Sets x Reps")
    notes = st.text_area("Notes")
    limit = st.number_input("Set Your Daily Limit", min_value=1, max_value=100, value=10)
    
    if st.button("Add Task"):
        st.write(f"Task added: {task} - {sets_reps}")
        st.write(f"Limit: {limit} sets/reps")
        st.write(f"Notes: {notes}")

# Achievements
elif page == "Achievements":
    st.title("Achievements 🏆")
    st.write("Track your progress and completed tasks.")
    # Placeholder for achievements, you can extend this to display actual achievements
    st.write("You have completed 10 out of 12 tasks this week!")
    st.write("Great job! Keep pushing your limits.")

# Settings
elif page == "Settings":
    st.title("Settings ⚙️")
    st.write("Customize your app settings here.")

# Example layout with columns
st.header("Leg Day 🦵")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Workouts")
    st.write("Squats - Target: Quads, Hamstrings")
    st.write("Leg Press - Target: Quads, Hamstrings")

with col2:
    st.subheader("Notes 📝")
    st.write("Focus on full range of motion, control the weight.")
    st.text_area("Add your own notes")

