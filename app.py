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
>>> tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
>>> tab1.write("this is tab 1")
>>> tab2.write("this is tab 2")

st.area_chart(df)
st.bar_chart(df)
st.bar_chart(df, horizontal=True)
st.line_chart(df)
st.map(df)
st.scatter_chart(df)

st.altair_chart(chart)
st.bokeh_chart(fig)
st.graphviz_chart(fig)
st.plotly_chart(fig)
st.pydeck_chart(chart)
st.pyplot(fig)
st.vega_lite_chart(df, spec)

# Work with user selections
event = st.plotly_chart(
    df,
    on_select="rerun"
)
event = st.altair_chart(
    chart,
    on_select="rerun"
)
event = st.vega_lite_chart(
    df,
    spec,
    on_select="rerun"
)
