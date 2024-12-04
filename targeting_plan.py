import streamlit as st

def validate_zip(zip_code):
    """Validate ZIP code format (US 5-digit)."""
    return len(zip_code) == 5 and zip_code.isdigit()

def submit_form(industry, location, budget):
    st.success(f"Form submitted successfully for industry: {industry}, location: {location}, and budget: ${budget}.")

def targeting_plan_form():
    """Render the targeting plan form."""
    industry = st.selectbox("Select Industry", ["Retail", "Healthcare", "Finance", "Education"])
    location = st.text_input("Enter Location (ZIP code):")
    budget = st.number_input("Set Budget ($)", min_value=100, step=50)

    if st.button("Submit"):
        if validate_zip(location):
            submit_form(industry, location, budget)
        else:
            st.error("Invalid ZIP code! Please enter a valid 5-digit ZIP.")
