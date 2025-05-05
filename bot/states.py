from aiogram.fsm.state import StatesGroup, State


class BotState(StatesGroup):
    language = State()


class BackState(StatesGroup):
    main = State()
