import os
import random
from twilio.rest import Client

# ---------- CONFIG ----------
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH_TOKEN")
TO_NUMBER = os.getenv("TO_NUMBER")  # e.g. "whatsapp:+91XXXXXXXXXX"
FROM_NUMBER = "whatsapp:+14155238886"

# ---------- QUOTES ----------
QUOTES = [
    "Believe you can and you're halfway there. 🌟",
    "Every day is a new beginning. Take a deep breath and start again. 🌅",
    "Your only limit is your mind. 🚀",
    "Push yourself, because no one else is going to do it for you. 💪",
    "Small steps every day lead to big results. 🏆",
]

# ---------- SEND ----------
def send_motivation():
    client = Client(TWILIO_SID, TWILIO_AUTH)
    quote = random.choice(QUOTES)
    message = client.messages.create(
        from_=FROM_NUMBER,
        body=f"🌞 Daily Motivation 🌞\n\n{quote}",
        to=TO_NUMBER
    )
    print(f"✅ Sent: {quote} | SID: {message.sid}")

if __name__ == "__main__":
    send_motivation()
