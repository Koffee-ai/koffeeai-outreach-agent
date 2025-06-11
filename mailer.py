# mailer.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configure your email credentials (use environment variables in production)
EMAIL_ADDRESS = "koffee.ai.marketing@gmail.com"
EMAIL_PASSWORD = "@3nadh3NADH"

def send_email(to_email, en_msg, local_msg):
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "🚀 Grow your business with AI — From Koffee.ai"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email

        html_content = f"""
        <html>
            <body>
                <p>{en_msg}</p>
                <hr>
                <p>{local_msg}</p>
            </body>
        </html>
        """

        msg.attach(MIMEText(html_content, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        print(f"[EMAIL] Sent to {to_email}")

    except Exception as e:
        print(f"[EMAIL ERROR] Failed to send email to {to_email}: {e}")
