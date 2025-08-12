import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from src.keyboards.all_keyboards import start_keyboard
from locales import RusButtons

start_router = Router()

logger = logging.getLogger(__name__)


@start_router.message(Command("start"))
async def cmd_start(message: Message):
    logger.info(f"/start command was called by user {message.from_user.username}")
    await message.answer("Привет! Что тебе хочется?", reply_markup=start_keyboard())


@start_router.message(F.text == RusButtons.BACK)
async def cmd_start(message: Message):
    logger.info(f"Back button was pressed by user {message.from_user.username}")
    await message.answer("Возвращаемся назад", reply_markup=start_keyboard())
