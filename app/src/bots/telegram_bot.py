from telegram import Update, Poll
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, PollAnswerHandler
import logging
import os
from app.src.connectors.db import get_session
from app.src.models import PollResponse
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_CHAT_ID = int(os.getenv("TELEGRAM_GROUP_CHAT_ID").split()[0])


poll_question = "Did you go to the gym today?"

async def start_poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != TELEGRAM_GROUP_CHAT_ID:
        return await update.message.reply_text("Use this command in the group only.")

    message = await context.bot.send_poll(
        chat_id=TELEGRAM_GROUP_CHAT_ID,
        question=poll_question,
        options=["Yes", "No"],
        is_anonymous=False,
        allows_multiple_answers=False,
    )
    context.bot_data[message.poll.id] = message.message_id

async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = update.poll_answer
    user_id = answer.user.id
    username = answer.user.username
    response = ", ".join(answer.option_ids.__str__())

    poll_id = answer.poll_id
    message_id = context.bot_data.get(poll_id)
    if message_id is None:
        return

    session = get_session()
    session.add(PollResponse(
        platform="telegram",
        user_id=str(user_id),
        username=username,
        question=poll_question,
        response="Yes" if answer.option_ids[0] == 0 else "No",
    ))
    session.commit()


def run_telegram_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("startpoll", start_poll))
    app.add_handler(PollAnswerHandler(handle_poll_answer))
    logging.info("Telegram bot is running...")
    app.run_polling()