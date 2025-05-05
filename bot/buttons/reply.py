from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _

uzb_text = "Uzbek"
en_text = "English"
main_panel_text = "Main Panel"
language_text = "Language"


def make_reply(btns: list, size: list, repeat=False):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*btns)
    if repeat:
        rkb.adjust(size[0], repeat=True)
    else:
        rkb.adjust(size[0], repeat=True)
    return rkb.as_markup(resize_keyboard=True)


def language():
    btn1 = KeyboardButton(text="Uzbek")
    btn2 = KeyboardButton(text="English")
    buttons = [btn1, btn2]
    size = [2]
    return make_reply(buttons, size)


def main_panel():
    btn1 = KeyboardButton(text="Menu")
    btn2 = KeyboardButton(text=_("Contact with us"))
    buttons = [btn1, btn2]
    size = [2]
    return make_reply(buttons, size)


def menu_buttons():
    btn1 = KeyboardButton(text=_("Salads"))
    btn3 = KeyboardButton(text='Fast food')
    btn2 = KeyboardButton(text=_("Traditional foods"))
    btn4 = KeyboardButton(text=_("Back"))
    buttons = [btn1, btn2, btn3, btn4]
    size = [3, 1]
    return make_reply(buttons, size)


def salads():
    btn1 = KeyboardButton(text=_("Sezar salad"))
    btn2 = KeyboardButton(text=_('Olivie salad'))
    btn3 = KeyboardButton(text=_("Back"))
    buttons = [btn1, btn2, btn3]
    size = [2, 1]
    return make_reply(buttons, size)


def fast_food():
    btn1 = KeyboardButton(text="Burger")
    btn2 = KeyboardButton(text='Hot Dog')
    btn3 = KeyboardButton(text=_("Back"))
    buttons = [btn1, btn2, btn3]
    size = [2, 1]
    return make_reply(buttons, size)


def traditional():
    btn1 = KeyboardButton(text=_("Plov"))
    btn2 = KeyboardButton(text=_('Samsa'))
    btn3 = KeyboardButton(text=_("Back"))
    buttons = [btn1, btn2, btn3]
    size = [2, 1]
    return make_reply(buttons, size)
