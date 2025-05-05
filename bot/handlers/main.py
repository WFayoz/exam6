from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.buttons.reply import uzb_text, en_text, main_panel, language_text, language
from bot.buttons.inline import admin
from bot.states import BotState, BackState
from bot.utils_function import check_user

main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await check_user(message)
    await state.set_state(BotState.language)
    await message.answer(_("Hello, {}".format(message.from_user.full_name)))
    await message.answer(text="Choose language || Tilni tanlang", reply_markup=language())


@main_router.message(BotState.language, F.text.in_([uzb_text, en_text]))
async def command_start_handler(message: Message, state: FSMContext, i18n) -> None:
    map_ = {uzb_text: "uz", en_text: "en"}
    await state.set_data({"locale": map_.get(message.text)})
    i18n.current_locale = map_.get(message.text)
    await message.answer(_("Welcome"), reply_markup=main_panel())


@main_router.message(F.text == __("Contact with us"))
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Admin", reply_markup=admin())


@main_router.message(F.text == "hello")
async def language_check(message: Message):
    await message.answer(_("hello this text is for testing is multilang working or not "))
