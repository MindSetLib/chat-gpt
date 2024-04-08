"""Keyboard manipulation callbacks"""
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext


async def process_callback_model(call: types.CallbackQuery, state: FSMContext):
    model = call.data.replace('m_', '')
    model_choice = 'GPT-3.5' if 'gpt' in model else 'Claude 3'
    await state.update_data(model_choice=model)
    await call.message.edit_text(f'Вы выбрали {model_choice}')


def register_callbacks(dp: Dispatcher):
    """Register bot callbacks and triggers."""
    dp.register_callback_query_handler(process_callback_model, lambda c: c.data.startswith('m_'),
                                       state='*')
