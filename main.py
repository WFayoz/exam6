import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n, FSMI18nMiddleware

from bot.dispatcher import dp
from env_data.utils import Env
import db.models
from bot import handlers

db_session = db.AsyncDatabaseSession()


async def main() -> None:
    db_session.init()
    await db_session.create_all()
    i18n = I18n(path='locales', default_locale='en', domain="messages")
    dp.update.middleware(FSMI18nMiddleware(i18n))
    bot = Bot(token=Env.bot.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
