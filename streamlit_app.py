import streamlit as st
import pandas as pd

COLOR_RED = "#FF4B4B"
COLOR_BLUE = "#1C83E1"
COLOR_CYAN = "#00C0F2"

def display_callout(title, color, icon, second_text):
    st.markdown(
        div(
            style=styles(
                background_color=color,
                padding=rem(1),
                display="flex",
                flex_direction="row",
                border_radius=rem(0.5),
                margin=(0, 0, rem(0.5), 0),
            )
        )(
            div(style=styles(font_size=rem(2), line_height=1))(icon),
            div(style=styles(padding=(rem(0.5), 0, rem(0.5), rem(1))))(title),
        ),
        unsafe_allow_html=True,
    )

def display_small_text(text):
    st.markdown(
        div(
            style=styles(
                font_size=rem(0.8),
                margin=(0, 0, rem(1), 0),
            )
        )(text),
        unsafe_allow_html=True,
    )

def display_dial(title, value, color):
    st.markdown(
        div(
            style=styles(
                text_align="center",
                color=color,
                padding=(rem(0.8), 0, rem(3), 0),
            )
        )(
            h2(style=styles(font_size=rem(0.8), font_weight=600, padding=0))(title),
            big(style=styles(font_size=rem(3), font_weight=800, line_height=1))(
                value
            ),
        ),
        unsafe_allow_html=True,
    )

def display_dict(dict):
    for k, v in dict.items():
        a, b = st.columns([1, 4])
        a.write(f"**{k}:**")
        b.write(v)



uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

def generate_streamlit_report(df):
  # number of employees
  num_employees = len(df)
  polarity_color = COLOR_BLUE
  subjectivity_color = COLOR_CYAN
  
  st.write(display_dial("Employees", f"{num_employees}", polarity_color))

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