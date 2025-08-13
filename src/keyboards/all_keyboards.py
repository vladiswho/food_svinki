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



def post_diet_keyboard():
    diet_buttons = [
        [
            types.KeyboardButton(text=RusButtons.POST_BREAKFAST),
            types.KeyboardButton(text=RusButtons.POST_LUNCH),
            types.KeyboardButton(text=RusButtons.POST_DINNER),
        ],
        [back_button],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=3,
        keyboard=diet_buttons,
        input_field_placeholder="Я записываю",
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

def back_keyboard():
    button = [[types.KeyboardButton(text=RusButtons.BACK)]]
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
        keyboard=button,
        input_field_placeholder="Введите рецепт"
    )
    return keyboard

def confirm_keyboard():
    buttons = [[types.KeyboardButton(text=RusButtons.CONFIRM), types.KeyboardButton(text=RusButtons.CANCEL)]]
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2,
        keyboard=buttons,
        input_field_placeholder="Подтвердите действие"
    )
    return keyboard