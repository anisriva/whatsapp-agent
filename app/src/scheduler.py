from apscheduler.schedulers.background import BackgroundScheduler
from app.src.twilio_sender import send_whatsapp_checkin
from app.src.bots.telegram_bot import start_poll
from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_CHAT_ID = int(os.getenv("TELEGRAM_GROUP_CHAT_ID"))

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def start_schedulers():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_whatsapp_checkin, 'cron', hour=8, minute=0)
    scheduler.add_job(lambda: bot.send_message(chat_id=TELEGRAM_GROUP_CHAT_ID, text="/startpoll"), 'cron', hour=8, minute=0)
    scheduler.start()