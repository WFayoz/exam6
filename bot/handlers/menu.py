from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.buttons.reply import menu_buttons, salads, fast_food, traditional

menu_router = Router()


@menu_router.message(F.text == __('Menu'))
async def menu_handler(message: Message) -> None:
    await message.answer(_("Menu 🍽️ 👇🏿"), reply_markup=menu_buttons())


@menu_router.message(F.text == __('Salads'))
async def menu_handler(message: Message) -> None:
    await message.answer(_("Salads 🥗 👇🏿"), reply_markup=salads())


@menu_router.message(F.text == __('Fast food'))
async def menu_handler(message: Message) -> None:
    await message.answer("Fast food 🌭 👇🏿 ", reply_markup=fast_food())


@menu_router.message(F.text == __('Traditional foods'))
async def menu_handler(message: Message) -> None:
    await message.answer(_("Traditional foods 🍛 👇🏿"), reply_markup=traditional())


@menu_router.message(F.text == __('Sezar salad'))
async def menu_handler(message: Message) -> None:
    await message.answer(_("""1 large or 2 small heads of romaine lettuce
Parmesan cheese, shredded or shaved
Crisp croutons – homemade can be made several days ahead. The recipe below makes enough for 2 salads.
Caesar salad dressing – homemade is best and here is our favorite store-bought dressing in a pinch"""))


@menu_router.message(F.text == __('Olivie salad'))
async def menu_handler(message: Message) -> None:
    await message.answer(_("""1 large or 2 small heads of romaine lettuce
Parmesan cheese, shredded or shaved
Crisp croutons – homemade can be made several days ahead. The recipe below makes enough for 2 salads.
Caesar salad dressing – homemade is best and here is our favorite store-bought dressing in a pinch"""))


@menu_router.message(F.text == __('Plov'))
async def menu_handler(message: Message) -> None:
    await message.answer(_("""1 large or 2 small heads of romaine lettuce
Parmesan cheese, shredded or shaved
Crisp croutons – homemade can be made several days ahead. The recipe below makes enough for 2 salads.
Caesar salad dressing – homemade is best and here is our favorite store-bought dressing in a pinch"""))


@menu_router.message(F.text == __('Samsa'))
async def menu_handler(message: Message) -> None:
    await message.answer(_("""1 large or 2 small heads of romaine lettuce
Parmesan cheese, shredded or shaved
Crisp croutons – homemade can be made several days ahead. The recipe below makes enough for 2 salads.
Caesar salad dressing – homemade is best and here is our favorite store-bought dressing in a pinch"""))


@menu_router.message(F.text == __('Burger'))
async def menu_handler(message: Message) -> None:
    await message.answer(_("""1 large or 2 small heads of romaine lettuce
Parmesan cheese, shredded or shaved
Crisp croutons – homemade can be made several days ahead. The recipe below makes enough for 2 salads.
Caesar salad dressing – homemade is best and here is our favorite store-bought dressing in a pinch"""))


@menu_router.message(F.text == __('Hot Dog'))
async def menu_handler(message: Message) -> None:
    await message.answer(_("""1 large or 2 small heads of romaine lettuce
Parmesan cheese, shredded or shaved
Crisp croutons – homemade can be made several days ahead. The recipe below makes enough for 2 salads.
Caesar salad dressing – homemade is best and here is our favorite store-bought dressing in a pinch"""))
