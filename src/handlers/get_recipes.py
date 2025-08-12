import logging
from aiogram import Router, F
from aiogram.types import Message

from src.keyboards.all_keyboards import diet_keyboard
from locales import RusButtons

get_recipes_router = Router()

logger = logging.getLogger(__name__)


@get_recipes_router.message(F.text == RusButtons.GET_RECIPE)
async def get_breakfast(message: Message):
    logger.info(f"Get recipe button was pressed by user {message.from_user.username}")
    await message.answer("Выберите прием пищи:", reply_markup=diet_keyboard())


@get_recipes_router.message(F.text == RusButtons.GET_BREAKFAST)
async def get_breakfast(message: Message):
    logger.info(
        f"Get breakfast command was pressed by user {message.from_user.username}"
    )
    await message.answer("Пока рано", reply_markup=diet_keyboard())
