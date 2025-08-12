from aiogram import types

from locales import RusButtons

back_button = types.KeyboardButton(text=RusButtons.BACK)


def diet_keyboard():
    diet_buttons = [
        [
            types.KeyboardButton(text=RusButtons.GET_BREAKFAST),
            types.KeyboardButton(text=RusButtons.GET_LUNCH),
            types.KeyboardButton(text=RusButtons.GET_DINNER),
        ],
        [back_button],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=3,
        keyboard=diet_buttons,
        input_field_placeholder="Кушать подано",
    )
    return keyboard


def start_keyboard():
    start_buttons = [
        [
            types.KeyboardButton(text=RusButtons.GET_RECIPE),
            types.KeyboardButton(text=RusButtons.POST_RECIPE),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2,
        keyboard=start_buttons,
        input_field_placeholder="Выберите опцию:",
    )
    return keyboard
