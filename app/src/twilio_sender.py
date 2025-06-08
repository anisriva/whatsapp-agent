from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM = os.getenv("TWILIO_PHONE_NUMBER")
RECIPIENTS = os.getenv("WHATSAPP_RECIPIENTS", "").split(",")

client = Client(TWILIO_SID, TWILIO_TOKEN)

def send_whatsapp_checkin():
    for recipient in RECIPIENTS:
        client.messages.create(
            from_=FROM,
            body="🏋️ Did you go to the gym today? Reply with Yes/No",
            to=recipient.strip()
        )