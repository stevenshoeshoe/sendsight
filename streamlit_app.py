import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

def generate_streamlit_report(df):
  # number of employees
  num_employees = len(df)
  st.write("Number of employees:", num_employees)

  # top locations
  top_locations = df['state'].value_counts()[:3]
  st.write("Top locations:")
  st.bar_chart(top_locations)

  # top departments
  top_departments = df['department'].value_counts()[:3]
  st.write("Top departments:")
  st.bar_chart(top_departments)

if st.button("Create Report"):
    generate_streamlit_report(df)
    st.success("Email sent!")

template = st.selectbox("Select a template", ["Headcount Analysis", "Cohort Analysis"])

email = st.text_input("Enter your email address")

if st.button("Send Email"):
    # Code to send email goes here
    st.success("Email sent!")