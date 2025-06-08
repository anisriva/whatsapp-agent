import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    logger.info(f"Chat ID: {chat.id}, Title: {chat.title}, Type: {chat.type}")
    await update.message.reply_text(f"\u2705 Group ID: `{chat.id}`", parse_mode="Markdown")

def run_chat_id_fetcher():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN not set in .env")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, get_chat_id))
    logger.info("Send a message in the group with the bot to fetch its Chat ID.")
    app.run_polling()

if __name__ == "__main__":
    run_chat_id_fetcher()