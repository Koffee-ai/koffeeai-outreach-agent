import streamlit as st
from PIL import Image

# Load logo
logo = Image.open("assets/logo.jpeg")  # Make sure it's a rounded image

# Page config
st.set_page_config(page_title="Koffee.ai Outreach Agent", page_icon="☕", layout="wide", initial_sidebar_state="expanded")

# Sidebar
with st.sidebar:
    st.image(logo, width=150)
    st.markdown("### Welcome to Koffee.ai Outreach Agent — Grow your business with AI 🚀")
    
    category = st.selectbox("Business Category", ["Cafe", "Gym", "Salon", "Boutique", "Restaurant", "Hospital", "Other"])
    if category == "Other":
        category = st.text_input("Enter your category")

    state = st.selectbox("Select State", ["Andhra Pradesh", "Karnataka", "Telangana", "Tamil Nadu", "Kerala"])
    city = st.text_input("Enter City")

    max_contacts = st.slider("Max Businesses to Reach", 10, 100, 50)

    language_option = st.selectbox("Preferred Language", ["Auto (Based on State)", "English", "Telugu", "Kannada", "Tamil", "Malayalam"])

    special_offer = st.text_area("Special Offer (Optional)")

    start = st.button("🚀 Start Outreach", use_container_width=True)

# Main content
st.title("📢 Koffee.ai Smart Outreach Dashboard")

if start:
    st.info("🔍 Collecting businesses from social media and web directories...")
    progress = st.progress(0)
    status_text = st.empty()

    # Simulated steps
    import time
    steps = ["Collecting data", "Scraping contacts", "Generating messages", "Sending outreach", "Waiting for responses"]
    for i, step in enumerate(steps):
        status_text.markdown(f"**{step}...**")
        time.sleep(1.2)
        progress.progress((i+1)/len(steps))

    st.success("✅ Outreach Completed!")

    st.markdown("### 📊 Outreach Summary")
    st.dataframe({
        "Business Name": ["ABC Cafe", "XYZ Gym"],
        "Email Sent": ["Yes", "Yes"],
        "WhatsApp Sent": ["Yes", "No"],
        "DM Sent": ["No", "Yes"],
        "Response Status": ["Pending", "Responded"],
        "Meeting Booked": ["-", "✅"]
    })

    st.markdown("---")
    st.caption("Made with ☕ by Koffee.ai — AI-Powered Growth")
