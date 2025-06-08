from apscheduler.schedulers.background import BackgroundScheduler
from bots.telegram_bot import start_poll
from telegram import Bot
from telegram.ext import ApplicationBuilder
import os, asyncio

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
group_chat_id = os.getenv("GROUP_CHAT_ID")

scheduler = BackgroundScheduler()

def schedule_daily_poll():
    bot = Bot(token=bot_token)
    
    async def send_poll():
        await bot.send_poll(
            chat_id=group_chat_id,
            question="Did you go to the gym today?",
            options=["Yes", "No"],
            is_anonymous=False,
        )

    scheduler.add_job(lambda: asyncio.run(send_poll()), 'cron', hour=9)  # Every day at 9 AM
    scheduler.start()
