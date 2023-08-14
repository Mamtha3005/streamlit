import streamlit as st
import joblib
from format_results import format_to_json, save_json_to_excel

# Load the trained ML model
model = joblib.load("sentiment_model.pkl")

st.title("Let's predict RNA Sequences!")

# Adding a text input widget
rna_sequence = st.text_input("Enter RNA Sequence", "Type here...")

# Make prediction when user submits input
if st.button("Predict"):
    # Process the input using the ML model
    prediction = model.predict([rna_sequence])[0]

    formatted_result = format_to_json(prediction)

    # Display the formatted result as JSON
    st.table(formatted_result)

    # Save the JSON data to an Excel file
    save_json_to_excel(formatted_result, "sentiment_results.xlsx")