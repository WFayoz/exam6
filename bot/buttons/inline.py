from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _

from db.models import Category


def admin():
    ikb = InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text="Admin 1", url='https://t.me/WFayoz'),
        InlineKeyboardButton(text="Admin 2", url='https://t.me/WFayoz'),

    )
    ikb.adjust(repeat=True)
    return ikb.as_markup()
