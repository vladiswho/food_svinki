from dataclasses import dataclass


@dataclass
class RusButtons:
    BACK = "🔙 Назад"

    GET_RECIPE = "✈️ Получить рецепт"
    POST_RECIPE = "✍🏻 Новый рецепт"

    GET_BREAKFAST = "🍳 Завтрак"
    GET_LUNCH = "🍜 Обед"
    GET_DINNER = "🥗 Ужин"

    POST_BREAKFAST = "🖌 Завтрак"
    POST_LUNCH = "✒️ Обед"
    POST_DINNER = "🖍 Ужин"

    CONFIRM = "✅ Подтвердить"
    CANCEL = "❌ Отменить"
