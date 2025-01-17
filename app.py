import streamlit as st

# Full Page Layout
st.set_page_config(page_title="FAU ISM 6427C", layout="wide")

# Header with an Image
st.image("https://img2.wikia.nocookie.net/__cb20120628082105/collegefootballmania/images/4/4b/NCAA-Florida_Atlantic_Owls-logo.png")
st.title("FAU ISM 6427C")
st.write("Welcome to the course repository for FAU's ISM 6427C class.")

# Sidebar
st.sidebar.header("Course Information")
st.sidebar.write("Instructor: Dr. John Doe")
st.sidebar.write("Semester: Spring 2025")
st.sidebar.write("Office Hours: By Appointment")

# Main Content
st.subheader("About This Class")
st.write("This class focuses on practical applications of AI and data science tools, including the use of platforms like Streamlit for project deployment.")

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

# You can also use "with" notation:
with tab1:
    st.radio("Select one:", [1, 2])

