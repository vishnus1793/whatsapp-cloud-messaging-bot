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
    "To Know is to Know That You Know Nothing. That is the Meaning of True Knowledge.",
    
    # Iron Man & Marvel Inspired Quotes
    "I am Iron Man. 🕶️",
    "Sometimes you gotta run before you can walk. ⚙️",
    "Heroes are made by the path they choose, not the powers they are graced with. 🦸",
    "Part of the journey is the end. 🔥",
    "We’re in the endgame now. ♟️",
    "It’s not about how much we lost, it’s about how much we have left. ❤️",
    "The truth is... I am Iron Man. ⚡",
    "With great power comes great responsibility. 🕷️",
    "Wakanda Forever! 🐾",
    "Avengers, assemble! 🛡️",
    "I can do this all day. 🇺🇸",
    "The hardest choices require the strongest wills. 💎",
    "I am inevitable. ⏳"
]

# ---------- SEND ----------
from datetime import datetime
import random
from twilio.rest import Client

def send_motivation():
    client = Client(TWILIO_SID, TWILIO_AUTH)
    quote = random.choice(QUOTES)
    today = datetime.now().strftime("%A, %d %B %Y")  # Example: "Wednesday, 27 August 2025"
    
    message = client.messages.create(
        from_=FROM_NUMBER,
        body=f"🌞 Daily Motivation 🌞\n📅 {today}\n\n{quote}",
        to=TO_NUMBER
    )
    print(f"✅ Sent: {quote} | Date: {today} | SID: {message.sid}")

if __name__ == "__main__":
    send_motivation()
