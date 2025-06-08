from app.src.connectors.db import init_db
from app.src.bots.telegram_bot import run_telegram_bot
from app.src.scheduler import start_schedulers

init_db()
start_schedulers()
run_telegram_bot()