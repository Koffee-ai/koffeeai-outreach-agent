import streamlit as st
from datetime import datetime
import random

# App Config
st.set_page_config(page_title="Koffee.ai Outreach Agent ☕", page_icon="☕", layout="centered")

# Logo & Title
st.image("assets/logo.jpeg", width=180)
st.markdown("## ☕ Koffee.ai Outreach Agent")
st.markdown("#### Grow your local business outreach with AI ✨")

# Sidebar Info
st.sidebar.title("Agent Settings")
city = st.sidebar.text_input("📍 Target City", value="Kakinada")
language = st.sidebar.radio("🈯 Language", ["Telugu + English", "English Only"])
num_messages = st.sidebar.slider("📤 Number of Messages", 1, 10, 3)

# Outreach Message Template
def generate_outreach_message(business_name, city, language):
    if language == "Telugu + English":
        return f"""
నమస్తే {business_name} team 🙏,

మీ వ్యాపారాన్ని Kakinada లో మరింత ప్రచారం చేయాలనుకుంటున్నారా? 🌟  
మీకు AI ఆధారిత **Marketing Tools** మరియు **Social Media Content Packs** అందిస్తున్నాము.  
**Koffee.ai** ద్వారా, మీరు 3x జెంప్ చేసుకోవచ్చు! 🚀

👉 మా వెబ్‌సైట్ చూడండి: https://koffee-ai-marketing.netlify.app  
👉 మమ్మల్ని సంప్రదించండి: +91 99121 25596 (WhatsApp)  
👉 Email: koffee.ai.marketing@gmail.com  

Let’s grow your business with AI ☕!

---

Hello {business_name} team 👋,

Are you looking to boost your business in {city}?  
We offer **AI-powered Marketing Tools** and **Social Media Content Packs** via Koffee.ai. 🚀

👉 Visit: https://koffee-ai-marketing.netlify.app  
👉 WhatsApp: +91 99121 25596  
👉 Email: koffee.ai.marketing@gmail.com  

Let’s grow your business with AI ☕!
"""
    else:
        return f"""
Hello {business_name} team 👋,

Are you looking to boost your business in {city}?  
We offer **AI-powered Marketing Tools** and **Social Media Content Packs** via Koffee.ai. 🚀

👉 Visit: https://koffee-ai-marketing.netlify.app  
👉 WhatsApp: +91 99121 25596  
👉 Email: koffee.ai.marketing@gmail.com  

Let’s grow your business with AI ☕!
"""

# User Input
business_list = st.text_area("📝 Enter Business Names (one per line)", height=150)
if st.button("Generate Outreach Messages"):
    st.markdown("---")
    st.subheader("📤 Generated Messages:")
    businesses = business_list.strip().split("\n")
    if businesses:
        random.shuffle(businesses)
        for i, business in enumerate(businesses[:num_messages]):
            msg = generate_outreach_message(business.strip(), city, language)
            st.markdown(f"**{i+1}. {business.strip()}**")
            st.code(msg)
    else:
        st.warning("Please enter at least one business name.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 14px;'>
    Powered by <b>Koffee.ai ☕</b> | Contact: <b>koffee.ai.marketing@gmail.com</b> | WhatsApp: <b>+91 99121 25596</b>
    </div>
    """, unsafe_allow_html=True
)
