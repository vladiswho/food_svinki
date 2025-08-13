import logging
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from locales import RusButtons
from src.keyboards.all_keyboards import post_diet_keyboard, start_keyboard, back_keyboard, confirm_keyboard
from src.utils.utils import check_if_admin, save_file
from src.application.bot import bot

post_recipes_router = Router()

logger = logging.getLogger(__name__)

class StatesConfig(StatesGroup):
    waiting_recipe = State()
    waiting_confirmation = State()


@post_recipes_router.message(F.text == RusButtons.POST_RECIPE)
async def post_recipe(message: Message):
    logger.info(f"Post recipe button was pressed by user {message.from_user.username}")
    if not check_if_admin(message.from_user.id):
        logger.warning(f"User with id {message.from_user.id} not allowed to press post recipe button")
        await message.answer("Вы не администратор!", reply_markup=start_keyboard())
    else:
        await message.answer("На какой прием пищи добавить рецепт?", reply_markup=post_diet_keyboard())



@post_recipes_router.message(F.text.in_([RusButtons.POST_BREAKFAST, RusButtons.POST_LUNCH, RusButtons.POST_DINNER]))
async def post_breakfast(message: Message, state: FSMContext):
    await state.clear()
    logger.info(f"Post breakfast|lunch|dinner button was pressed by user {message.from_user.username}")
    if not check_if_admin(message.from_user.id):
        logger.warning(f"User with id {message.from_user.id} not allowed to press post recipe button")
        await message.answer("Куда мы лезем? А? Администратором надо быть!", reply_markup=start_keyboard())
        return

    await message.answer("Введите рецепт или пришлите картинку рецепта", reply_markup=back_keyboard())
    match message.text:
        case RusButtons.POST_BREAKFAST:
            await state.update_data(meal="breakfast")
        case RusButtons.POST_LUNCH:
            await state.update_data(meal="lunch")
        case RusButtons.POST_DINNER:
            await state.update_data(meal="dinner")
    await state.set_state(StatesConfig.waiting_recipe)

@post_recipes_router.message(StatesConfig.waiting_recipe)
async def write_recipe(message: Message, state: FSMContext):
    if message.photo:
        photo_id = message.photo[-1].file_id
        await state.update_data(recipe_photo=photo_id)
        preview_message = "Вы отправили фото рецепта. Подтвердите сохранение."
        await message.answer_photo(photo=photo_id, caption=preview_message, reply_markup=confirm_keyboard())
    elif message.text:
        recipe_text = message.text
        await state.update_data(recipe_text=recipe_text)
        preview_message = f"Вы отправили рецепт:\n{recipe_text}\nПодтвердите сохранение."
        await message.answer(preview_message, reply_markup=confirm_keyboard())
    else:
        await message.answer("Пожалуйста, отправьте текст или фото рецепта.")
        return
    await state.set_state(StatesConfig.waiting_confirmation)

@post_recipes_router.message(StatesConfig.waiting_confirmation)
async def confirm_recipe(message: Message, state: FSMContext):
    if message.text == RusButtons.CONFIRM:
        data = await state.get_data()
        meal_type = data.get("meal")

        recipe_text = data.get("recipe_text")
        recipe_photo_id = data.get("recipe_photo")

        if recipe_text:
            try:
                save_file(meal_type=meal_type, recipe_text=recipe_text)
                await message.answer("Текстовый рецепт сохранён!", reply_markup=start_keyboard())
            except Exception as e:
                await message.answer(f"Ошибка при сохранении рецепта: {e}", reply_markup=start_keyboard())
        elif recipe_photo_id:
            try:
                tg_bot = bot.get_bot()
                file = await tg_bot.get_file(recipe_photo_id)
                file_path = file.file_path

                file_obj = await tg_bot.download_file(file_path)
                photo_bytes = file_obj.read()

                save_file(meal_type=meal_type, photo_file_id=recipe_photo_id, photo_bytes=photo_bytes)
                await message.answer("Фото рецепта сохранено!", reply_markup=start_keyboard())
            except Exception as e:
                await message.answer(f"Ошибка при сохранении фото: {e}", reply_markup=start_keyboard())
        else:
            await message.answer("Нет данных для сохранения.", reply_markup=start_keyboard())

        await state.clear()

    elif message.text == RusButtons.CANCEL:
        await message.answer("Действие отменено.", reply_markup=start_keyboard())
        await state.clear()

