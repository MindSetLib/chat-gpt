from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def model_choice_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True)
    btn_gpt = InlineKeyboardButton('GPT-3.5', callback_data='m_gpt')
    btn_claude = InlineKeyboardButton('Claude 3', callback_data='m_claude')
    keyboard.add(btn_gpt, btn_claude)
    return keyboard
