import streamlit as st
from urllib.parse import urlencode, quote

def validate_zip_or_location(location):
    """Validate ZIP code or location input (e.g., New York, NY or 94109)."""
    if location.isdigit():
        return len(location) == 5
    return len(location) > 0  # Assume valid if it's a non-empty text string

def submit_targeting_form(data):
    """Create a mailto link to redirect to Gmail."""
    subject = "Targeting Plan Request"
    body = f"""
    Hello,

    Please find the submitted targeting plan request details below:

    First Name: {data['First Name']}
    Last Name: {data['Last Name']}
    Name of Business: {data['Business Name']}
    Website: {data['Website']}
    Industry: {data['Industry']}
    Location: {data['Location']}
    Advertising Types: {", ".join(data['Advertising Type'])}
    Budget: {data['Budget']}
    Email: {data['Email']}
    Phone: {data['Phone']}
    Notes: {data['Notes']}
    """

    # Construct the mailto URL
    mailto_link = f"mailto:?subject={quote(subject)}&body={quote(body)}"
    st.markdown(f"[Click here to open Gmail](mailto:?subject={quote(subject)}&body={quote(body)})", unsafe_allow_html=True)
    st.markdown(f"<a href='{mailto_link}' target='_blank'>Open Gmail</a>", unsafe_allow_html=True)

def targeting_plan_form():
    """Render the targeting plan form."""
    st.markdown("Fill out the form below to receive a personalized advertising targeting plan based on your industry and location.")
    
    # Collecting user inputs
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    business_name = st.text_input("Name of Business/Store", placeholder="ABC Retail")
    website = st.text_input("Business Website", placeholder="https://www.example.com")
    industry = st.selectbox(
        "Select Your Industry",
        ["- Select Your Industry -", "Retail", "Healthcare", "Finance", "Education", "Other"]
    )
    location = st.text_input("Enter Your Location / Location to Target", placeholder='e.g., "New York, NY" or "94109"')
    advertising_type = st.multiselect(
        "What Type of Advertising Are You Interested In?",
        [
            "OTT (Over-the-Top Streaming Ads)",
            "CTV (Connected TV Ads)",
            "Geofencing",
            "Influencer Marketing",
            "Not Sure (to allow you to recommend a strategy)"
        ]
    )
    budget = st.selectbox("Do You Have a Budget in Mind?", [1000, 2000, 5000, 10000, "Not Sure"])
    email = st.text_input("Your Email", placeholder="example@email.com")
    phone = st.text_input("Your Phone Number", placeholder="(555) 123-4567")
    notes = st.text_area("Notes", placeholder="Any specific details or goals for your targeting plan")

    if st.button("Get My Target Plan"):
        # Validate required fields
        if not first_name or not last_name or industry == "- Select Your Industry -" or not validate_zip_or_location(location):
            st.error("Please fill out all required fields and ensure your location is valid.")
        else:
            # Prepare form data for submission
            form_data = {
                "First Name": first_name,
                "Last Name": last_name,
                "Business Name": business_name,
                "Website": website,
                "Industry": industry,
                "Location": location,
                "Advertising Type": advertising_type,
                "Budget": budget,
                "Email": email,
                "Phone": phone,
                "Notes": notes,
            }
            submit_targeting_form(form_data)

    st.markdown("Do Check https://brandify.io/targeting-plan/ for more Target Plans & Pricing")

# Call the function to render the form
targeting_plan_form()
