def generate_outreach_texts(business_name, category, location, offer_text=None):
    # You can plug in actual regional translations later
    english_text = f"""
Hi {business_name} team 👋,

Are you looking to grow your {category} business in {location}?

Koffee.ai provides **AI-powered Marketing Tools**, **Automation**, and **AI SaaS** to increase your customer engagement and boost sales. 🚀
{f"\n🎁 Special Offer: {offer_text}" if offer_text else ""}

Visit us: https://koffee-ai-marketing.netlify.app  
Contact: +91 99121 25596  
Email: koffee.ai.marketing@gmail.com

Let’s grow your business with AI ☕
"""

    local_text = f"""హాయ్ {business_name} 🙏,

మీ {category} బిజినెస్ ను {location} లో పెంచాలనుకుంటున్నారా?

**Koffee.ai** మీకు AI ఆధారిత మార్కెటింగ్ టూల్స్, ఆటోమేషన్ మరియు SaaS సేవలు అందిస్తుంది.  
{f"\n🎁 స్పెషల్ ఆఫర్: {offer_text}" if offer_text else ""}

మమ్మల్ని సంప్రదించండి: https://koffee-ai-marketing.netlify.app  
📞 +91 99121 25596  
📧 koffee.ai.marketing@gmail.com

AI తో మీ వ్యాపారాన్ని పెంచండి ☕
"""

    return english_text.strip(), local_text.strip()
