import streamlit as st
from googletrans import Translator

# Initialize translator
translator = Translator()

# Page config
st.set_page_config(page_title="Koffee.ai Outreach Agent", page_icon="☕", layout="centered")

# Header
st.title("☕ Koffee.ai Outreach Agent")
st.subheader("📢 Generate Outreach Messages for Businesses")

# Input Form
with st.form("outreach_form"):
    target_category = st.text_input("Target Business Category", placeholder="e.g., Gym, Café, Clinic")
    location = st.text_input("Target Location (City / State / Area)", placeholder="e.g., Kakinada, Andhra Pradesh")
    max_reach = st.number_input("Max Businesses to Contact", min_value=1, max_value=500, value=100)
    
    region = st.selectbox(
        "Target Region / Language",
        [
            "Andhra Pradesh → Telugu + English",
            "Karnataka → Kannada + English",
            "Tamil Nadu → Tamil + English",
            "Telangana → Telugu + English",
            "Kerala → Malayalam + English",
            "Rest of India → English only"
        ]
    )
    
    special_offer_enabled = st.checkbox("Enable Special Offer")
    special_offer_text = ""
    if special_offer_enabled:
        special_offer_text = st.text_area("Special Offer Text", placeholder="e.g., Get 25% off on first 3 months...")

    submit_btn = st.form_submit_button("Generate Outreach Messages 🚀")

# Message Generator Logic
if submit_btn:
    # English base message
    english_message = f"""
    Hello {target_category} owner 👋,

    Are you looking to boost your business in {location}?

    We at Koffee.ai offer:
    ✅ AI-powered Marketing Tools
    ✅ AI Automation Services
    ✅ AI SaaS solutions tailored to your business

    {"Special Offer: " + special_offer_text if special_offer_enabled else ""}

    👉 Visit: https://koffee-ai-marketing.netlify.app
    👉 WhatsApp: +91 99121 25596
    👉 Email: koffee.ai.marketing@gmail.com

    Let’s grow your business with AI ☕!
    """

    # Translate to local language
    if "Andhra Pradesh" in region or "Telangana" in region:
        local_lang = "te"  # Telugu
    elif "Karnataka" in region:
        local_lang = "kn"  # Kannada
    elif "Tamil Nadu" in region:
        local_lang = "ta"  # Tamil
    elif "Kerala" in region:
        local_lang = "ml"  # Malayalam
    else:
        local_lang = None  # English only
    
    if local_lang:
        local_message = translator.translate(english_message, dest=local_lang).text
    else:
        local_message = "Not applicable (English only region)."

    # Output
    st.success("✅ Messages Generated!")

    st.markdown("### 📩 English Message")
    st.code(english_message)

    st.markdown(f"### 🌐 Local Language Message ({region})")
    st.code(local_message)

    st.markdown("### 💬 Combined Message")
    combined_message = english_message + "\n\n" + local_message
    st.code(combined_message)

    # Copy button (Streamlit can't natively copy to clipboard, but user can copy from code block)
    st.info("👉 Copy and send this message via WhatsApp, Email, Social DMs.")

