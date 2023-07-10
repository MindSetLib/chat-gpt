import asyncio
import logging

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault

from commands import register_commands
from config import Config
from updates_worker import get_handled_updates_list

load_dotenv()


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Start chat with bot'),
        BotCommand(command='help', description='Start chat with bot'),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(Config.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot)

    register_commands(dp)

    await set_bot_commands(bot)

    try:
        await dp.start_polling(allowed_updates=get_handled_updates_list(dp))
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


try:
    asyncio.run(main())
except (KeyboardInterrupt, SystemExit):
    logging.info('Bot stopped!')
