from aiogram import Dispatcher
from aiogram.types import Message

from utils import make_request_openai, make_requests


async def send_welcome(message: Message):
    text = "Hi there! Сhat-GPT bot at your service!\n\n"
    await message.answer(text)


async def ask_question(message: Message):
    answer = await make_request_openai(message.text)
    await message.answer(answer)


def register_commands(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_message_handler(ask_question, regexp=r'^(?![\d+_@.-]+$)[a-zA-Zа-яА-Я0-9+_. @?-]*$')
