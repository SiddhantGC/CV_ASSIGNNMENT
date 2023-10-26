import streamlit as st
# Streamlit app title and description
st.title("First Name Printer")
st.write("Enter your first name and see it printed below.")

# Input for the first name
first_name = st.text_input("Enter your first name")

# Check if the input is not empty and display it
if first_name:
    st.write(f"Hello, {first_name}!")

