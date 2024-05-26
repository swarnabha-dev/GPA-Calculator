import streamlit as st

# Function to calculate GPA
def calculate_gpa(grades, credits):
    grade_points = {
        'S': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 0
    }
    total_points = sum([grade_points[grade] * credit for grade, credit in zip(grades, credits)])
    total_credits = sum(credits)
    gpa = total_points / total_credits
    return gpa

# Streamlit app
st.set_page_config(
    page_title="GPA Calculator",
    page_icon=":bar_chart:",
    layout="centered",
    initial_sidebar_state="auto",
)

# Load custom CSS from styles.css
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("GPA Calculator")

st.markdown("""
Use this app to calculate your GPA based on your grades and course credits.
""")

num_courses = st.number_input("Enter the number of courses", min_value=1, max_value=10, value=1)

credits = []
grades = []

grade_options = ['S', 'A', 'B', 'C', 'D', 'E', 'F']

for i in range(num_courses):
    st.subheader(f"Course {i+1}")
    
    credit = st.number_input(f"Enter the credits for course {i+1}", min_value=0.5, max_value=5.0, value=3.0, step=0.5)
    credits.append(credit)
    
    grade = st.selectbox(f"Select the grade for course {i+1}", grade_options)
    grades.append(grade)

if st.button("Calculate GPA"):
    gpa = calculate_gpa(grades, credits)
    st.subheader(f"Your GPA is: {gpa:.2f}")
else:
    st.write("Enter your course details to calculate GPA")

# Add "Made by" message at the bottom right corner
st.markdown("""
    <div class="footer">
        Made by Your Name
        <a href="https://github.com/swarnabha-dev/" target="_blank"><img src="https://img.icons8.com/?size=48&id=LoL4bFzqmAa0&format=png&color=000000" style="vertical-align: middle;"></a>
        <a href="https://www.instagram.com/swarnabha_halder/" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/instagram-new.png" style="vertical-align: middle;"></a>
        <a href="https://www.linkedin.com/in/swarnabha-halder-627692254/" target="_blank"><img src="https://img.icons8.com/color/48/000000/linkedin.png" style="vertical-align: middle;"></a>
    </div>
    """, unsafe_allow_html=True)
