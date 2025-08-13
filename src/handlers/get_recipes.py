import logging
import random
from aiogram import Router, F
from aiogram.types import Message, FSInputFile

from locales import RusButtons
from src.keyboards.all_keyboards import diet_keyboard
from src.utils.utils import read_file
from src.utils.recipes_cache import recipes_cache

get_recipes_router = Router()

logger = logging.getLogger(__name__)


@get_recipes_router.message(F.text == RusButtons.GET_RECIPE)
async def get_recipe(message: Message):
    logger.info(f"Get recipe button was pressed by user {message.from_user.username}")
    await message.answer("Выберите прием пищи:", reply_markup=diet_keyboard())


@get_recipes_router.message(F.text == RusButtons.GET_BREAKFAST)
async def get_breakfast(message: Message):
    logger.info(
        f"Get breakfast button was pressed by user {message.from_user.username}"
    )
    cached_recipes = recipes_cache.BREAKFAST

    if not cached_recipes:
        await message.answer("Не нашлось ни одного рецепта 😔", reply_markup=diet_keyboard())
        logger.warning("No recipes found in the recipes cache")
        return
    random_recipe = random.choice(cached_recipes)
    try:
        if ".txt" in random_recipe:
            file = read_file(f"./recipes/breakfast/{random_recipe}")
            await message.answer(file, reply_markup=diet_keyboard())
        else:
            photo_file = FSInputFile(path=f"./recipes/breakfast/{random_recipe}")
            await message.answer_photo(photo_file, reply_markup=diet_keyboard())
        logger.info("Success getting breakfast")
    except BaseException as e:
        logger.error(f"Cannot send breakfast: {e}")
        await message.answer("Произошла ошибка!", reply_markup=diet_keyboard())

@get_recipes_router.message(F.text == RusButtons.GET_LUNCH)
async def get_lunch(message: Message):
    logger.info(
        f"Get lunch button was pressed by user {message.from_user.username}"
    )
    cached_recipes = recipes_cache.LUNCH

    if not cached_recipes:
        await message.answer("Не нашлось ни одного рецепта 😔", reply_markup=diet_keyboard())
        logger.warning("No recipes found in the recipes cache")
        return
    random_recipe = random.choice(cached_recipes)
    try:
        if ".txt" in random_recipe:
            file = read_file(f"./recipes/lunch/{random_recipe}")
            await message.answer(file, reply_markup=diet_keyboard())
        else:
            photo_file = FSInputFile(path=f"./recipes/lunch/{random_recipe}")
            await message.answer_photo(photo_file, reply_markup=diet_keyboard())
        logger.info("Success getting lunch")
    except BaseException as e:
        logger.error(f"Cannot send lunch: {e}")
        await message.answer("Произошла ошибка!", reply_markup=diet_keyboard())

@get_recipes_router.message(F.text == RusButtons.GET_DINNER)
async def get_dinner(message: Message):
    logger.info(
        f"Get dinner button was pressed by user {message.from_user.username}"
    )
    cached_recipes = recipes_cache.DINNER

    if not cached_recipes:
        await message.answer("Не нашлось ни одного рецепта 😔", reply_markup=diet_keyboard())
        logger.warning("No recipes found in the recipes cache")
        return
    random_recipe = random.choice(cached_recipes)
    try:
        if ".txt" in random_recipe:
            file = read_file(f"./recipes/dinner/{random_recipe}")
            await message.answer(file, reply_markup=diet_keyboard())
        else:
            photo_file = FSInputFile(path=f"./recipes/dinner/{random_recipe}")
            await message.answer_photo(photo_file, reply_markup=diet_keyboard())
        logger.info("Success getting dinner")
    except BaseException as e:
        logger.error(f"Cannot send dinner: {e}")
        await message.answer("Произошла ошибка!", reply_markup=diet_keyboard())

