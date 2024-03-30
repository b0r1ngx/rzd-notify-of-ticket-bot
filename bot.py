import logging
from datetime import date

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from telegram import ForceReply, Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from business.api.api import search_train_by_date
from business.is_tickets_available import is_tickets_available
from constants.constants import BOT_TOKEN
from database.db_api import commit_user_to_db, get_all_users
from database.db_session import init_database_session

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

bot: Bot


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    commit_user_to_db({"chat_id": user.id})
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


async def scan_for_available_tickets():
    # todo: if later what make user interaction, we can show user fast marks like:
    #       "get tickets for today" -> date.today()
    #       also if we go by this way, we need to understand OriginCode & DestinationCode,
    #       for user can search for any cities

    request = search_train_by_date(date(2024, 3, 31))
    is_available, train = is_tickets_available(request)
    if is_available:
        users = get_all_users()
        for user in users:
            await bot.send_message(
                chat_id=user.chat_id,
                text=f"Ticket available, check train: {train}",
            )


async def im_work():
    users = get_all_users()
    for user in users:
        await bot.send_message(
            chat_id=user.chat_id,
            text=f"Im working, dont kill me, I wanna be alive",
        )


def start_schedule_functions():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(scan_for_available_tickets, trigger=IntervalTrigger(seconds=10))
    scheduler.add_job(im_work, trigger=IntervalTrigger(minutes=10))
    scheduler.start()


def main() -> None:
    init_database_session()
    start_schedule_functions()

    application = Application.builder().token(BOT_TOKEN).build()

    global bot
    bot = application.bot

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
