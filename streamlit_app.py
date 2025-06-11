# Directory structure:
# koffeeai-outreach-agent/
# ├── streamlit_app.py
# ├── scraper.py
# ├── mailer.py
# ├── social_messenger.py
# ├── tracker.py
# ├── utils.py
# └── auto_responder.py

# --- streamlit_app.py ---
import streamlit as st
from scraper import scrape_businesses
from mailer import send_email
from social_messenger import send_social_messages
from tracker import update_tracker, display_tracker
from utils import generate_outreach_texts
from auto_responder import handle_responses

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

if st.button("📥 Check for Responses"):
    with st.spinner("Checking for replies and booking meetings..."):
        handle_responses()
        st.success("Auto-replies sent and tracker updated.")

st.divider()
st.header("📊 Outreach Tracker")
display_tracker()


# --- social_messenger.py ---
import time

def send_social_messages(social_links, en_msg, local_msg):
    for platform, link in social_links.items():
        try:
            print(f"[SOCIAL] Sending message to {platform}: {link}")
            print(f"  English:\n{en_msg}")
            print(f"  Local:\n{local_msg}")

            # NOTE:
            # - Instagram/Facebook: Use Meta Graph API (https://developers.facebook.com/docs/messenger-platform)
            # - LinkedIn: Use LinkedIn Messaging API or automation tools like TexAu, PhantomBuster, Puppeteer.
            # - Login, cookies, sessions, and headless automation are needed for real DMs.

            time.sleep(2)  # simulate sending delay
        except Exception as e:
            print(f"[SOCIAL ERROR] Failed to message on {platform}: {e}")


# --- auto_responder.py ---
def check_incoming_messages():
    simulated_responses = [
        {"name": "Chai Adda", "email": "chai@adda.com", "platform": "email"},
        {"name": "FitZone Gym", "social": "https://instagram.com/fitzone"}
    ]
    return simulated_responses

def generate_auto_reply(name):
    return f"""Hi {name}, 👋\n\nThanks for your interest in Koffee.ai 🚀\n\nWe’d love to discuss how our AI marketing and automation tools can grow your business.\nHere’s a link to book a quick call with our team: https://calendly.com/koffee-ai/15min\n\nLooking forward to connecting!\n\n– Koffee.ai Team ☕"""

def handle_responses():
    responses = check_incoming_messages()
    for r in responses:
        reply = generate_auto_reply(r['name'])

        if 'email' in r:
            print(f"[AUTO-REPLY] Sending email to {r['email']}:\n{reply}")
            # send_email(r['email'], reply, "")
        elif 'social' in r:
            print(f"[AUTO-REPLY] Sending message to social link {r['social']}:\n{reply}")
            # send_social_messages({"platform": r['social']}, reply, "")

        print(f"[TRACKER] Marked {r['name']} as responded.")
