from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from api import make_model_request
from keyboards import model_choice_keyboard


async def send_welcome(message: Message):
    text = "Бот готов к работе!\n\n" \
           "Используйте команду /model для выбора модели.\n" \
           "Задайте свой вопрос и дождитесь ответа от бота."
    await message.answer(text)


async def send_model(message: Message):
    text = "Выберите модель:\n"
    await message.answer(text, reply_markup=await model_choice_keyboard())


async def ask_question(message: Message, state: FSMContext):
    state_data = await state.get_data()
    try:
        model = state_data['model_choice']
        temp_msg = await message.answer('Генерирую ответ...')
        answer = await make_model_request(question=message.text,
                                          model=model)
        await temp_msg.edit_text(answer)
    except KeyError:
        await message.answer('Для начала выберите модель для обращения, \nиспользуя команду /model')
        await state.finish()


def register_commands(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(send_model, commands=['model'])

    dp.register_message_handler(ask_question, regexp=r'^(?![\d+_@.-]+$)[a-zA-Zа-яА-Я0-9+_.,: @?-]*$',
                                state='*')
