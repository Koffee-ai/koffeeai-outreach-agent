# Directory structure:
# koffeeai-outreach-agent/
# ├── streamlit_app.py
# ├── scraper.py
# ├── mailer.py
# ├── social_messenger.py
# ├── tracker.py
# └── utils.py

# --- streamlit_app.py ---
import streamlit as st
from scraper import scrape_businesses
from mailer import send_email
from social_messenger import send_social_messages
from tracker import update_tracker, display_tracker
from utils import generate_outreach_texts

st.set_page_config(page_title="Koffee.ai Outreach Agent", page_icon="☕", layout="centered")
st.title("Welcome to Koffee.ai Outreach Agent — Grow your business with AI ✨")

st.sidebar.header("📅 Campaign Setup")
category = st.sidebar.text_input("Target Business Category", placeholder="e.g. cafes, gyms")
location = st.sidebar.text_input("Location", placeholder="e.g. Kakinada")
max_contacts = st.sidebar.slider("Max Businesses to Contact", 10, 100, 50)
special_offer = st.sidebar.text_area("Optional Special Offer")

if st.sidebar.button("✉️ Launch Outreach"):
    with st.spinner("Scraping businesses and preparing messages..."):
        businesses = scrape_businesses(category, location, max_contacts)
        for biz in businesses:
            name = biz['name']
            email = biz.get('email')
            socials = biz.get('socials')
            phone = biz.get('phone')

            en_msg, local_msg = generate_outreach_texts(name, category, location, special_offer)

            if email:
                send_email(email, en_msg, local_msg)
            if socials:
                send_social_messages(socials, en_msg, local_msg)

            update_tracker(name, email, socials)

        st.success("Outreach complete! Messages sent to selected businesses.")

st.divider()
st.header("📊 Outreach Tracker")
display_tracker()


# --- social_messenger.py ---
def send_social_messages(social_links, en_msg, local_msg):
    for platform, link in social_links.items():
        try:
            # This is a stub — actual messaging via automation APIs requires access tokens and platform permission.
            print(f"[SOCIAL] Sending message to {platform}: {link}")
            print(f"  English:\n{en_msg}")
            print(f"  Local:\n{local_msg}")

            # NOTE:
            # - Instagram/Facebook: Use Facebook Graph API (https://developers.facebook.com/docs/messenger-platform)
            # - LinkedIn: LinkedIn API has limited DM support. Alternatives include Puppeteer, TexAu, or PhantomBuster.
            # - For real usage, handle login/auth, rate limits, and message templates.

        except Exception as e:
            print(f"[SOCIAL ERROR] Failed to message on {platform}: {e}")
