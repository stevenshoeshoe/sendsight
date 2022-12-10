import streamlit as st

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data.head())

template = st.selectbox("Select a templte", ["Headcount Analysis", "Cohort Analysis"])

email = st.text_input("Enter your email address")

if st.button("Send Email"):
    # Code to send email goes here
    st.success("Email sent!")
