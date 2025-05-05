
from bot.dispatcher import dp
from bot.handlers.main import main_router
from bot.handlers.menu import menu_router

dp.include_routers(
    *[main_router,menu_router]
)
