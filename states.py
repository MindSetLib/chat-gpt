from aiogram.dispatcher.filters.state import StatesGroup, State


class ProcessModel(StatesGroup):
    model_choice = State()
