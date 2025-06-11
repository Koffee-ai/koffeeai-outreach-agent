import csv
import os
import streamlit as st

TRACKER_FILE = "outreach_tracker.csv"

def update_tracker(name, email, socials):
    exists = os.path.exists(TRACKER_FILE)
    with open(TRACKER_FILE, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not exists:
            writer.writerow(["Business Name", "Email", "Social Links"])
        writer.writerow([name, email, ", ".join(socials.keys() if socials else [])])

def display_tracker():
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE, newline="") as csvfile:
            st.dataframe(csv.reader(csvfile), height=300)
    else:
        st.info("No outreach has been tracked yet.")
